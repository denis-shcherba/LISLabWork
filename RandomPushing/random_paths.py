from robotic import ry
import numpy as np

from quadratic_solver import line_circle_intersection, line_rect_intersection
from visual import plotLine

def segment_line(point1, point2, point_between):
    return [point1 + (point2 - point1) * 0.5 * (1-np.cos(np.pi * i/(point_between-1))) for i in range(point_between)]

def generate_waypointsv2(C, obj_pos, obj_width, robot_pos=np.array([0, 0]), inner_rad=.3, outer_rad=1, start_distance=.07, waypoints=None):

    success = False
    try:
        z = obj_pos[2]
    except:
        z = 0
    obj_pos = np.array((obj_pos[0], obj_pos[1]))
    robot_pos = np.array((robot_pos[0], robot_pos[1]))

    rob2obj_len = np.linalg.norm(obj_pos-robot_pos)
    
    if inner_rad:
        if rob2obj_len < inner_rad or rob2obj_len >= outer_rad:
            print("Object is outside of arena!")
            return None, None, None, None, success
    else:
        if rob2obj_len >= outer_rad:
            print("Object is outside of arena!")
            return None, None, None, None, success
    angle = np.random.random() * np.pi*2

    move_vec = np.array([np.cos(angle), np.sin(angle)])

    # obj_pos=posvector, move_vec= directions_vector, robot_pos = circle offset
    inner_points = line_circle_intersection(obj_pos, move_vec, robot_pos, inner_rad) if inner_rad else []
    outer_points = line_circle_intersection(obj_pos, move_vec, robot_pos, outer_rad)

    if inner_points:
        if np.linalg.norm(outer_points[1]-obj_pos) > np.linalg.norm(outer_points[0]-obj_pos):
            outer_inter = outer_points[0]
        else:
            outer_inter = outer_points[1]
        
        if len(inner_points) > 1:
            if np.linalg.norm(inner_points[1]-obj_pos) > np.linalg.norm(inner_points[0]-obj_pos):
                point0 = inner_points[0]
            else:
                point0 = inner_points[1]
        else:
            point0 = inner_points[0]
        point1 = outer_inter
    else:
        point0 = outer_points[0]
        point1 = outer_points[1]
    
    if C:
        plotLine(C, np.array([point0[0], point0[1], .651]), np.array([point1[0], point1[1], .651]))

    if np.random.choice([0, 1]):
        start_vec = point0-obj_pos
        end_vec = point1-obj_pos

    else:
        start_vec = point1-obj_pos
        end_vec = point0-obj_pos

    start_vec /= np.linalg.norm(start_vec)
    start_vec *= start_distance + obj_width
    start_point = obj_pos + start_vec

    end_vec *= np.random.random()
    end_point = obj_pos + end_vec

    end3d = np.array([end_point[0], end_point[1], z])
    start3d = np.array([start_point[0], start_point[1], z])
    if C:
        if waypoints:
            points = segment_line(start3d, end3d, waypoints)
            for i, p in enumerate(points):
                way = C.getFrame(f'way{i}')
                way.setPosition(p)
        else:
            way0 = C.getFrame('start_point')
            # t: position relative to cylinder , d: degrees arm rotation, d:degrees gripper rotation
            way0.setPosition(point0)

            way1 = C.getFrame('end_point')
            way1.setPosition(point1)

    success = True
    return start3d, end3d, point0, point1, success

