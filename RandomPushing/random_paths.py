from robotic import ry
import numpy as np

def segment_line(point1, point2, point_between):
    return [point1 + (point2 - point1) * 0.5 * (1-np.cos(np.pi * i/(point_between-1))) for i in range(point_between)]

def generate_waypoints(C, mutli_waypoints):
    r = .15
    phi = np.random.random()*np.pi*2

    point0 = np.array([np.cos(phi), np.sin(phi), 0]) * r
    point1 = point0 * -2

    x_vec = point1 - point0
    unitz = np.array([0,0,1])
    cross_ = np.cross(x_vec, unitz)
    scaling = ( 2 * np.random.random() - 1 ) * .1
    offset = scaling * cross_/np.linalg.norm(cross_)

    #point0 += offset
    point0[2] = ( 2 * np.random.random() - 1 ) * .03
    #point1 += offset
    point1[2] = ( 2 * np.random.random() - 1 ) * .03

    gripper_angle = phi-(0.5*np.pi)

    if mutli_waypoints:
        points = segment_line(point0, point1, mutli_waypoints)
        for i, p in enumerate(points):
            way = C.getFrame(f'way{i}')
            way.setRelativePose(f't({p[0]} {p[1]} {p[2]}) r({gripper_angle} 0 0 1) d(-45 1 0 0)')
    else:
        way0 = C.getFrame('start_point')
        # t: position relative to cylinder , d: degrees arm rotation, d:degrees gripper rotation
        way0.setRelativePose(f't({point0[0]} {point0[1]} {point0[2]}) r({gripper_angle} 0 0 1) d(-45 1 0 0)')

        way1 = C.getFrame('end_point')
        way1.setRelativePose(f't({point1[0]} {point1[1]} {point1[2]}) r({gripper_angle} 0 0 1) d(-45 1 0 0)')
    
    return point0.tolist(), point1.tolist()


def push_problem(C, mutli_waypoints):
    '''creates a motion problem using "waypoint engineering" approach: define waypoints and motion relative to these'''

    # define a 2 waypoint problem in KOMO
    komo = ry.KOMO()
    komo.setConfig(C, True)
    if mutli_waypoints: komo.setTiming(mutli_waypoints, 1, 1., 2)
    else: komo.setTiming(2., 1, 1., 0)

    #komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
    komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)

    if mutli_waypoints:
        for i in range(mutli_waypoints):
            komo.addObjective([i+1], ry.FS.poseDiff, ['l_gripper', f'way{i}'], ry.OT.eq, [1e1])
    else:
        komo.addObjective([1.], ry.FS.poseDiff, ['l_gripper', 'start_point'], ry.OT.eq, [1e1])
        komo.addObjective([2.], ry.FS.poseDiff, ['l_gripper', 'end_point'], ry.OT.eq, [1e1])

    return komo

def compute_motion(C, verbose):
    '''solves the pushProblem'''

    #-- define a motion problem
    komo = push_problem(C)
    print('this is the defined motion problem: ', komo.reportProblem())
    #komo.view(verbose>0, 'this is the path configuration (two overlaying configurations, waypoints included)')

    #-- solve it -> compute motion
    ret = ry.NLP_Solver().setProblem(komo.nlp()).setOptions( stopTolerance=1e-2, verbose=4 ).solve()
    print(ret)
    print('RET TYPE:',type(ret))
    key = komo.view(verbose>0, 'happy with the motion?')
    if verbose>0 and chr(key)=='q':
        exit()

    komo.view_close()
    
    return komo.getPath(), ret.feasible

def run_waypoints_one_by_one(bot, path, wait, C):
    '''run a list of waypoints on the bot (or sim)'''

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