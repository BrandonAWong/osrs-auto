from platform import system
from pyscreeze import Box
from pyautogui import ImageNotFoundException

if system() == "Windows":
    from pyautogui import locateOnScreen as find, click, press
else:
    from locate_linux import find
    from inputs_linux import click, press


def open_inventory() -> None:
    """ If inventory is not open, then open it """
    try:
        find("./images/empty_inventory.png", confidence=0.5)
    except ImageNotFoundException:
        press("esc")
