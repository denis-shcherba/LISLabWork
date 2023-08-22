from robotic import ry
import numpy as np
from sklearn.decomposition import PCA
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
    
    new_p = []
    for lines in points:
        for p in lines: 
            if sum(p) != 0:
                new_p.append(p)

    points = new_p
    cameraFrame = ry_config.getFrame("camera")
    R, t = cameraFrame.getRotationMatrix(), cameraFrame.getPosition()

    points = [R@p+t for p in points]

    objectpoints=[]
    for p in points:
        if p[2] > .655:
            objectpoints.append(p)
    points = objectpoints

    if not points: return [0, 0, 0]

    # Compute the mean array along axis 0
    array_stack = np.stack(points, axis=0)
    middlepoint = np.mean(array_stack, axis=0)
    """
    #middlepoint = np.power(np.prod(array_stack, axis=0), 1.0 / len(points))
    pca = PCA(n_components=3)
    pca.fit(array_stack)
    middlepoint = pca.mean_
    print(middlepoint)
    """

    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, (10, 100, 20), (25, 255, 255))
    only_object = cv2.bitwise_and(rgb, rgb, mask=mask)
    
    pclFrame = ry_config.getFrame("pcl")
    if not pclFrame:
        pclFrame = ry_config.addFrame('pcl')
        pclFrame.setPointCloud(np.array(points))
        pclFrame.setColor([0.,1.,0.]) #only to see it when overlaying with truth
        ry_config.view_recopyMeshes()

        ry_config.addFrame('mid_point') \
            .setPosition(middlepoint) \
            .setShape(ry.ST.marker, size=[.2]) \
            .setColor([1, 1, 0])
    else:
        pclFrame.setPointCloud(np.array(points))
        ry_config.view_recopyMeshes()
        ry_config.getFrame('mid_point') \
            .setPosition(middlepoint)
    
    return middlepoint

def point2obj(bot, ry_config, objpos):
    C = ry_config
    bot.home(C)
    komo = ry.KOMO()
    komo.setConfig(C, True)
    komo.setTiming(1., 1, 1., 0)
    komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
    komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)

    # Robot gripper has to be looking down
    # opos = C.getFrame("obj").getPosition()
    gpos = C.getFrame("l_gripper").getPosition()
    komo.addObjective([1.], ry.FS.vectorZ, ["l_gripper"], ry.OT.eq, [1e1], gpos-objpos)

    ret = ry.NLP_Solver() \
        .setProblem(komo.nlp()) \
        .setOptions(stopTolerance=1e-2, verbose=0) \
        .solve()
    
    print(ret)
        
    bot.moveTo(komo.getPath()[0], 1., False)
    while bot.getTimeToEnd() > 0:
        bot.sync(C, .1)

def plotArena(middleP, innerR, outerR, C, resolution=48):
    
    step_size = 2*np.pi/resolution
    for i in range(resolution):
        angle = step_size*i

        dir_vec = np.array([np.cos(angle), np.sin(angle), 0])
        inner_point = middleP + innerR*dir_vec
        outer_point = middleP + outerR*dir_vec

        C.addFrame(f'inner_arena_{i}') \
            .setPosition(inner_point) \
            .setShape(ry.ST.sphere, size=[.02]) \
            .setColor([1, 0, 0])
        
        C.addFrame(f'outer_arena_{i}') \
            .setPosition(outer_point) \
            .setShape(ry.ST.sphere, size=[.02]) \
            .setColor([1, 0, 0])