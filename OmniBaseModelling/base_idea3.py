#! /usr/bin/env python3
import sys
import numpy as np
from solid import scad_render_to_file
from solid.objects import cube, translate, union, rotate

SEGMENTS = 48

radial_vector0 = np.array([ 31., -19., 0.])
radial_vector0 /= np.linalg.norm(radial_vector0)
radial_vector1 = np.array([-31., -19., 0.])
radial_vector1 /= np.linalg.norm(radial_vector1)

side_count = 3
step_angle = 360/side_count
step_angle_rad = np.deg2rad(step_angle)
rad_size = 30 # Length from center to outer wheel

wheel_gap = 9
ctiw = 44 # Center to inner wheel support
ctow = wheel_gap+ctiw # Center to outer wheel support
wsl = 30 # Wheel support length

p1 = np.array([wsl*.5, ctiw, 0.])
p2 = np.array([np.sin(step_angle_rad), np.cos(step_angle_rad), 0.]) * ctiw - np.array([np.sin(step_angle_rad+np.pi*.5), np.cos(step_angle_rad+np.pi*.5), 0.]) * wsl*.5
boll = np.linalg.norm(p1-p2) # Big outer lines length
bolr = np.linalg.norm((p1+p2)*.5)# Big outer lines rad length

# Circular inner support
p3 = (p1+p2)*.5
p2 = np.array([-np.sin(step_angle_rad), np.cos(step_angle_rad), 0.]) * ctiw - np.array([-np.sin(step_angle_rad+np.pi*.5), np.cos(step_angle_rad+np.pi*.5), 0.]) * wsl*.5
p1 = np.array([-wsl*.5, ctiw, 0.])
p4 = (p1+p2)*.5
cil = np.linalg.norm(p3-p4) # Big outer lines length
cir = np.linalg.norm((p3+p4)*.5)# Big outer lines rad length

# Radial connections
p1 = np.array([0, ctiw, 0.])
p2 = (p4+p3)*.5
rcl = np.linalg.norm(p1-p2)
rcr = np.linalg.norm((p1+p2)*.5)

def basic_geometry():

    shapes = []
    for i in range(side_count):
        dir_vector = np.array([np.sin(i*step_angle_rad), np.cos(i*step_angle_rad), 0.])
        rot = -step_angle*i
        outer_wheel_support = union()(
                                translate(dir_vector*(ctow+1))(
                                    rotate((0, 0, rot))(
                                        cube([wsl, 2, 4], center=True))))
        shapes.append(outer_wheel_support)
        inner_wheel_support = union()(
                                translate(dir_vector*(ctiw+1))(
                                    rotate((0, 0, rot))(
                                        cube([wsl, 2, 4], center=True))))
        shapes.append(inner_wheel_support)

        inner_circle = union()(
                            translate(dir_vector*(cir+1))(
                                rotate((0, 0, rot))(
                                    cube([cil, 2, 4], center=True))))
        shapes.append(inner_circle)

        radial_support = union()(
                            translate(dir_vector*(rcr+1))(
                                rotate((0, 0, rot+90))(
                                    cube([rcl, 2, 4], center=True))))
        shapes.append(radial_support)

        dir_vector = np.array([np.sin(i*step_angle_rad+step_angle_rad*.5), np.cos(i*step_angle_rad+step_angle_rad*.5), 0.])
        rot -= step_angle*.5
        big_outer_line = union()(
                            translate(dir_vector*(bolr+1))(
                                rotate((0, 0, rot))(
                                    cube([boll, 2, 4], center=True))))
        shapes.append(big_outer_line)

    return union()(*shapes)

if __name__ == '__main__':
    out_dir = sys.argv[1] if len(sys.argv) > 1 else None

    a = basic_geometry()

    # Adding the file_header argument as shown allows you to change
    # the detail of arcs by changing the SEGMENTS variable.  This can
    # be expensive when making lots of small curves, but is otherwise
    # useful.
    file_out = scad_render_to_file(a, out_dir=out_dir, file_header=f'$fn = {SEGMENTS};')
    print(f"{__file__}: SCAD file written to: \n{file_out}")
