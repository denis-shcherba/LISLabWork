from robotic import ry

def setup_config(waypoints=None, obj_pos=[-.50, .1, .69], on_real=False):
    '''creates a config to work with'''

    C = ry.Config()
    #ry.params_add({'botsim/engine': 'kinematic'})
    C.addFile(ry.raiPath('../rai-robotModels/scenarios/pandaSingle.g'))

    f = C.addFrame("camera", "l_gripper")
    f.setShape(ry.ST.camera, [.1])
    f.addAttributes({'focalLength':0.895, 'width':640., 'height':360.})

    """
    if not on_real:
        C.addFrame('obj') \
            .setPosition(obj_pos) \
            .setShape(ry.ST.cylinder, size=[.08, .06]) \
            .setColor([1, .5, 0]) .setMass(.1) .setContact(True)
    """
    if waypoints:
        for i in range(waypoints):
            C.addFrame(f'way{i}') \
                .setShape(ry.ST.sphere, size=[.01]) \
                .setPosition([0, .0, .0]) \
                .setColor([0, 0, 1])
    else:
        C.addFrame('start_point') \
            .setShape(ry.ST.sphere, size=[.01]) \
            .setPosition([0, .0, .0]) \
            .setColor([0, 0, 1])
        
        C.addFrame('end_point') \
            .setShape(ry.ST.sphere, size=[.01]) \
            .setPosition([0, .0, .0]) \
            .setColor([0, 0 , 1])
    return C

def startup_robot(C, on_real):
    '''start the robot (or simulation)'''

    bot = ry.BotOp(C, on_real)
    bot.home(C)

    bot.gripperClose(ry._left)
    while not bot.gripperDone(ry._left):
        bot.sync(C, .1)
    return bot
