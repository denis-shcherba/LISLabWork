import glob
from mesh_helper import *
import argparse


VISUALIZE = False
VERBOSE = 0

def main():
    files = sorted(glob.glob('giraffe.ply'))

    parser = argparse.ArgumentParser(description="This program demonstrates argument parsing with help option.")
    # parser.add_argument("argument1", type=str, help="The first argument you want to pass.")
    # parser.add_argument("argument2", type=int, help="The second argument (integer) you want to pass.")


    parser.add_argument("-v", "--view", action="store_true", help="Launches into ry-view mode after mesh processing (optional).")

    args = parser.parse_args()

    for file in files:

        
        M = MeshHelper(file)

        if M.failed:
            continue

        M.autoScale()
        M.repair()

        if VERBOSE == 2: 
            print('  watertight:', M.mesh.is_watertight)
            print('  oriented:', M.mesh.is_winding_consistent)


        M.transformInertia()
        M.export_ply()
        M.export_mesh(False)
        M.createPoints()
        M.createDecomposition()
        M.export_h5()
        gFile = M.export_scene()
            
        print('=== done: ', file)
        
        if args.view:
            import robotic as ry
            import sys 
            try:
                C = ry.Config()
                C.watchFile(gFile)
            except KeyboardInterrupt:
                sys.exit(1)

if __name__ == "__main__":
    main()



