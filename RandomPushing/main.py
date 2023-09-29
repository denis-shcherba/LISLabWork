from robotic import ry
import json
import numpy as np
from config import setup_config, startup_robot
from random_paths import compute_motion, run_waypoints_one_by_one
from visual import getObject, point2obj
from arena import *


INITIAL_OBJ_POS = [-.5, 0, .69]
DEBUG = False
OBJ_HEIGHT = .08

ON_REAL = False

robot_pos = np.array([-.54, -.17, .651])

if __name__ == "__main__":

    #-- load parameters, typically automatically from 'rai.cfg'
    ry.params_print()
    verbose = 0

    #-- define a configuration
    C = setup_config(INITIAL_OBJ_POS, ON_REAL)
    if DEBUG:
        key = C.view(verbose>0, 'happy with the config?')
        print('key pressed: ', chr(key)) #use this for basic interaction, e.g. aborting the program
        if chr(key)=='q':
            exit()

    bot = startup_robot(C, ON_REAL)

    data = []
    obj_pos = INITIAL_OBJ_POS

    # Generate Arena
    arena = RectangularArena(middleP=robot_pos, innerR=.1, width=0.7, height=0.8)
    arena.plotArena(C)

    # Point towards set initial object position
    point2obj(bot, C, np.array(obj_pos))

    # Capture midpoint from point cloud
    obj_pos  = getObject(bot, C, arena)
    
    for i in range(3):

        if not obj_pos: break

        bot.home(C)

        #-- compute a motion (debug this inside the method)
        way_start, way_end, _, _, success = arena.generate_waypoints(obj_pos, obj_width=.3, ry_config=C)

        if not success: break
        path, feasible = compute_motion(C, verbose)
        print('returned path shape: ', type(path), path.shape)

        #-- now, if we're happy with the motion, send it to the robot
        if feasible:
            obj_start = obj_pos

            # Move object
            run_waypoints_one_by_one(bot, path, True, C)
            # Check new object position
            point2obj(bot, C, np.array(obj_pos))
            obj_pos = getObject(bot, C, arena)
            
            # Store information
            data.append({
                "way_pos": {
                    "start": [i for i in way_start],
                    "end": [i for i in way_end]
                },
                "obj_pos": {
                    "start": [i for i in obj_start],
                    "end": [i for i in obj_pos]
                }
            })

    bot.home(C)
    with open('data/data.json', 'w') as f:
        json.dump(data, f)
