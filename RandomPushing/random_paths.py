from robotic import ry
import numpy as np

def segment_line(point1, point2, point_between):
    return [point1 + (point2 - point1) * 0.5 * (1-np.cos(np.pi * i/(point_between-1))) for i in range(point_between)]

def push_problem(C):
    '''creates a motion problem using "waypoint engineering" approach: define waypoints and motion relative to these'''

    # define a 2 waypoint problem in KOMO   
    komo = ry.KOMO()
    komo.setConfig(C, True)
    komo.setTiming(2., 1, 1., 0)

    komo.addControlObjective([], 0, 1e-2)
    #komo.addControlObjective([], 1, 1e1)

    komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
    komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)
   
    komo.addObjective([1.], ry.FS.poseDiff, ['l_gripper', 'start_point'], ry.OT.eq, [1e1])
    komo.addObjective([2.], ry.FS.poseDiff, ['l_gripper', 'end_point'], ry.OT.eq, [1e1])

    return komo

def compute_motion(C, verbose=0):
    '''solves the pushProblem'''

    #-- define a motion problem
    komo = push_problem(C)
    if verbose:
        print('this is the defined motion problem: ', komo.reportProblem())

    #-- solve it -> compute motion
    ret = ry.NLP_Solver().setProblem(komo.nlp()).setOptions( stopTolerance=1e-2, verbose=verbose).solve()
    if verbose:
        print(ret)
        print('RET TYPE:',type(ret))

    komo.view_close()
    
    return komo.getPath(), ret.feasible

def run_waypoints_one_by_one(bot, path, wait, C):

    # add the path points by appending individual waypoints to the spline buffer (spline will have zero velocity at waypoints)
    bot.moveTo(path[0], 1., False)
    while bot.getTimeToEnd() > 0:
        bot.sync(C, .1)

    bot.move(path, [4.])
    while bot.getTimeToEnd() > 0:
        bot.sync(C, .1)

    if wait:
        # wait for the spling buffer to be done, and sync C just for fun
        while bot.getTimeToEnd()>0:
            key = bot.sync(C, .1)
            # print(chr(key))
            if chr(key)=='q':
                return
            