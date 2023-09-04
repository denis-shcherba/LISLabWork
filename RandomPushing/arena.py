import numpy as np
from robotic import ry
from quadratic_solver import line_circle_intersection, line_rect_intersection
from visual import plotLine
from random_paths import segment_line

class Arena:
    def __init__(self, C, middleP, width=None, height=None):
        self.C=C
        self.middleP= middleP
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


#circular Arena with inner and outer circle
class CircularArena(Arena):
    def __init__(self, C, middleP, outerR, innerR=None):
        super().__init__(C, middleP)
        self.outerR = outerR
        self.innerR = innerR

    def area(self):
        outer_area = np.pi * self.outerR ** 2
        if self.innerR:
            inner_area = np.pi * self.innerR ** 2
        return outer_area - inner_area
    def plotArena(self, resolution=48):
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
                self.C.addFrame(f'inner_arena_{i}') \
                    .setPosition(inner_point) \
                    .setShape(ry.ST.sphere, size=[.02]) \
                    .setColor([1, 0, 0])
            
            self.C.addFrame(f'outer_arena_{i}') \
                .setPosition(outer_point) \
                .setShape(ry.ST.sphere, size=[.02]) \
                .setColor([1, 0, 0])
    def generate_waypoints(self, C, obj_pos, obj_width, robot_pos=np.array([0, 0]), start_distance=.07, waypoints=None):

        success = False
        try:
            z = obj_pos[2]
        except:
            z = 0
        obj_pos = np.array((obj_pos[0], obj_pos[1]))
        robot_pos = np.array((robot_pos[0], robot_pos[1]))

        rob2obj_len = np.linalg.norm(obj_pos-robot_pos)
        
        if self.innerR:
            if rob2obj_len < self.innerR or rob2obj_len >= self.outerR:
                print("Object is outside of arena!")
                return None, None, None, None, success
        else:
            if rob2obj_len >= self.outerR:
                print("Object is outside of arena!")
                return None, None, None, None, success
        angle = np.random.random() * np.pi*2

        move_vec = np.array([np.cos(angle), np.sin(angle)])

        # obj_pos=posvector, move_vec= directions_vector, robot_pos = circle offset
        inner_points = line_circle_intersection(obj_pos, move_vec, robot_pos, self.innerR) if self.innerR else []
        outer_points = line_circle_intersection(obj_pos, move_vec, robot_pos, self.outerR)

        if inner_points:
            if np.linalg.norm(outer_points[1]-obj_pos) > np.linalg.norm(outer_points[0]-obj_pos):
                outer_inter = outer_points[0]
            else:
                outer_inter = outer_points[1]
            
            if len(inner_points) > 1:
                if np.linalg.norm(inner_points[1]-obj_pos) > np.linalg.norm(inner_points[0]-obj_pos):
                    point0 = inner_points[0]
                else:
                    point0 = inner_points[1]
            else:
                point0 = inner_points[0]
            point1 = outer_inter
        else:
            point0 = outer_points[0]
            point1 = outer_points[1]
        
        if C:
            plotLine(C, np.array([point0[0], point0[1], .651]), np.array([point1[0], point1[1], .651]))

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

        end3d = np.array([end_point[0], end_point[1], z])
        start3d = np.array([start_point[0], start_point[1], z])
        if C:
            if waypoints:
                points = segment_line(start3d, end3d, waypoints)
                for i, p in enumerate(points):
                    way = C.getFrame(f'way{i}')
                    way.setPosition(p)
            else:
                way0 = C.getFrame('start_point')
                # t: position relative to cylinder , d: degrees arm rotation, d:degrees gripper rotation
                way0.setPosition(point0)

                way1 = C.getFrame('end_point')
                way1.setPosition(point1)

        success = True
        return start3d, end3d, point0, point1, success       


class RectangularArena(Arena):
    def __init__(self, C, middleP, width, height, innerR=None, middlePCirc=None):
        super().__init__(C, middleP, width, height)
        self.innerR = innerR
        if middlePCirc:
            self.middlePCirc=middlePCirc
        else:
            self.middlePCirc = middleP
    def area(self):
        return self.width * self.height
    

    #TODO Implement plotArena for rectArena
    def plotArena(self, resolution=48):
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
                self.C.addFrame(f'inner_arena_{i}') \
                    .setPosition(inner_point) \
                    .setShape(ry.ST.sphere, size=[.02]) \
                    .setColor([1, 0, 0])

            dir_vec_rect = np.array([np.cos(angle), np.sin(angle), 0])  # Direction vector for rectangular arena
            #outer_point = self.middleP + np.array([self.width, self.height, 0]) * dir_vec_rect

            self.C.addFrame(f'outer_arena_{i}') \
                .setPosition(outer_point) \
                .setShape(ry.ST.sphere, size=[.02]) \
                .setColor([1, 0, 0])
    def generate_waypoints(self, C, obj_pos, obj_width, robot_pos=np.array([0, 0]), start_distance=.07, waypoints=None):

        success = False
        try:
            z = obj_pos[2]
        except:
            z = 0
        obj_pos = np.array((obj_pos[0], obj_pos[1]))
        robot_pos = np.array((robot_pos[0], robot_pos[1]))

        rob2obj_len = np.linalg.norm(obj_pos-robot_pos)
        
        if self.innerR:
            if rob2obj_len < self.innerR:
                print("Object is outside of arena!")
                return None, None, None, None, success
        else:
            if obj_pos[0] > robot_pos[0]+1/2*self.width or obj_pos[0] < robot_pos[0]-1/2*self.width or obj_pos[1] > robot_pos[1]+1/2*self.height or obj_pos[1] < robot_pos[1]-1/2*self.height:
                print("Object is outside of arena!")
                return None, None, None, None, success
        angle = np.random.random() * np.pi*2

        move_vec = np.array([np.cos(angle), np.sin(angle)])

        # obj_pos=posvector, move_vec= directions_vector, robot_pos = circle offset
        inner_points = line_circle_intersection(obj_pos, move_vec, robot_pos, self.innerR) if self.innerR else []
        outer_points = line_rect_intersection(obj_pos, move_vec, robot_pos, self.width, self.height)

        if inner_points:
            if np.linalg.norm(outer_points[1]-obj_pos) > np.linalg.norm(outer_points[0]-obj_pos):
                outer_inter = outer_points[0]
            else:
                outer_inter = outer_points[1]
            
            if len(inner_points) > 1:
                if np.linalg.norm(inner_points[1]-obj_pos) > np.linalg.norm(inner_points[0]-obj_pos):
                    point0 = inner_points[0]
                else:
                    point0 = inner_points[1]
            else:
                point0 = inner_points[0]
            point1 = outer_inter
        else:
            point0 = outer_points[0]
            point1 = outer_points[1]
        
        if C:
            plotLine(C, np.array([point0[0], point0[1], .651]), np.array([point1[0], point1[1], .651]))

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

        #blaue waypoints hier TODO
        end3d = np.array([end_point[0], end_point[1], z])
        start3d = np.array([start_point[0], start_point[1], z])
        if C:
            if waypoints:
                points = segment_line(start3d, end3d, waypoints)
                for i, p in enumerate(points):
                    way = C.getFrame(f'way{i}')
                    way.setPosition(p)
            else:
                way0 = C.getFrame('start_point')
                # t: position relative to cylinder , d: degrees arm rotation, d:degrees gripper rotation
                way0.setPosition(point0)

                way1 = C.getFrame('end_point')
                way1.setPosition(point1)

        success = True
        return start3d, end3d, point0, point1, success

