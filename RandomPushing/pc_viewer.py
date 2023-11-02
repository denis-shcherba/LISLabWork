from robotic import ry
import numpy as np
from visual import PCD
from arena import *
import json

#-- load parameters, typically automatically from 'rai.cfg'
ry.params_print()
verbose = 0

#-- define a configuration
C = ry.Config()

scanned_views = json.load(open("./data/scanned_obj.json"))

pcd_files = [f'point_cloud_{i}.pcd' for i in range(len(scanned_views))]

final_points = PCD(pcd_files, True)

pclFrame = C.addFrame('pcl')
pclFrame.setPointCloud(np.array(final_points))
pclFrame.setColor([1.,0.,1.])
C.view_recopyMeshes()

C.view(True)
