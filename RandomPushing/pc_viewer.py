import robotic as ry
import numpy as np
from visual import point2pointPCR
from arena import *
import json

#-- load parameters, typically automatically from 'rai.cfg'
ry.params_print()
verbose = 0

#-- define a configuration
C = ry.Config()

scanned_views = json.load(open("./data/scanned_obj.json"))
for i, v in enumerate(scanned_views):
    pclFrame = C.addFrame(f'pcl{i}')
    pclFrame.setPointCloud(np.array(v))
    pclFrame.setColor([0.,1.,0.])
    pclFrame.setPosition([0,.30,0])
    C.view_recopyMeshes()

pcd_files = [f'point_cloud_{i}.pcd' for i in range(len(scanned_views))]

final_points = point2pointPCR(pcd_files, False)

pclFrame = C.addFrame('pcl')
pclFrame.setPointCloud(np.array(final_points))
pclFrame.setColor([0.,0.,1.])
C.view_recopyMeshes()

C.view(True)
