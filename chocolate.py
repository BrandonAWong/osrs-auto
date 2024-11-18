from threading import current_thread

from platform import system
from pyscreeze import Box
from pyautogui import ImageNotFoundException

from random import randint, uniform
from time import sleep

from game_actions import focus_game, open_inventory
from random_cords import get_random_cords

if system() == "Windows":
    from pyautogui import locateOnScreen as find, click, press, moveTo
else:
    from locate_linux import find
    from inputs_linux import click, press, moveTo


def auto_chocolate():
    # find banker
    open_inventory()
    sleep(uniform(0.25, 1))

    try:
        moveTo(*get_random_cords(find("./images/knife.png", confidence=0.5)))
        click(clicks=1)
        moveTo(*get_random_cords(find("./images/chocolate_bar.png", confidence=0.8)))
        click(clicks=1)
        for _ in range(randint(48, 50)):
            if current_thread().stopped:
                return
            sleep(uniform(1, 1.2))
    except ImageNotFoundException:
        return

