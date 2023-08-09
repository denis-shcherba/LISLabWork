from robotic import ry
import matplotlib.pyplot as plt
import cv2
import numpy as np

def flyToPoint(point, C, bot):
    
    komo = ry.KOMO()
    komo.setConfig(C, True)
    komo.setTiming(1., 1, 1., 0)

    # komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
    # komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)
    komo.addObjective([], ry.FS.vectorZ, ["l_gripper"], ry.OT.eq, [0.5], [0, 0, 1])
    komo.addObjective([1.], ry.FS.position, ["l_gripper"], ry.OT.eq, [1e1], [point[0], point[1], 1.2])

    ret = ry.NLP_Solver() \
        .setProblem(komo.nlp()) \
        .setOptions(stopTolerance=1e-2, verbose=0) \
        .solve()
    
    print(ret)
        
    bot.moveTo(komo.getPath()[0], 1., False)
    while bot.getTimeToEnd() > 0:
        bot.sync(C, .1)

def getBirdView(bot):
    rgb, depth = bot.getImageAndDepth('camera')

    hsv = cv2.cvtColor(rgb, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(hsv, (10, 100, 20), (25, 255, 255))

    _, gray = cv2.threshold(mask, 1, 255, cv2.THRESH_BINARY)
    gray = cv2.bitwise_not(gray)
 
    blur = cv2.GaussianBlur(gray, (5, 5),
                       cv2.BORDER_DEFAULT)
    ret, thresh = cv2.threshold(blur, 200, 255,
                           cv2.THRESH_BINARY_INV)

    contours, hierarchies = cv2.findContours(
    thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    blank = np.zeros(thresh.shape[:2], dtype='uint8')
    cv2.drawContours(blank, contours, -1, (255, 0, 0), 1)

    for i in contours:
        M = cv2.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv2.drawContours(rgb, [i], -1, (0, 255, 0), 2)
            cv2.circle(rgb, (cx, cy), 7, (0, 0, 255), -1)
            cv2.putText(rgb, "center", (cx - 20, cy - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        # print(f"x: {cx} y: {cy}")

    # plt.imshow(rgb)
    # plt.show()
    h, w, _ = rgb.shape
    distance_to_center = np.sqrt((cx - w*.5)**2 + (cy - h*.5)**2)
    return cx, cy, distance_to_center
