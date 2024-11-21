from datetime import datetime

from pyautogui import locate, locateAll
from pyscreeze import Box

from subprocess import run

from typing import Generator

def find(path: str, confidence: float=1) -> Box:
    """ Locate given image """
    screenshot_path = f"/tmp/osrs{datetime.now().strftime("%Y%m%d")}.png"
    run([f"grim -o eDP-1 {screenshot_path}"], shell=True)
    return locate(path, screenshot_path, confidence=confidence)

def find_all(path: str, confidence: float=1) -> Generator:
    """ Locate all instances of a given image """
    screenshot_path = f"/tmp/osrs{datetime.now().strftime("%Y%m%d")}.png"
    run([f"grim -o eDP-1 {screenshot_path}"], shell=True)
    return locateAll(path, screenshot_path, confidence=confidence)