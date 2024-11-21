from platform import system
from pyscreeze import Box
from pyautogui import ImageNotFoundException

from random_cords import get_random_cords

if system() == "Windows":
    from pyautogui import locateOnScreen as find, click, press, moveTo
else:
    from linux.locate_linux import find
    from linux.inputs_linux import click, press, moveTo


def focus_game() -> bool:
    """
    If game is on screen, click on it to put it into focus.
    If game was focussed return True, otherwise False.
    """
    checks: tuple[str, ...] = ("all_chat", "all_chat_inactive", "attack_menu")
    for check in checks:
        try:
            moveTo(*get_random_cords(find(f"./static/{check}.png", confidence=0.6)))
            click(clicks=1)
            return True
        except ImageNotFoundException:
            continue
    return False

def open_inventory() -> None:
    """ If inventory is not open, then open it """
    try:
        find("./static/empty_inventory.png", confidence=0.5)
    except ImageNotFoundException:
        press("esc")

