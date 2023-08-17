from robotic import ry
import numpy as np
import matplotlib.pyplot as plt
import cv2


def getObject(bot, ry_config):
    """
    Computes center of point cloud from real sense sensor. 

    Args:
        bot (roboter) : 
        ry_config (environment config) :

    Returns:
        Cloud center or middle point (float list): [x, y, z].

    """
    bot.sync(ry_config, .1)
    rgb, depth, points = bot.getImageDepthPcl('camera', False)

    cameraFrame = ry_config.getFrame("camera")
    R, t = cameraFrame.getRotationMatrix(), cameraFrame.getPosition()

    points = [R@p+t for line in points for p in line]
    min_z = min([p[2] for p in points])

    print(min_z)
    objectpoints=[]
    for p in points:
        if p[2] > .655:
            objectpoints.append(p)
    points = objectpoints

    min_x = min([p[0] for p in points])
    min_y = min([p[1] for p in points])
    min_z = min([p[2] for p in points])
    max_x = max([p[0] for p in points])
    max_y = max([p[1] for p in points])
    max_z = max([p[2] for p in points])

    new_p = []
    c = 0 
    for p in points:
        if p[0] == max_x or p[1] == max_y or p[2] == max_z:
            c += 1
        else:
            new_p.append(p)

    points = new_p

    array_stack = np.stack(points, axis=0)

# Compute the mean array along axis 0
    middlepoint = np.mean(array_stack, axis=0)

    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, (10, 100, 20), (25, 255, 255))
    only_object = cv2.bitwise_and(rgb, rgb, mask=mask)

    pclFrame = ry_config.addFrame('pcl2')
    pclFrame.setPointCloud(np.array(points))
    pclFrame.setColor([0.,1.,0.]) #only to see it when overlaying with truth
    ry_config.view_recopyMeshes()

    ry_config.addFrame('mid_point') \
        .setPosition(middlepoint) \
        .setShape(ry.ST.marker, size=[.2]) \
        .setColor([1, 1, 0]) # yellow
    
    return middlepoint

def point2obj(bot, ry_config, objpos):
    C = ry_config
    komo = ry.KOMO()
    komo.setConfig(C, True)
    komo.setTiming(1., 1, 1., 0)
    komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
    komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)

    # Robot gripper has to be looking down
    # opos = C.getFrame("obj").getPosition()
    gpos = C.getFrame("l_gripper").getPosition()
    komo.addObjective([1.], ry.FS.vectorZ, ["l_gripper"], ry.OT.eq, [1e1], (objpos-gpos)*-1)

    ret = ry.NLP_Solver() \
        .setProblem(komo.nlp()) \
        .setOptions(stopTolerance=1e-2, verbose=0) \
        .solve()
    
    print(ret)
        
    bot.moveTo(komo.getPath()[0], 1., False)
    while bot.getTimeToEnd() > 0:
        bot.sync(C, .1)
