from robotic import ry
import numpy as np
from config import setup_config, startup_robot
from visual import getObject, lookAtObj, scanObject
from arena import *
from time import sleep
import json
import open3d as o3d
import os 
import matplotlib.pyplot as plt

INITIAL_OBJ_POS = [-.5, 0, .69]
DEBUG = False
OBJ_HEIGHT = .08

ON_REAL = True

robot_pos = np.array([-.54, -.17, .651])

if __name__ == "__main__":

    #-- load parameters, typically automatically from 'rai.cfg'
    ry.params_print()
    verbose = 0

    #-- define a configuration
    C = setup_config(INITIAL_OBJ_POS, ON_REAL)
    if DEBUG:
        key = C.view(verbose>0, 'happy with the config?')
        print('key pressed: ', chr(key)) #use this for basic interaction, e.g. aborting the program
        if chr(key)=='q':
            exit()

    bot = startup_robot(C, ON_REAL)

    data = []
    obj_pos = INITIAL_OBJ_POS

    # Generate Arena
    arena = CircularArena(middleP=robot_pos, innerR=None, outerR=.3)
    arena.plotArena(C)

    # Point towards set initial object position
    lookAtObj(bot, C, np.array(obj_pos))

    # Capture midpoint from point cloud
    obj_pos  = getObject(bot, C, arena)
    scanObject(bot, C, np.array(obj_pos), arena)
    bot.hold()
    bot.home(C)

    #C.view(True)
    del bot
    del C



# Load the original JSON file
with open('data/scanned_obj.json', 'r') as input_file:
    data = json.load(input_file)

# Ensure the data is a list of lists
if not isinstance(data, list) or not all(isinstance(item, list) for item in data):
    raise ValueError("The input data should be a list of lists.")

# Create a subdirectory for the PCD files
if not os.path.exists('data'):
    os.mkdir('data')

# Split the data into 8 separate point clouds
num_point_clouds = 8
data_per_point_cloud = len(data) // num_point_clouds

for i in range(num_point_clouds):
    start_idx = i * data_per_point_cloud
    end_idx = (i + 1) * data_per_point_cloud
    point_cloud = data[start_idx:end_idx]
    
    # Remove the outer brackets from each point cloud
    point_cloud = point_cloud[0]

    # Save each point cloud as a separate JSON file without additional brackets
    output_filename = f'data/point_cloud_{i}.json'
    with open(output_filename, 'w') as output_file:
        json.dump(point_cloud, output_file)

    print(f'Saved {output_filename}')

    with open(output_filename, 'r') as json_file:
        json_data = json.load(json_file)

    # Create a PointCloud object
    point_cloud_obj = o3d.geometry.PointCloud()

    # Set the points in the PointCloud
    point_cloud_obj.points = o3d.utility.Vector3dVector(json_data)

    # Save the PointCloud as a PCD file in the "data" subdirectory
    output_pcd_file = f'data/point_cloud_{i}.pcd'
    o3d.io.write_point_cloud(output_pcd_file, point_cloud_obj)

print("Splitting and saving completed.")


pcd_files = [
    'point_cloud_0.pcd',
    'point_cloud_1.pcd',
    'point_cloud_2.pcd',
    'point_cloud_3.pcd',
    'point_cloud_4.pcd',
    'point_cloud_5.pcd',
    'point_cloud_6.pcd',
    'point_cloud_7.pcd'
]

# Load the first point cloud as the initial reference
merged_cloud = o3d.io.read_point_cloud("data/"+pcd_files[0])

# Iterate through the remaining point clouds and align/merge
for pcd_file in pcd_files[1:]:
    # Load the next point cloud
    cloud_to_align = o3d.io.read_point_cloud("data/"+pcd_file)

    # Perform ICP registration
    icp_result = o3d.pipelines.registration.registration_icp(
        cloud_to_align, merged_cloud, 0.1, np.identity(4), o3d.pipelines.registration.TransformationEstimationPointToPoint())

    # Apply the transformation to align the point cloud with the reference
    cloud_to_align.transform(icp_result.transformation)
    print("Transformation:", icp_result.transformation)
    # Combine the aligned point cloud with the merged point cloud
    merged_cloud += cloud_to_align

# Save the merged point cloud to a new PCD file
o3d.io.write_point_cloud('merged_point_cloud.pcd', merged_cloud)

# Load the PCD file
#point_cloud = o3d.io.read_point_cloud("merged_point_cloud.pcd")
point_cloud = o3d.io.read_point_cloud("output.pcd")
# Convert the point cloud data to a NumPy array
points = np.asarray(point_cloud.points)

# Extract the X, Y, and Z coordinates
x = points[:, 0]
y = points[:, 1]
z = points[:, 2]

# Create a 2D scatter plot
plt.figure(figsize=(10, 10))
plt.scatter(x, y, s=0.1)  # Adjust the 's' parameter to control point size
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Scatter Plot of Point Cloud')
plt.show()

