from robotic import ry
import json
import numpy as np
from config import setup_config, startup_robot
from random_paths import generate_waypointsv2, compute_motion, run_waypoints_one_by_one
from visual import getObject, point2obj, plotArena

WAYPOINTS = 6
INITIAL_OBJ_POS = [-.50, .1, .69]
DEBUG = False
OBJ_HEIGHT = .08

INR = .25
OTR = .8

robot_pos = np.array([0, -0.21, .651])

if __name__ == "__main__":

    #-- load parameters, typically automatically from 'rai.cfg'
    ry.params_print()
    verbose = 1

    #-- define a configuration
    C = setup_config(WAYPOINTS, INITIAL_OBJ_POS)
    if DEBUG:
        key = C.view(verbose>0, 'happy with the config?')
        print('key pressed: ', chr(key)) #use this for basic interaction, e.g. aborting the program
        if chr(key)=='q':
            exit()

    bot = startup_robot(C)

    data = []
    non_f = 0
    obj_pos = INITIAL_OBJ_POS

    # first input to plotArena hardcodes radius pos x,y,z
    plotArena(robot_pos, INR, OTR, C)

    point2obj(bot, C, np.array(obj_pos))
    # getObj returns middlepoint or objpos, but no dist atm
    obj_pos  = getObject(bot, C) 
    dist = np.linalg.norm(C.getFrame("camera").getPosition()-obj_pos)
    if dist != None: 

        for i in range(10000):

            if not obj_pos:
                print("Can't find object!")
                break

            bot.home(C)

            #-- compute a motion (debug this inside the method)
            way_start, way_end, _, _, success = generate_waypointsv2(C, obj_pos, obj_width=.3, robot_pos=robot_pos, inner_rad=INR, outer_rad=OTR, waypoints=WAYPOINTS)
            if not success: break
            path, feasible = compute_motion(C, WAYPOINTS, np.array(way_start) - np.array(way_end), verbose)
            print('returned path shape: ', type(path), path.shape)

            #-- now, if we're happy with the motion, send it to the robot
            if feasible:
                d = {}
                d["way_pos"] = {}
                d["obj_pos"] = {}
                d["obj_pos"]["start"] = [i for i in obj_pos]
                d["way_pos"]["start"] = [i for i in way_start] 

                # send the path by individually sending waypoints 
                run_waypoints_one_by_one(bot, path, True, C)

            else:
                non_f += 1
                continue
                    
            point2obj(bot, C, np.array(obj_pos))
            obj_pos = getObject(bot, C)
            
            d["way_pos"]["end"] = [i for i in way_end]

            d["obj_pos"]["end"] = [i for i in obj_pos]

            data.append(d)

    bot.home(C)
    with open('data.json', 'w') as f:
        json.dump(data, f)

    print("Non feasable paths: ", non_f)
    del bot