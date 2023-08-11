from robotic import ry
import json
import numpy as np
from config import setup_config, startup_robot
from random_paths import generate_waypoints, compute_motion, run_waypoints_one_by_one
from bird_search import flyToPoint, getBirdView

WAYPOINTS = 6
INITIAL_OBJ_POS = [-.50, .1, .69]
DEBUG = False
OBJ_HEIGHT = .08

if __name__ == "__main__":

    #-- load parameters, typically automatically from 'rai.cfg'
    ry.params_print()
    verbose = 1

    #-- define a configuration
    C = setup_config(WAYPOINTS, INITIAL_OBJ_POS)
    key = C.view(verbose>0, 'happy with the config?')
    print('key pressed: ', chr(key)) #use this for basic interaction, e.g. aborting the program
    if chr(key)=='q':
        exit()

    bot = startup_robot(C)

    data = []
    non_f = 0

    obj_pos = INITIAL_OBJ_POS

    flyToPoint([obj_pos[0], obj_pos[1]], C, bot)
    obj_pos, dist = getBirdView(bot, C, debug=DEBUG)
    if dist != None: 
        
        while dist > 20:
            flyToPoint([obj_pos[0], obj_pos[1]], C, bot)
            obj_pos, dist = getBirdView(bot, C, debug=DEBUG)

        for i in range(1):
            bot.home(C)

            if dist:
                C.getFrame("predicted_obj").setPosition(np.array(obj_pos) + OBJ_HEIGHT*.5)

                #-- compute a motion (debug this inside the method)
                way_start, way_end = generate_waypoints(C, WAYPOINTS)
                path, feasible = compute_motion(C, WAYPOINTS, verbose)
                print('returned path shape: ', type(path), path.shape)

                #-- now, if we're happy with the motion, send it to the robot
                if feasible:
                    d = {}
                    d["way_pos"] = {}
                    d["obj_pos"] = {}
                    d["obj_pos"]["start"] = obj_pos
                    d["way_pos"]["start"] = way_start

                    # send the path by individually sending waypoints 
                    run_waypoints_one_by_one(bot, path, True, C)

                else:
                    non_f += 1
                    continue

                flyToPoint([obj_pos[0], obj_pos[1]], C, bot)
                obj_pos, dist = getBirdView(bot, C, debug=DEBUG)
                if dist == None: break
                while dist > 20:
                    flyToPoint([obj_pos[0], obj_pos[1]], C, bot)
                    obj_pos, dist = getBirdView(bot, C, debug=DEBUG)
                
                d["way_pos"]["end"] = way_end
                d["obj_pos"]["end"] = obj_pos
                data.append(d)
                

    bot.home(C)
    with open('data.json', 'w') as f:
        json.dump(data, f)

    print("Non feasable paths: ", non_f)
    del bot