from robotic import ry

from config import setup_config, startup_robot
from bird_search import flyToPoint, getBirdView

if __name__ == "__main__":
    ry.params_print()
    C = setup_config()

    bot = startup_robot(C)
    obj_pos = C.getFrame("obj").getPosition()

    while True:
        flyToPoint([obj_pos[0], obj_pos[1]], C, bot)
        cx, cy, dist = getBirdView(bot)
        if dist < 20: break
