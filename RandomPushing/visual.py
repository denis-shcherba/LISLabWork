from robotic import ry
import numpy as np
from utils.ransac import point_above_plane, get_plane_from_points
import json

def getFilteredPointCloud(bot, ry_config, arena, z_cutoff=.67):
    bot.sync(ry_config, .0)
    rgb, depth, points = bot.getImageDepthPcl('cameraWrist', False)

    new_rgb = []
    for lines in rgb:
        for c in lines: 
            new_rgb.append(c.tolist())
    rgb = new_rgb

    new_p = []
    for lines in points:
        for p in lines: 
            new_p.append(p.tolist())
    points = new_p

    new_rgb = []
    new_p = []
    for i, p in enumerate(points):
        if sum(p) != 0:
            new_rgb.append(rgb[i])
            new_p.append(p)
    points = np.array(new_p)
    
    cameraFrame = ry_config.getFrame("cameraWrist")

    R, t = cameraFrame.getRotationMatrix(), cameraFrame.getPosition()

    points = points @ R.T
    points = points + np.tile(t.T, (points.shape[0], 1))

    objectpoints=[]
    colors = []
    for i, p in enumerate(points):
        if p[2] > z_cutoff and arena.point_in_arena(np.array(p)):
            objectpoints.append(p)
            colors.append(rgb[i])
    return objectpoints, colors

def getObject(bot, ry_config, arena, use_ransac=False):
    """
    Computes center of point cloud from real sense sensor. 

    Args:
        bot (roboter) : 
        ry_config (environment config) :

    Returns:
        Cloud center or middle point (float list): [x, y, z].

    """

    if use_ransac:
        points, _ = getFilteredPointCloud(bot, ry_config, arena, z_cutoff=0)
        normal, plane_point = get_plane_from_points(points, ry_config)
        npoints = []
        for p in points:
            if point_above_plane(p, normal, plane_point):
                npoints.append(p)
        points = npoints
    else:
        points, _ = getFilteredPointCloud(bot, ry_config, arena)

    if not points:
        print("Object not found!")
        return []

    min_coor = np.array([
        min([p[0] for p in points]),
        min([p[1] for p in points]),
        min([p[2] for p in points])
    ])

    max_coor = np.array([
        max([p[0] for p in points]),
        max([p[1] for p in points]),
        max([p[2] for p in points])
    ])

    midpoint = (max_coor+min_coor)/2
    
    pclFrame = ry_config.getFrame("pcl")
    if not pclFrame:
        pclFrame = ry_config.addFrame('pcl')
        pclFrame.setPointCloud(np.array(points))
        pclFrame.setColor([0.,1.,0.]) #only to see it when overlaying with truth
        ry_config.view_recopyMeshes()

        ry_config.addFrame('mid_point') \
            .setPosition(midpoint) \
            .setShape(ry.ST.marker, size=[.2]) \
            .setColor([1, 1, 0])
    else:
        pclFrame.setPointCloud(np.array(points))
        ry_config.view_recopyMeshes()
        ry_config.getFrame('mid_point') \
            .setPosition(midpoint)
    
    return midpoint.tolist()

def lookAtObj(bot, ry_config, objpos):
    ry_config.getFrame("predicted_obj").setPosition(objpos)
    q_now = ry_config.getJointState()

    # bot.home(ry_config)
    q_home = bot.get_qHome()

    komo = ry.KOMO()
    komo.setConfig(ry_config, True)
    komo.setTiming(1., 1, 1., 0)
    komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
    komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)

    # Should be predicted obj instead of obj
    komo.addObjective([1.], ry.FS.positionRel, ["predicted_obj", "cameraWrist"], ry.OT.eq, [1.], [.0, .0, .5])
    komo.addObjective([1.], ry.FS.position, ["l_gripper"], ry.OT.ineq, np.array([[.0, .0, -100.]]), [0, 0, 1])
    komo.addObjective([], ry.FS.qItself, [], ry.OT.sos, [.1], q_home)
    komo.addObjective([], ry.FS.qItself, [], ry.OT.sos, [.1], q_now)

    ret = ry.NLP_Solver() \
        .setProblem(komo.nlp()) \
        .setOptions(stopTolerance=1e-2, verbose=0) \
        .solve()
    
    print(ret)
        
    bot.moveTo(komo.getPath()[0], 1., False)
    while bot.getTimeToEnd() > 0:
        bot.sync(ry_config, .1)

