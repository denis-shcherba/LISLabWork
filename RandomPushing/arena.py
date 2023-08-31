import numpy as np
from robotic import ry

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


class RectangularArena(Arena):
    def __init__(self, C, middleP, width, height, innerR=None):
        super().__init__(C, middleP, width, height)
        self.innerR = innerR
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


        for i in range(resolution):
            angle = step_size * i
            dir_vec_circ = np.array([np.cos(angle), np.sin(angle), 0])
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
                inner_point = self.middleP + self.innerR * dir_vec_circ
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



"""
def plotArena(self, middleP, height, width, innerR, C, resolution=48):
        '''
        Visualises the pushing area.
        Returns:
            None: Adds visualization frames representing red spheres for the inner and outer area.
        '''
        step_size = (2*height+2*width)/resolution
        for i in range(resolution):
            angle = step_size*i
            #outer_point = middleP + outerR*dir_vec

            if innerR:
    
                dir_vec_circ = np.array([np.cos(angle), np.sin(angle), 0])

                inner_point = middleP + innerR*dir_vec_circ
                C.addFrame(f'inner_arena_{i}') \
                    .setPosition(inner_point) \
                    .setShape(ry.ST.sphere, size=[.02]) \
                    .setColor([1, 0, 0])
            
            C.addFrame(f'outer_arena_{i}') \
                .setPosition(outer_point) \
                .setShape(ry.ST.sphere, size=[.02]) \
                .setColor([1, 0, 0])#
"""
