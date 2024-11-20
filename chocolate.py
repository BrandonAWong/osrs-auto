from threading import current_thread

from platform import system
from pyscreeze import Box
from pyautogui import ImageNotFoundException, easeInQuad, easeOutQuad, easeInOutQuad, easeInBounce, easeInElastic

from random import randint, uniform, choice
from time import sleep

from game_actions import focus_game, open_inventory
from random_cords import get_random_cords

if system() == "Windows":
    from pyautogui import locateOnScreen as find, click, press, moveTo
else:
    from locate_linux import find
    from inputs_linux import click, press, moveTo


def auto_chocolate(banker_loc: tuple[int, int]):
    """ Automation of chocolate processing """
    # Acts as a way to also focus the game
    get_banked_chocolate(banker_loc)
    sleep(uniform(0.25, 1))
    open_inventory()
    sleep(uniform(0.25, 1))
    
    try:
        knife_loc: Box = find("./images/knife.png", confidence=0.5)
        choco_loc: Box = find("./images/chocolate_bar.png", confidence=0.8)
        while True:
            process_chocolate(knife_loc, choco_loc)
            for _ in range(randint(48, 50)):
                if current_thread().stopped:
                    return
                sleep(uniform(1, 1.2))
            get_banked_chocolate(banker_loc, choco_loc)
    except ImageNotFoundException:
        return

def get_banked_chocolate(banker_loc: tuple[int, int], choco_loc: Box=None) -> None:
    moveTo(banker_loc[0] + randint(-5, 5), banker_loc[1] + randint(-5, 5), randint(1, 2), get_random_ease())
    sleep(uniform(0.5, 1.2))
    click()
    sleep(uniform(0.5, 1.2))

    # deposit
    if choco_loc is not None:
        moveTo(*get_random_cords(choco_loc), randint(1, 2))
        sleep(uniform(0.5, 1.2))
        click()

    moveTo(*get_random_cords(find("./images/chocolate_bar.png", confidence=0.8)), randint(1, 3), get_random_ease())
    sleep(uniform(0.5, 1.2))
    click()
    sleep(uniform(0.3, 1))
    press("esc")

def process_chocolate(knife_loc: Box, choco_loc: Box) -> None:
    moveTo(*get_random_cords(knife_loc), randint(1, 3), get_random_ease())
    sleep(uniform(0.5, 1.2))
    click()
    moveTo(*get_random_cords(choco_loc), randint(1, 3), get_random_ease())
    sleep(uniform(0.5, 1.2))
    click()

def check_chocolate_exists() -> bool:
    try:
        find("./images/chocolate_bar.png", confidence=0.8)
        return True
    except ImageNotFoundException:
        return False

def get_random_ease():
    return choice((easeInQuad, easeOutQuad, easeInOutQuad, easeInBounce, easeInElastic))