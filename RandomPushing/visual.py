from robotic import ry
import numpy as np
import matplotlib.pyplot as plt
import cv2

def getObject(bot, ry_config):
    rgb, depth, points = bot.getImageDepthPcl('camera', False)

    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, (10, 100, 20), (25, 255, 255))
    only_object = cv2.bitwise_and(rgb, rgb, mask=mask)

    ry_config.delFrame('pcl')
    pclFrame = ry_config.addFrame('pcl', 'camera')
    pclFrame.setPointCloud(points, rgb)
    pclFrame.setColor([1.,0.,0.]) #only to see it when overlaying with truth
    ry_config.view_recopyMeshes()

    return ry_config
