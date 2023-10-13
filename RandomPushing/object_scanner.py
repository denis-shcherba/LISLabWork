from robotic import ry
import numpy as np
from config import setup_config, startup_robot
from visual import getObject, lookAtObj, scanObject
from arena import *
from time import sleep


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
    arena = CircularArena(middleP=robot_pos, innerR=None, outerR=.3)
    arena.plotArena(C)

    # Point towards set initial object position
    lookAtObj(bot, C, np.array(obj_pos))

    # Capture midpoint from point cloud
    obj_pos  = getObject(bot, C, arena)
    scanObject(bot, C, np.array(obj_pos), arena)

    bot.home(C)

    C.view(True)
