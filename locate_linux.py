from datetime import datetime
from pyautogui import locate
from pyscreeze import Box
from subprocess import run

def find(path: str, confidence: float=1) -> Box:
    """ Locate given image """
    screenshot_path = f"/tmp/osrs{datetime.now().strftime("%Y%m%d")}.png"
    run([f"grim {screenshot_path}"], shell=True)
    return locate(path, screenshot_path, confidence=confidence)

