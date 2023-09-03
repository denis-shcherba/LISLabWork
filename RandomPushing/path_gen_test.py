import pygame
import sys
import numpy as np
from time import sleep
from random_paths import generate_waypointsv2, generate_waypoints_rect

ARENA_TYPE="RECTANGLE"

INNER_CIRCLE = True
# Initialize Pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Path generation test")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
salmon = (255, 128, 0)
magenta = (255, 0, 255)

screen.fill(white)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #screen.fill(white)
    sleep(.2)
    robot_pos = np.array([screen_width*.5, screen_height*.5])
    obj_pos = robot_pos+np.array([screen_width*.1, screen_height*.1])
    
    if ARENA_TYPE=="CIRCLE":
        inner_rad=50
        outer_rad=250

        start, end, intersect0, intersect1, _ = generate_waypointsv2(None, obj_pos, 5, robot_pos=robot_pos, inner_rad=inner_rad, outer_rad=outer_rad, start_distance=20)
        
        # Draw stuff
        pygame.draw.circle(screen, black, (robot_pos[0], robot_pos[1]), inner_rad, 2)
        pygame.draw.circle(screen, black, (robot_pos[0], robot_pos[1]), outer_rad, 2)
        pygame.draw.circle(screen, red, (obj_pos[0], obj_pos[1]), 7)

        pygame.draw.circle(screen, green, (intersect0[0], intersect0[1]), 7)
        pygame.draw.circle(screen, green, (intersect1[0], intersect1[1]), 7)

        pygame.draw.circle(screen, salmon, (start[0], start[1]), 7)
        pygame.draw.circle(screen, magenta, (end[0], end[1]), 7)
        
        pygame.draw.line(screen, blue, (intersect0[0], intersect0[1]), (intersect1[0], intersect1[1]), 2)

    elif ARENA_TYPE=="RECTANGLE":
        rect_width = 500
        rect_height = 350
        rect_x = robot_pos[0]-1/2*rect_width
        rect_y = robot_pos[1]-1/2*rect_height #minus nach oben lang in y lul



        # Draw stuff
        if INNER_CIRCLE:
            inner_rad=50
            pygame.draw.circle(screen, black, (robot_pos[0], robot_pos[1]), inner_rad, 2)
            start, end, intersect0, intersect1, _ = generate_waypoints_rect(None, obj_pos, 5, robot_pos=robot_pos, rect_width=rect_width, rect_height=rect_height, start_distance=20, inner_rad=inner_rad)
        else:
            start, end, intersect0, intersect1, _ = generate_waypoints_rect(None, obj_pos, 5, robot_pos=robot_pos, rect_width=rect_width, rect_height=rect_height, start_distance=20)

        
        pygame.draw.circle(screen, red, (obj_pos[0], obj_pos[1]), 7)

        #pygame.draw.circle(screen, (0, 255, 0), (intersect0[0], intersect0[1]), 7)
        #pygame.draw.circle(screen, (0, 255, 0), (intersect1[0], intersect1[1]), 7)
        outline_rect = pygame.Rect(rect_x, rect_y, rect_width, rect_height)
        pygame.draw.rect(screen, black,  outline_rect, 2)    
        pygame.draw.line(screen, blue, (intersect0[0], intersect0[1]), (intersect1[0], intersect1[1]), 2)

    # Update the display
    pygame.display.flip()
    
# Quit Pygame
pygame.quit()
sys.exit()
