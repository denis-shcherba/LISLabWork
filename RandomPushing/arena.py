import numpy as np
from robotic import ry
from utils.quadratic_solver import line_circle_intersection, line_rect_intersection
from visual import plotLine

class Arena:
    def __init__(self, middleP=np.array([0, 0])):
        self.middleP = middleP

    def area(self):
        return self.width * self.height

#circular Arena with inner and outer circle
class CircularArena(Arena):
    def __init__(self, middleP, outerR, innerR=None):
        super().__init__(middleP)
        self.outerR = outerR
        self.innerR = innerR

    def area(self):
        outer_area = np.pi * self.outerR ** 2
        if self.innerR:
            inner_area = np.pi * self.innerR ** 2
        return outer_area - inner_area
    
    def plotArena(self, ry_config, resolution=48):
        '''
        Visualises the pushing area.
        Returns:
            None: Adds visualization frames representing red spheres for the inner and outer area.
        '''
        step_size = 2*np.pi/resolution
        for i in range(resolution):
            angle = step_size*i
            dir_vec = np.array([np.cos(angle), np.sin(angle), 0])
            outer_point = self.middleP + self.outerR*dir_vec

            if self.innerR:
                inner_point = self.middleP + self.innerR*dir_vec
                ry_config.addFrame(f'inner_arena_{i}') \
                    .setPosition(inner_point) \
                    .setShape(ry.ST.sphere, size=[.02]) \
                    .setColor([1, 0, 0])
            
            ry_config.addFrame(f'outer_arena_{i}') \
                .setPosition(outer_point) \
                .setShape(ry.ST.sphere, size=[.02]) \
                .setColor([1, 0, 0])
            
    def generate_waypoints(self, obj_pos, obj_width=0, start_distance=.07, ry_config=None):
        '''
        Steers or moves towards target objects within a given constraint i.e., step size.

        Args:
            obj_pos: Position of object in arena 
            obj_width: Width of the object
            start_distance: The distance of the starting waypoint to the object (default: 7cm)
            ry_config: Configuration of the rai simulation (only to plot the path/waypoints generated)
        
        Returns:
            Starting waypoint for push,
            Ending waypoint for push,
            Intersection with arena,
            Intersection with arena,
            Path generation success status
        '''

        # Check if object is inside the arena
        rob2obj_len = np.linalg.norm(obj_pos-self.middleP)
        if rob2obj_len >= self.outerR or (self.innerR and rob2obj_len < self.innerR):
            print("Object is outside of arena!")
            return None, None, None, None, False
        
        # Generate a random direction vector for the push
        angle = np.random.random() * np.pi*2
        move_vec = np.array([np.cos(angle), np.sin(angle)])

        # Calculate intersections with inner/outer circle
        inner_points = line_circle_intersection(obj_pos, move_vec, self.middleP, self.innerR) if self.innerR else []
        outer_points = line_circle_intersection(obj_pos, move_vec, self.middleP, self.outerR)

        # The intersection fuctions remove the z value of vector, so we nee to put it back
        try: z = obj_pos[2]
        except: z = 0
        inner_points = [np.array([i[0], i[1], z]) for i in inner_points]
        outer_points = [np.array([i[0], i[1], z]) for i in outer_points]

        # Select relevant intersection points
        if inner_points:
            if len(inner_points) <= 1 or (len(inner_points) > 1 and np.linalg.norm(inner_points[1]-obj_pos) > np.linalg.norm(inner_points[0]-obj_pos)):
                point0 = inner_points[0]
            else:
                point0 = inner_points[1]

            if np.linalg.norm(outer_points[1]-obj_pos) > np.linalg.norm(outer_points[0]-obj_pos):
                point1 = outer_points[0]
            else:
                point1 = outer_points[1]
        else:
            point0 = outer_points[0]
            point1 = outer_points[1]
    
        # Pick a random orientation for the vector
        if np.random.choice([0, 1]):
            start_vec = point0-obj_pos
            end_vec = point1-obj_pos

        else:
            start_vec = point1-obj_pos
            end_vec = point0-obj_pos

        start_vec /= np.linalg.norm(start_vec)
        start_vec *= start_distance + obj_width
        start_point = obj_pos + start_vec

        end_vec *= np.random.random()
        end_point = obj_pos + end_vec

        # Display the path in the rai simulation
        if ry_config:
            plotLine(ry_config, np.array([point0[0], point0[1], .651]), np.array([point1[0], point1[1], .651]))
            
            way0 = ry_config.getFrame('start_point')
            way0.setPosition(point0)
            way1 = ry_config.getFrame('end_point')
            way1.setPosition(point1)

        return start_point, end_point, point0, point1, True    


