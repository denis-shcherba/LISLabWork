from robotic import ry
import numpy as np
from utils.ransac import point_above_plane, get_plane_from_points

def point_in_arena(point, arena_pos, inner_rad=None, outer_rad=None, width=None, height=None):
    if outer_rad:
        if np.linalg.norm(arena_pos-point) >= outer_rad: return False
    if inner_rad:
        if np.linalg.norm(arena_pos-point) <= inner_rad: return False
    if width and height:
        lenvec = point-arena_pos
        if point[0]>=1/2*width+arena_pos[0] or point[0]<=-1/2*width+arena_pos[0]:
            return False
        elif point[1]>=1/2*height+arena_pos[1] or point[1]<=-1/2*height+arena_pos[1]: 
           return False
    return True

def getFilteredPointCloud(bot, ry_config, arena_pos, inner_rad=None, outer_rad=None, z_cutoff=.69, height =None, width=None):
    OFFSET=.04
    bot.sync(ry_config, .0)
    rgb, depth, points = bot.getImageDepthPcl('cameraWrist', False)

    new_p = []
    for lines in points:
        for p in lines: 
            if sum(p) != 0:
                new_p.append(p.tolist())
    points = np.array(new_p)

    cameraFrame = ry_config.getFrame("cameraWrist")

    R, t = cameraFrame.getRotationMatrix(), cameraFrame.getPosition()

    points = points @ R.T
    points = points + np.tile(t.T, (points.shape[0], 1))

    objectpoints=[]
    for p in points:
        if p[2] > z_cutoff and point_in_arena(np.array(p), arena_pos, inner_rad, outer_rad, width=width, height=height):
            objectpoints.append(p-np.array([0,0,OFFSET]))
    points = objectpoints
    return points

def getObject(bot, ry_config,arena_pos, inner_rad=None, outer_rad=None, use_ransac=False, width=None, height=None):
    """
    Computes center of point cloud from real sense sensor. 

    Args:
        bot (roboter) : 
        ry_config (environment config) :

    Returns:
        Cloud center or middle point (float list): [x, y, z].

    """

    if use_ransac:
        points = getFilteredPointCloud(bot, ry_config,  arena_pos, inner_rad=inner_rad, outer_rad=outer_rad, z_cutoff=0, width=width, height=height)
        normal, plane_point = get_plane_from_points(points, ry_config)
        npoints = []
        for p in points:
            if point_above_plane(p, normal, plane_point):
                npoints.append(p)
        points = npoints
    else:
        points = getFilteredPointCloud(bot, ry_config, arena_pos, inner_rad=inner_rad, outer_rad=outer_rad, width=width, height=height)

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
    #komo.addObjective([], ry.FS.positionDiff, ["l_gripper", "obj"], ry.OT.eq, [1e2], [.34])

    ret = ry.NLP_Solver() \
        .setProblem(komo.nlp()) \
        .setOptions(stopTolerance=1e-2, verbose=0) \
        .solve()
    
    print(ret)
        
    bot.moveTo(komo.getPath()[0], 1., False)
    while bot.getTimeToEnd() > 0:
        bot.sync(C, .1)

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
