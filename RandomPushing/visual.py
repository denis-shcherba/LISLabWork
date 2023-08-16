from robotic import ry
import numpy as np
import matplotlib.pyplot as plt
import cv2


def getObject(bot, ry_config):
    rgb, depth, points = bot.getImageDepthPcl('camera', False)


    cameraFrame = ry_config.getFrame("camera")
    R, t = cameraFrame.getRotationMatrix(), cameraFrame.getPosition()

    points = [R@p+t for line in points for p in line]
    min_z = min([p[2] for p in points])
    print(min_z)
    objectpoints=[]
    for p in points:
        if p[2] > .651:
            objectpoints.append(p)
    points = objectpoints

    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, (10, 100, 20), (25, 255, 255))
    only_object = cv2.bitwise_and(rgb, rgb, mask=mask)

    pclFrame = ry_config.addFrame('pcl2')
    pclFrame.setPointCloud(np.array(points))
    pclFrame.setColor([0.,1.,0.]) #only to see it when overlaying with truth
    ry_config.view_recopyMeshes()
