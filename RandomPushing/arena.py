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
    def __init__(self, C, middleP, width, height):
        super().__init__(C, middleP, width, height)

    def area(self):
        return self.width * self.height
    

    #TODO Implement plotArena for rectArena
    def plotArena(self, middleP, height, width, innerR, C, resolution=48):
        '''
        Visualises the pushing area.
        Returns:
            None: Adds visualization frames representing red spheres for the inner and outer area.
        '''
        step_size = (2*height+2*width)/resolution
        for i in range(resolution):
            angle = step_size*i
            dir_vec = np.array([np.cos(angle), np.sin(angle), 0])
            #outer_point = middleP + outerR*dir_vec

            if innerR:
                inner_point = middleP + innerR*dir_vec
                C.addFrame(f'inner_arena_{i}') \
                    .setPosition(inner_point) \
                    .setShape(ry.ST.sphere, size=[.02]) \
                    .setColor([1, 0, 0])
            
            #C.addFrame(f'outer_arena_{i}') \
               # .setPosition(outer_point) \
                #.setShape(ry.ST.sphere, size=[.02]) \
                #.setColor([1, 0, 0])#