def generate_waypoints_rect(C, obj_pos, obj_width, robot_pos=np.array([0, 0]), rect_width=.5, rect_height=.3, inner_rad=None, start_distance=.07, waypoints=None):

    success = False
    try:
        z = obj_pos[2]
    except:
        z = 0
    obj_pos = np.array((obj_pos[0], obj_pos[1]))
    robot_pos = np.array((robot_pos[0], robot_pos[1]))

    rob2obj_len = np.linalg.norm(obj_pos-robot_pos)
    
    if inner_rad:
        if rob2obj_len < inner_rad:
            print("Object is outside of arena!")
            return None, None, None, None, success
    else:
        if obj_pos[0] > robot_pos[0]+1/2*rect_width or obj_pos[0] < robot_pos[0]-1/2*rect_width or obj_pos[1] > robot_pos[1]+1/2*rect_height or obj_pos[1] < robot_pos[1]-1/2*rect_height:
            print("Object is outside of arena!")
            return None, None, None, None, success
    angle = np.random.random() * np.pi*2

    move_vec = np.array([np.cos(angle), np.sin(angle)])

    # obj_pos=posvector, move_vec= directions_vector, robot_pos = circle offset
    inner_points = line_circle_intersection(obj_pos, move_vec, robot_pos, inner_rad) if inner_rad else []
    outer_points = line_rect_intersection(obj_pos, move_vec, robot_pos, rect_width, rect_height)

    if inner_points:
        if np.linalg.norm(outer_points[1]-obj_pos) > np.linalg.norm(outer_points[0]-obj_pos):
            outer_inter = outer_points[0]
        else:
            outer_inter = outer_points[1]
        
        if len(inner_points) > 1:
            if np.linalg.norm(inner_points[1]-obj_pos) > np.linalg.norm(inner_points[0]-obj_pos):
                point0 = inner_points[0]
            else:
                point0 = inner_points[1]
        else:
            point0 = inner_points[0]
        point1 = outer_inter
    else:
        point0 = outer_points[0]
        point1 = outer_points[1]
    
    if C:
        plotLine(C, np.array([point0[0], point0[1], .651]), np.array([point1[0], point1[1], .651]))

    if np.random.choice([0, 1]):
        start_vec = point0-obj_pos
        end_vec = point1-obj_pos

    else:
        start_vec = point1-obj_pos
        end_vec = point0-obj_pos

    start_vec /= np.linalg.norm(start_vec)
    start_vec *= start_distance + obj_width
    start_point = obj_pos + start_vec

    end_vec *= np.random.random()
    end_point = obj_pos + end_vec

    end3d = np.array([end_point[0], end_point[1], z])
    start3d = np.array([start_point[0], start_point[1], z])
    if C:
        if waypoints:
            points = segment_line(start3d, end3d, waypoints)
            for i, p in enumerate(points):
                way = C.getFrame(f'way{i}')
                way.setPosition(p)
        else:
            way0 = C.getFrame('start_point')
            # t: position relative to cylinder , d: degrees arm rotation, d:degrees gripper rotation
            way0.setPosition(point0)

            way1 = C.getFrame('end_point')
            way1.setPosition(point1)

    success = True
    return start3d, end3d, point0, point1, success

def push_problem(C, mutli_waypoints, hand_direction):
    '''creates a motion problem using "waypoint engineering" approach: define waypoints and motion relative to these'''

    # define a 2 waypoint problem in KOMO   
    komo = ry.KOMO()
    komo.setConfig(C, True)
    if mutli_waypoints: komo.setTiming(mutli_waypoints+1, 1, 1., 2)
    else: komo.setTiming(2., 1, 1., 0)

    komo.addControlObjective([], 0, 1e-2)
    komo.addControlObjective([], 1, 1e1)

    #komo.addControlObjective([], 0, 1e-2)



    komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
    komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)
    
    
    # komo.addObjective([], ry.FS.vectorZ, ['l_gripper'], ry.OT.eq, [1e1], hand_direction)


    if mutli_waypoints:
        #komo.addObjective([1], ry.FS.poseDiff, ['l_gripper', 'wayStart'], ry.OT.eq, [1e1])

        for i in range(mutli_waypoints):
            komo.addObjective([i+2], ry.FS.poseDiff, ['l_gripper', f'way{i}'], ry.OT.eq, [1e1])
    else:
        komo.addObjective([1.], ry.FS.poseDiff, ['l_gripper', 'start_point'], ry.OT.eq, [1e1])
        komo.addObjective([2.], ry.FS.poseDiff, ['l_gripper', 'end_point'], ry.OT.eq, [1e1])

    return komo

def compute_motion(C, multi_waypoints, hand_direction, verbose):
    '''solves the pushProblem'''

    #-- define a motion problem
    komo = push_problem(C, multi_waypoints, hand_direction)
    print('this is the defined motion problem: ', komo.reportProblem())
    #komo.view(verbose>0, 'this is the path configuration (two overlaying configurations, waypoints included)')

    #-- solve it -> compute motion
    ret = ry.NLP_Solver().setProblem(komo.nlp()).setOptions( stopTolerance=1e-2, verbose=4 ).solve()
    print(ret)
    print('RET TYPE:',type(ret))

    komo.view_close()
    
    return komo.getPath(), ret.feasible

def run_waypoints_one_by_one(bot, path, wait, C):
    '''run a list of waypoi        komo.addObjective([], ry.FS.vectorZ, ['l_gripper'], ry.OT.eq, [1e-5], hand_direction)
nts on the bot (or sim)'''

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
            