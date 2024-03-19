#!/usr/bin/python3

import argparse
import h5py
import numpy as np

parser = argparse.ArgumentParser(description='h5-file info')

parser.add_argument('FILE', type=str,
                    help='h5-file name')

def obj_info(name, obj):
    if isinstance(obj, h5py.Group):
        print(f'group: {obj.name}')
    if isinstance(obj, h5py.Dataset):
        print(f'  data: {obj.name}  shape: {obj.shape}  type: {obj.dtype}')

def main():
    args = parser.parse_args()

    print(f'== parsing H5 file \'{args.FILE}\'')
    try:
        with h5py.File(args.FILE, 'r') as fil:
            fil.visititems(obj_info)
    except KeyboardInterrupt:
        sys.exit(1)

if __name__ == "__main__":
    main()