def plotArena(middleP, innerR, outerR, C, resolution=48):
    '''
    Visualises the pushing area.

    Args: 
        middleP (np.ndarray): The center point of the arena in XYZ coordinates.
        innerR (int): The inner radius of the arena.
        outerR (ZZ): The outer radius of the arena.
        C: The object or container for visualization frames.
        resolution (int, optional): The number of points used to discretize the arena. Default is 48.

    Returns:
        None: Adds visualization frames representing red spheres for the inner and outer area.
    '''
    step_size = 2*np.pi/resolution
    for i in range(resolution):
        angle = step_size*i
        dir_vec = np.array([np.cos(angle), np.sin(angle), 0])
        outer_point = middleP + outerR*dir_vec

        if innerR:
            inner_point = middleP + innerR*dir_vec
            C.addFrame(f'inner_arena_{i}') \
                .setPosition(inner_point) \
                .setShape(ry.ST.sphere, size=[.02]) \
                .setColor([1, 0, 0])
        
        C.addFrame(f'outer_arena_{i}') \
            .setPosition(outer_point) \
            .setShape(ry.ST.sphere, size=[.02]) \
            .setColor([1, 0, 0])
        
def plotLine(ry_config, start, end, resolution=10):
    seg = end-start
    line_len = np.linalg.norm(seg)
    segsize = line_len / resolution
    seg /= line_len
    seg *= segsize
    for p in range(resolution+1):
        position = start + (seg * p)
        frame = ry_config.getFrame(f"line_{p}")
        if not frame:
            ry_config.addFrame(f"line_{p}") \
                .setPosition(position) \
                .setShape(ry.ST.sphere, size=[.02]) \
                .setColor([0, 1, 0])
        else:
            frame.setPosition(position)

def scanObject(bot, ry_config, obj_pos, arena, gripper_height=.3, gripper_distance=.2):

    all_points = []
    angle_step = 2*np.pi/8
    for i in range(8):
        angle = angle_step * i
        new_view = np.array([
            gripper_distance * np.sin(angle),
            gripper_distance * np.cos(angle),
            gripper_height
        ])

        ry_config.getFrame(f'view_point_{i}').setPosition(new_view+obj_pos)
        bot.sync(ry_config)

        komo = ry.KOMO()
        komo.setConfig(ry_config, True)
        komo.setTiming(1., 1, 1., 0)

        komo.addObjective([], ry.FS.accumulatedCollisions, [], ry.OT.eq)
        komo.addObjective([], ry.FS.jointLimits, [], ry.OT.ineq)

        komo.addObjective([1.], ry.FS.positionDiff, ['l_gripper', f'view_point_{i}'], ry.OT.eq, [1e1])
        komo.addObjective([1.], ry.FS.positionRel, ["predicted_obj", "cameraWrist"], ry.OT.eq, [1.], [.0, .0, -.3])

        ret = ry.NLP_Solver().setProblem(komo.nlp()).setOptions(stopTolerance=1e-2, verbose=0).solve()
        print(ret)
        bot.move(komo.getPath(), [3.])
        while bot.getTimeToEnd() > 0:
            bot.sync(ry_config, .1)

        points, _ = getFilteredPointCloud(bot, ry_config, arena)
        all_points.append([list(p) for p in points])

    json.dump(all_points, open("data/scanned_obj.json", "w"))
    return all_points

def voxelGridDownsampling(original_pc, voxel_space_dimensions=[10, 10, 10]):
    sampled_pc = []
    voxels = [
        [[[] for _ in range(voxel_space_dimensions[2])]
        for _ in range(voxel_space_dimensions[1])]
        for _ in range(voxel_space_dimensions[0])
    ]

    xs = [p[0] for p in original_pc]
    ys = [p[1] for p in original_pc]
    zs = [p[2] for p in original_pc]
    min_x = min(xs)
    max_x = max(xs)
    min_y = min(ys)
    max_y = max(ys)
    min_z = min(zs)
    max_z = max(zs)

    for point in original_pc:
        x = int(((point[0] - min_x)/ (max_x - min_x)) * voxel_space_dimensions[0])
        x = x if x != voxel_space_dimensions[0] else voxel_space_dimensions[0]-1
        y = int(((point[1] - min_y)/ (max_y - min_y)) * voxel_space_dimensions[1])
        y = y if y != voxel_space_dimensions[1] else voxel_space_dimensions[1]-1
        z = int(((point[2] - min_z)/ (max_z - min_z)) * voxel_space_dimensions[2])
        z = z if z != voxel_space_dimensions[2] else voxel_space_dimensions[2]-1
        voxels[x][y][z].append(np.array(point))

    for x in range(voxel_space_dimensions[0]):
        for y in range(voxel_space_dimensions[1]):
            for z in range(voxel_space_dimensions[2]):
                if len(voxels[x][y][z]) > 0:
                    sampled_pc.append(sum(voxels[x][y][z])/len(voxels[x][y][z]))

    return sampled_pc
