from robotic import ry
import numpy as np
from config import setup_config, startup_robot
from visual import point2obj, getFilteredPointCloud, getObject
from arena import CircularArena
from utils.visualize import viewPointCloud


WAYPOINTS = 6
INITIAL_OBJ_POS = [-.5, 0, .69]
DEBUG = False
OBJ_HEIGHT = .08

INR = None
OTR = .3

ON_REAL = True
USE_RANSAC = False

robot_pos = np.array([-.54, -.17, .651])

if __name__ == "__main__":

    #-- load parameters, typically automatically from 'rai.cfg'
    ry.params_print()
    verbose = 1

    #-- define a configuration
    C = setup_config(WAYPOINTS, INITIAL_OBJ_POS, False, debug=DEBUG)
    if DEBUG:
        key = C.view(verbose>0, 'happy with the config?')
        print('key pressed: ', chr(key)) #use this for basic interaction, e.g. aborting the program
        if chr(key)=='q':
            exit()

    bot = startup_robot(C, ON_REAL)
    obj_pos = INITIAL_OBJ_POS

    # first input to plotArena hardcodes radius pos x,y,z
    circArenaInOut = CircularArena(C=C, middleP=robot_pos, innerR=INR, outerR=OTR)
    circArenaInOut.plotArena()

    point2obj(bot, C, np.array(obj_pos))
    points, colors = getFilteredPointCloud(bot, C, robot_pos, outer_rad=OTR)
    viewPointCloud(points, colors)