class RectangularArena(Arena):
    
    def __init__(self, middleP, width, height, innerR=None, middlePCirc=[]):
        super().__init__(middleP)
        self.width = width
        self.height = height
        self.innerR = innerR
        self.middlePCirc = middlePCirc if len(middlePCirc) else middleP

    def area(self):
        return self.width * self.height

    #TODO Implement plotArena for rectArena
    def plotArena(self, ry_config, resolution=48):
        '''
        Visualises the pushing area.
        Returns:
            None: Adds visualization frames representing red spheres for the inner and outer area.
        '''
        step_size = (2*self.height+2*self.width)/resolution  # You can keep the step size consistent for both circular and rectangular arenas
        """following: spaghetti code of doom"""
        step_size2 = 2*np.pi/resolution
        
        for i in range(resolution):
            angle = step_size * i
            angle2 = step_size2*i
            dir_vec_circ = np.array([np.cos(angle2), np.sin(angle2), 0])
            #middle_hypothenuse= np.sqrt(1/2*self.height+1/2 *self.width)
            if(angle <= self.height):
                outer_point = self.middleP   + np.array([-1/2*self.width, step_size*i-1/2*self.height,0])
            elif(angle > self.height and angle <= self.height+self.width):
                outer_point = self.middleP  + np.array([step_size*i-self.height  - 1/2*self.width, 1/2*self.height,0])
            elif(angle > self.height+self.width and angle <= self.height*2+self.width):
                outer_point = self.middleP  + np.array([1/2*self.width, -(step_size*i-self.height-self.width)+1/2*self.height,0])
            else:
               outer_point = self.middleP + np.array([step_size*i-2*self.height-self.width-1/2*self.width,-1/2*self.height,0])


            if self.innerR:
                inner_point = self.middlePCirc + self.innerR * dir_vec_circ
                ry_config.addFrame(f'inner_arena_{i}') \
                    .setPosition(inner_point) \
                    .setShape(ry.ST.sphere, size=[.02]) \
                    .setColor([1, 0, 0])

            dir_vec_rect = np.array([np.cos(angle), np.sin(angle), 0])  # Direction vector for rectangular arena
            #outer_point = self.middleP + np.array([self.width, self.height, 0]) * dir_vec_rect

            ry_config.addFrame(f'outer_arena_{i}') \
                .setPosition(outer_point) \
                .setShape(ry.ST.sphere, size=[.02]) \
                .setColor([1, 0, 0])
    
    def point_in_rect(self, point):
        return point[0] > self.middleP[0]+.5*self.width or point[0] < self.middleP[0]-.5*self.width or point[1] > self.middleP[1]+.5*self.height or point[1] < self.middleP[1]-.5*self.height
            
    def generate_waypoints(self, obj_pos, obj_width=0, start_distance=.07, ry_config=None):
        '''
        Steers or moves towards target objects within a given constraint i.e., step size.

        Args:
            obj_pos: Position of object in arena 
            obj_width: Width of the object
            start_distance: The distance of the starting waypoint to the object (default: 7cm)
            ry_config: Configuration of the rai simulation (only to plot the path/waypoints generated)
        
        Returns:
            Starting waypoint for push,
            Ending waypoint for push,
            Intersection with arena,
            Intersection with arena,
            Path generation success status
        '''
            
        # Check if object is inside the arena
        if self.point_in_rect(obj_pos) or (self.innerR and np.linalg.norm(obj_pos-self.middlePCirc) < self.innerR):
            print("Object is outside of arena!")
            return None, None, None, None, False
        
        # Generate a random direction vector for the push
        angle = np.random.random() * np.pi*2
        move_vec = np.array([np.cos(angle), np.sin(angle)])

        # Calculate intersections with inner/outer boundaries
        inner_points = line_circle_intersection(obj_pos, move_vec, self.middlePCirc, self.innerR) if self.innerR else []
        outer_points = line_rect_intersection(obj_pos, move_vec, self.middleP, self.width, self.height)

        # The intersection fuctions remove the z value of vector, so we nee to put it back
        try: z = obj_pos[2]
        except: z = None
        if z != None:
            inner_points = [np.array([i[0], i[1], z]) for i in inner_points]
            outer_points = [np.array([i[0], i[1], z]) for i in outer_points]

        # Select relevant intersection points
        if inner_points:
            if len(inner_points) <= 1 or (len(inner_points) > 1 and np.linalg.norm(inner_points[1]-obj_pos) > np.linalg.norm(inner_points[0]-obj_pos)):
                point0 = inner_points[0]
            else:
                point0 = inner_points[1]

            if np.linalg.norm(outer_points[1]-obj_pos) > np.linalg.norm(outer_points[0]-obj_pos):
                point1 = outer_points[0]
            else:
                point1 = outer_points[1]
        else:
            point0 = outer_points[0]
            point1 = outer_points[1]
        
        # Pick a random orientation for the vector
        if np.random.choice([0, 1]):
            start_vec = point0-obj_pos
            end_vec = point1-obj_pos

        else:
            start_vec = point1-obj_pos
            end_vec = point0-obj_pos

        start_vec /= np.linalg.norm(start_vec)
        start_vec *= start_distance + obj_width
        start_point = obj_pos + start_vec

        end_vec *= np.random.random()
        end_point = obj_pos + end_vec

        # Display the path in the rai simulation
        if ry_config:
            plotLine(ry_config, np.array([point0[0], point0[1], .651]), np.array([point1[0], point1[1], .651]))
            
            way0 = ry_config.getFrame('start_point')
            way0.setPosition(point0)
            way1 = ry_config.getFrame('end_point')
            way1.setPosition(point1)

        return start_point, end_point, point0, point1, True
