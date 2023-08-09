from robotic import ry

def setup_config(waypoints=None):
    '''creates a config to work with'''

    C = ry.Config()
    #ry.params_add({'botsim/engine': 'kinematic'})
    C.addFile(ry.raiPath('../rai-robotModels/scenarios/pandaSingle.g'))

    f = C.addFrame("camera", "l_gripper")
    f.setShape(ry.ST.camera, [.1])
    f.addAttributes({'focalLength':0.895, 'width':640., 'height':360.})

    C.addFrame('obj') \
        .setPosition([-.50, .1, .69]) \
        .setShape(ry.ST.cylinder, size=[.08, .06]) \
        .setColor([1, .5, 0]) .setMass(.1) .setContact(True)
    
    if waypoints:
        for i in range(waypoints):
            way = C.addFrame(f'way{i}', "obj")
            way.setShape(ry.ST.marker, size=[.1])
    else:
        way0 = C.addFrame('start_point', "obj")
        way0.setShape(ry.ST.marker, size=[.1])
        way1 = C.addFrame('end_point', "obj")
        way1.setShape(ry.ST.marker, size=[.1])
    return C

def startup_robot(C):
    '''start the robot (or simulation)'''

    bot = ry.BotOp(C, False)
    bot.home(C)

    bot.gripperClose(ry._left)
    while not bot.gripperDone(ry._left):
        bot.sync(C, .1)
    return bot
