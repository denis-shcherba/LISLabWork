import numpy as np

def line_circle_intersection(line_pos, line_vec, circle_pos, circle_radious):

    a = line_vec[0]**2 + line_vec[1]**2
    b = 2*(line_vec[0]*line_pos[0] + line_vec[1]*line_pos[1] - line_vec[0]*circle_pos[0] - line_vec[1]*circle_pos[1])
    c = circle_pos[0]**2 + circle_pos[1]**2 - 2*line_pos[0]*circle_pos[0] - 2*line_pos[1]*circle_pos[1] - circle_radious**2 + line_pos[0]**2 + line_pos[1]**2

    tmp = b**2-4*a*c

    if tmp < 0:
        return []
    if tmp == 0:
        t = -b/(2*a)
        return [np.array([line_vec[0]*t+line_pos[0], line_vec[1]*t+line_pos[1]])]

    t = (-b+np.sqrt(tmp))/(2*a)
    result = [np.array([line_vec[0]*t+line_pos[0], line_vec[1]*t+line_pos[1]])]
    t = (-b-np.sqrt(tmp))/(2*a)
    result.append(np.array([line_vec[0]*t+line_pos[0], line_vec[1]*t+line_pos[1]]))
    return result