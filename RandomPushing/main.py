from robotic import ry
import numpy as np
import json

from config import setup_config, startup_robot
from random_paths import generate_waypoints, compute_motion, run_waypoints_one_by_one
from visual import getObject

WAYPOINTS = 16
            
def path_object_top(C):
    way = C.getFrame('view_start')
    if not way:
        way = C.addFrame('view_start', "obj")
        way.setShape(ry.ST.marker, size=[.1])
        way.setRelativePose(f't(0 0 .5)')

    way = C.getFrame('view_end')
    if not way:
        way = C.addFrame('view_end', "obj")
        way.setShape(ry.ST.marker, size=[.1])
        way.setRelativePose(f't(0 0 .3)')
    
    komo = ry.KOMO()
    komo.setConfig(C, True)
    komo.setTiming(2., 1, 1., 0)

    #komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
    komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)

    komo.addObjective([], ry.FS.vectorZ, ["l_gripper"], ry.OT.eq, [0.5], [0, 0, 1])

    komo.addObjective([1.], ry.FS.positionDiff, ['l_gripper', 'view_start'], ry.OT.eq, [1e1])
    komo.addObjective([2.], ry.FS.positionDiff, ['l_gripper', 'view_end'], ry.OT.eq, [1e1])

    ry.NLP_Solver() \
        .setProblem(komo.nlp()) \
        .setOptions(stopTolerance=1e-2, verbose=0) \
        .solve()
        
    # Move robot throught generated path
    bot.move(komo.getPath(), [2.])
    while bot.getTimeToEnd() > 0:
        bot.sync(C, .1)

    # C = getObject(bot, C)


if __name__ == "__main__":

    #-- load parameters, typically automatically from 'rai.cfg'
    ry.params_print()
    verbose = 1

    #-- define a configuration
    C = setup_config(WAYPOINTS)
    key = C.view(verbose>0, 'happy with the config?')
    print('key pressed: ', chr(key)) #use this for basic interaction, e.g. aborting the program
    if chr(key)=='q':
        exit()

    bot = startup_robot(C)
    path_object_top(C)

    data = []
    non_f = 0
    for i in range(1):
        #-- compute a motion (debug this inside the method)
        start, end = generate_waypoints(C)
        path, feasible = compute_motion(C, verbose)
        print('returned path shape: ', type(path), path.shape)

        #-- now, if we're happy with the motion, send it to the robot
        if feasible:
            d = {}
            d["way_pos"] = {}
            d["obj_pos"] = {}
            objp = C.getFrame("obj").getPosition()
            d["obj_pos"]["start"] = [o for o in objp]

            # send the path by individually sending waypoints 
            run_waypoints_one_by_one(bot, path, True, C)

            # shutdown things
            bot.home(C)

            d["way_pos"]["start"] = start
            d["way_pos"]["end"] = end
            objp = C.getFrame("obj").getPosition()
            d["obj_pos"]["end"] = [o for o in objp]
            data.append(d)

        else: non_f += 1

    with open('data.json', 'w') as f:
        json.dump(data, f)

    print("Non feasable paths: ", non_f)
    del bot