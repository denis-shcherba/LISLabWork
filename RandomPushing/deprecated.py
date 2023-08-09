def path_object_top(C):
    way = C.getFrame('view_start')
    if not way:
        way = C.addFrame('view_start', "obj")
        way.setShape(ry.ST.marker, size=[.1])
        way.setRelativePose(f't(0 0 .5)')

    way = C.getFrame('view_end')
    if not way:
        way = C.addFrame('view_end', "obj")
        way.setShape(ry.ST.marker, size=[.1])
        way.setRelativePose(f't(0 0 .3)')
    
    komo = ry.KOMO()
    komo.setConfig(C, True)
    komo.setTiming(2., 1, 1., 0)

    #komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
    komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)

    komo.addObjective([], ry.FS.vectorZ, ["l_gripper"], ry.OT.eq, [0.5], [0, 0, 1])

    komo.addObjective([1.], ry.FS.positionDiff, ['l_gripper', 'view_start'], ry.OT.eq, [1e1])
    komo.addObjective([2.], ry.FS.positionDiff, ['l_gripper', 'view_end'], ry.OT.eq, [1e1])

    ry.NLP_Solver() \
        .setProblem(komo.nlp()) \
        .setOptions(stopTolerance=1e-2, verbose=0) \
        .solve()
        
    # Move robot throught generated path
    bot.move(komo.getPath(), [2.])
    while bot.getTimeToEnd() > 0:
        bot.sync(C, .1)
        