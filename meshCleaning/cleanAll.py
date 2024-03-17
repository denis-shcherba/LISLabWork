#!/usr/bin/python3

import glob
from mesh_helper import *

#import signal
# def timeout(signum, frame):
#     raise Exception("timeout handler")
#signal.signal(signal.SIGALRM, timeout)

def main():
    #files = sorted(glob.glob('models/*.obj'))
    files = sorted(glob.glob('tr*.ply'))

    for file in files:
        if file[-5]=='-':
            continue
    #    if file[:11]<'models/86ff':
    #        continue
    #    if file[:13]>'models/room00':
    #        continue
        
        M = MeshHelper(file)

        if M.failed:
            continue

        M.autoScale()
        M.repair()
        # print('  watertight:', M.mesh.is_watertight)
        # print('  oriented:', M.mesh.is_winding_consistent)
        # if not M.mesh.is_watertight or M.mesh.is_empty:
        #     continue

        M.transformInertia()

        # M.export_ply()
        M.export_mesh(False)
        M.createPoints()
        M.createDecomposition()
        M.export_h5()
        M.export_scene()
            
        print('=== done: ', file)
        #exit()

if __name__ == "__main__":
    main()
