from robotic import ry
import numpy as np
import matplotlib.pyplot as plt
import cv2


def getObject(bot, ry_config):
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

    print(points)
    """middlepoint = [
        sum([p[0] for p in points])/len(points),
        sum([p[1] for p in points])/len(points),
        sum([p[2] for p in points])/len(points)
    ]"""
    array_stack = np.stack(points, axis=0)

# Compute the mean array along axis 0
    middlepoint = np.mean(array_stack, axis=0)
    
    #middlepoint = np.mean(points)
    print(middlepoint)

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
        .setColor([1, 0, 0])
