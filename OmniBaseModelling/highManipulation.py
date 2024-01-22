import robotic as ry
import numpy as np
import matplotlib.pyplot as plt


def syncAndExit(C, bot, sync_time=.1, homing = True):
    key = bot.sync(C, .1)
    if chr(key) == "q":
        if(homing==True):
            bot.home(C)
        exit()


class RobotMan():
    def __init__(self, C):
        self.C = C


    def setupInverseKinematics(self, C: ry.Config, phases: int, enableCollisions: bool=True, slicesPerPhase: int=20) -> ry.KOMO:
        """
        """
        q_now = C.getJointState()

        komo = ry.KOMO()
        komo.setConfig(C, enableCollisions)

        komo.setTiming(phases, slicesPerPhase, 1., 2)

        komo.addControlObjective([], 0, 1e-1)
        komo.addControlObjective([], 1, 1e-1)
        komo.addControlObjective([], 2, 1e1)

        komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)
        if(enableCollisions):
            komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
        komo.addObjective([], ry.FS.qItself, [], ry.OT.sos, [.1], q_now)

        return komo


    def graspBox(self):
        """
        """
        self.setupInverseKinematics(self.C)
        pass


    def graspTopBox(self, time, obj, gripper="l_gripper", grasp_direction='xz') -> ry.KOMO():
        """
        grasp a box with a centered top grasp (axes fully aligned)
        """
        komo = self.setupInverseKinematics(self.C, 4)

        if grasp_direction == 'zx':
            align = [ry.FS.scalarProductXY, ry.FS.scalarProductXZ, ry.FS.scalarProductYZ]
        elif grasp_direction == 'zy':
            align = [ry.FS.scalarProductYY, ry.FS.scalarProductXZ, ry.FS.scalarProductYZ]
        elif grasp_direction == 'yx':
            align = [ry.FS.scalarProductXY, ry.FS.scalarProductXZ, ry.FS.scalarProductZZ]
        elif grasp_direction == 'yz':
            align = [ry.FS.scalarProductXX, ry.FS.scalarProductXZ, ry.FS.scalarProductZZ]
        elif grasp_direction == 'xy':
            align = [ry.FS.scalarProductYY, ry.FS.scalarProductYZ, ry.FS.scalarProductZZ]
        elif grasp_direction == 'xz':
            align = [ry.FS.scalarProductYX, ry.FS.scalarProductYZ, ry.FS.scalarProductZZ]
        else:
            raise Exception('pickDirection not defined:', grasp_direction)

        # position: centered
        komo.addObjective([time], ry.FS.positionDiff, [gripper, obj], ry.OT.eq, [1e1])

        # orientation: grasp axis orthogonal to target plane X-specific
        komo.addObjective([time-.2,time], align[0], [obj, gripper], ry.OT.eq, [1e0])
        komo.addObjective([time-.2,time], align[1], [obj, gripper], ry.OT.eq, [1e0])
        komo.addObjective([time-.2,time], align[2], [obj, gripper], ry.OT.eq, [1e0])

        return komo


    def grabBlock(self, C, bot, block):
        qHome = C.getJointState()

        komo = ry.KOMO(C, 1, 1, 0, False)
        komo.addObjective(
            times=[], 
            feature=ry.FS.jointState, 
            frames=[],
            type=ry.OT.sos, 
            scale=[1e-1], 
            target=qHome
        )
        komo.addObjective([], ry.FS.positionDiff, ['l_gripper', block], ry.OT.eq, [1e1])

        ret = ry.NLP_Solver(komo.nlp(), verbose=4) .solve()
        print(ret)

        q = komo.getPath()
        del komo #also closes komo view

        C.setJointState(q[0])

        komo = self.setupInverseKinematics(C, 1)

        komo.addObjective([], ry.FS.positionDiff, ['l_gripper', block], ry.OT.eq, [1e1])
        komo.addObjective([], ry.FS.scalarProductXY, ['l_gripper', block], ry.OT.eq, [1e1], [0])
        komo.addObjective([], ry.FS.scalarProductXZ, ['l_gripper', block], ry.OT.eq, [1e1], [0])
        komo.addObjective([], ry.FS.distance, ['l_palm', block], ry.OT.ineq, [1e1])

        return komo

    def endeffectorToPoint(self):
        """
        """
        pass
    

    def solveKomo(self, komo):
        ret = ry.NLP_Solver(komo.nlp(), verbose=0 ) .solve()
        print(ret)
        if ret.feasible:
            print('--- FEASIBLE ---')
        else:
            print('---  !!!!!!!!!!! NOT FEASIBLE !!!!!!!!!!! ---')

        q = komo.getPath()

        return q


class Debug():
    """
    """
    def __init__(self, C):
        self.C = C


    def plotPath(komo: ry.KOMO()) -> None:
        q = komo.getPath()
        plt.plot(q)
        plt.show()



############### Testing ####################

C = ry.Config()
C.addFile(ry.raiPath('scenarios/pandaSingle.g'))
th = .67    #table height
block1x, block1y = -.3, .04
C.addFrame('block1') \
    .setPosition([block1x, block1y, th]) \
    .setShape(ry.ST.ssBox, size=[.06,.12,.06,.002]) \
    .setColor([1,.5,0]) \
    .setContact(True) \
    .setMass(1e-2)
bot = ry.BotOp(C, False)
bot.home(C)
bot.gripperMove(ry._left, 0.07, .1)
while not bot.gripperDone(ry._left):
    syncAndExit(C, bot)

pickandplace = RobotMan(C)
komo = pickandplace.graspTopBox(3, block="block1")
q= pickandplace.solveKomo(komo)

C.setJointState(q[0])
bot.move(q, [5])



while bot.getTimeToEnd()>0:
    syncAndExit(C, bot)
bot.gripperClose(ry._left, width=.03, speed=.1)
while not bot.gripperDone(ry._left):
    syncAndExit(C, bot)