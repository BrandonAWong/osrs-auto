from threading import current_thread
from platform import system

from pyscreeze import Box
from pyautogui import ImageNotFoundException, easeInQuad, easeOutQuad, easeInOutQuad, easeInBounce

from random import randint, uniform, choice
from time import sleep

from GameActions.basic_actions import open_inventory
from random_cords import get_random_cords

if system() == "Windows":
    from pyautogui import locateOnScreen as find, locateAllOnScreen as find_all, click, press, moveTo
else:
    from linux.locate_linux import find, find_all
    from linux.inputs_linux import click, press, moveTo
    

def auto_chocolate(banker_loc: tuple[int, int], speed="slow"):
    """ Automation of chocolate processing """
    try:
        # Acts as a way to also focus the game
        get_banked_chocolate(banker_loc)
        sleep(uniform(0.25, 1))
        open_inventory()
        sleep(uniform(0.25, 1))
        
        speed = speed.lower()
        knife_loc: Box = find("./static/knife.png", confidence=0.5)
        choco_loc: Box = tuple(find_all("./static/chocolate_bar.png", confidence=0.8))[-1]
        while not current_thread().stopped:
            if speed == "slow" or speed == "random" and choice(("slow", "fast")) == "slow":
                process_chocolate_slow(knife_loc, choco_loc)
            else:
                process_chocolate_fast(knife_loc, choco_loc)

            if current_thread().stopped:
                return
            
            get_banked_chocolate(banker_loc, choco_loc)
    except ImageNotFoundException:
        return

def get_banked_chocolate(banker_loc: tuple[int, int], inven_loc: Box=None) -> None:
    moveTo(banker_loc[0] + randint(-5, 5), banker_loc[1] + randint(-5, 5), randint(1, 2), get_random_ease())
    sleep(uniform(0.5, 1.2))
    click()
    sleep(uniform(0.5, 1.2))

    # deposit
    if inven_loc is not None:
        moveTo(*get_random_cords(inven_loc), uniform(1, 2))
        sleep(uniform(0.5, 1.2))
        click()

    moveTo(*get_random_cords(find("./static/chocolate_bar.png", confidence=0.8)), uniform(1, 3), get_random_ease())
    sleep(uniform(0.5, 1.2))
    click()
    sleep(uniform(0.3, 1))
    press("esc")

def process_chocolate_slow(knife_loc: Box, choco_loc: Box):
    process_chocolate(knife_loc, choco_loc)
    for _ in range(randint(48, 50)):
        if current_thread().stopped:
            return
        sleep(uniform(1, 1.2))

def process_chocolate_fast(knife_loc: Box, choco_loc: Box):
    for _ in range(randint(15, 17)):
        if current_thread().stopped:
            return
        process_chocolate(knife_loc, choco_loc)
        sleep(uniform(0.1, 0.3))

def process_chocolate(knife_loc: Box, choco_loc: Box) -> None:
    moveTo(*get_random_cords(knife_loc), uniform(0.2,1), get_random_ease())
    sleep(uniform(0.1, 0.5))
    click()
    moveTo(*get_random_cords(choco_loc), uniform(0.2,1), get_random_ease())
    sleep(uniform(0.1, 0.3))
    click()

def check_chocolate_exists() -> bool:
    try:
        find("./static/chocolate_bar.png", confidence=0.8)
        return True
    except ImageNotFoundException:
        return False

def get_random_ease():
    return choice((easeInQuad, easeOutQuad, easeInOutQuad, easeInBounce))