import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Node:
    def __init__(self, config, parent=None):
        self.config = config
        self.parent = parent

def random_sample_3d(lower = 0, upper = 10):
    '''
    Randomly samples a 3D point within specified bounds.

    Args:
        lower (int): lower bound of the sampling distribution.
        upper (int): upper bound of the sampling distribution.

    Returns: 3D points (tuple): x,y,z coordinates.
    '''
    return (random.uniform(lower, upper), random.uniform(lower, upper), random.uniform(lower, upper))

def steer_3d(from_points, to_point, step_size=0.5):
    '''
    Steers or moves towards target objects within a given constraint i.e., step size.

    Args:
        from point (tuple): 3d points from the targer. 
        to points (tuple): 3d points towards the target.
        step size (float): constrains the movement from points to target point by step size.
    
    Returns:
        new 3d coordinates (tuple): 3D points.
    '''
    new_3dcoords = []
    # For each dimension (x, y, z)
    for i in range(3):  
        distance = to_point[i] - from_points[i]
        # take min between step size and computed distance  
        step = min(step_size, abs(distance))
        # linear iterpolation from points adhering to stepsize times step function 0 for 0 dist, -1 for dist < 0 and 1 for dist > 1
        new_coordinate = from_points[i] + step * math.copysign(1, distance) 
        new_3dcoords.append(new_coordinate)  # Add the new coordinate to the list
    return tuple(new_3dcoords)  # Return the new configuration as a tuple


def is_valid_config_3d(config, obstacles = [(2, 2, 2), (6, 6, 6)], obstacle_size = 1.0):
    '''
    Checks for collision. 

    Args: 
        config (tuple): 3D points.
        obstacles (list of tuples): 3D points. 
        obstacle size (float): size of obstacle. 

    Returns:
        True or False (bool): False if colesison detected True if valid path  
    '''
    # iterate over each obstacle
    # if distance between the two is smaller than obstacle size, then its collision
    # because points are within objects i.e., too close.  
    for obstacle in obstacles:
        # Check collision with each obstacle
        if distance_3d(config, obstacle) < obstacle_size:
            return False  # Collision detected
    return True 

def distance_3d(points1, points2):
    '''
    Computes eucledian distance between two 3D points.
    
    Args: 
        points1 (tuple): x,y,z of 3D point. 
        points2 (tuple): x,y,z of 3D point.
    
    Returns
        eucledian distance (float): distance between the two 3D points. 

    '''
    squared_sum = 0
    for i in range(3):  # Assuming 3D space with x, y, z coordinates
        squared_sum += (points1[i] - points2[i])**2
    return math.sqrt(squared_sum)

def rrt_3d(start, goal, max_iterations=3000):
    tree = [Node(start)]

    for _ in range(max_iterations):
        random_config = random_sample_3d()
        nearest_node = min(tree, key=lambda node: distance_3d(node.config, random_config))

        new_config = steer_3d(nearest_node.config, random_config)
        if is_valid_config_3d(new_config): # check collision
            new_node = Node(new_config, parent=nearest_node)
            tree.append(new_node)
            if distance_3d(new_config, goal) < 0.5:  # Adjust the threshold as needed
                return construct_path(new_node)

    return None

def construct_path(end_node):
    path = []
    node = end_node
    while node is not None:
        path.append(node.config)
        node = node.parent
    return list(reversed(path))

# Start and End Goal
start = (0, 0, 0)
goal = (10, 10, 10)

path = rrt_3d(start, goal)
if path:
    print("Path found:", path)
else:
    print("Path not found")



# Visualization function to plot the environment and path
def visualize_environment(path=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot obstacles
    for obstacle in [(2, 2, 2), (6, 6, 6)]:
        ax.scatter(*obstacle, color='red', marker='s', s=100)

    # Plot path if available
    if path:
        path_coords = list(zip(*path))
        ax.plot(*path_coords, marker='o', color='blue')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

# Example usage and test
start = (0, 0, 0)
goal = (9, 9, 9)

path = rrt_3d(start, goal)
if path:
    print("Path found:", path)
    visualize_environment(path)
else:
    print("Path not found")
    visualize_environment()
