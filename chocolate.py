from game_actions import open_inventory

from platform import system
from pyscreeze import Box
from pyautogui import ImageNotFoundException

if system() == "Windows":
    from pyautogui import locateOnScreen as find, click, press
else:
    from locate_linux import find
    from inputs_linux import click, press


def auto_chocolate():
    open_inventory()
    

auto_chocolate() 
