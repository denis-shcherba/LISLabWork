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
        
def generate_waypoints(C, mutli_waypoints):
    r = .15
    phi = np.random.random()*np.pi*2

    point0 = np.array([np.cos(phi), np.sin(phi), 0]) * r
    point1 = point0 * -(.08+(r*2))

    x_vec = point1 - point0
    unitz = np.array([0,0,1])
    cross_ = np.cross(x_vec, unitz)
    scaling = ( 2 * np.random.random() - 1 ) * .1
    offset = scaling * cross_/np.linalg.norm(cross_)

    #point0 += offset
    point0[2] = ( 2 * np.random.random() - 1 ) * .03
    #point1 += offset
    point1[2] = ( 2 * np.random.random() - 1 ) * .03

    gripper_angle = phi-(0.5*np.pi)

    if mutli_waypoints:
        points = segment_line(point0, point1, mutli_waypoints)
    
        way = C.getFrame('wayStart')
        way.setRelativePose(f't({points[0][0]} {points[0][1]} {points[0][2]+.07}) r({gripper_angle} 0 0 1) d(-45 1 0 0)')
        for i, p in enumerate(points):
            way = C.getFrame(f'way{i}')
            way.setRelativePose(f't({p[0]} {p[1]} {p[2]}) r({gripper_angle} 0 0 1) d(-45 1 0 0)')

    else:
        way0 = C.getFrame('start_point')
        # t: position relative to cylinder , d: degrees arm rotation, d:degrees gripper rotation
        way0.setRelativePose(f't({point0[0]} {point0[1]} {point0[2]}) r({gripper_angle} 0 0 1) d(-45 1 0 0)')

        way1 = C.getFrame('end_point')
        way1.setRelativePose(f't({point1[0]} {point1[1]} {point1[2]}) r({gripper_angle} 0 0 1) d(-45 1 0 0)')
    
    return [p for p in point0], [p for p in point1]
