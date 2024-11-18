from random import randint, uniform 
from time import sleep
import uinput
from pyautogui import position

def click(clicks: int=1) -> None:
    with uinput.Device([uinput.BTN_LEFT]) as device:
        wait_for_device_ready()
        for _ in range(clicks):
            device.emit(uinput.BTN_LEFT, 1)

def moveTo(x: int, y: int) -> None:
    with uinput.Device([uinput.REL_X, uinput.REL_Y, uinput.BTN_MOUSE]) as device:
        wait_for_device_ready()
        count = 0
        while True:
            cur_x, cur_y = position()
            if cur_x == x and cur_y == y:
                break

            move_value = (count // 125) + 1
            move_x = move_value if cur_x < x else -move_value if cur_x > x else 0
            move_y = move_value if cur_y < y else -move_value if cur_y > y else 0 

            device.emit(uinput.REL_X, move_x)
            device.emit(uinput.REL_Y, move_y)

            count += 1 if count < 250 else -count
            sleep(uniform(0.001, 0.01))

def press(key: "str") -> None:
    ukey = getattr(uinput, f"KEY_{key.upper()}")
    with uinput.Device([ukey]) as device:
        wait_for_device_ready()
        device.emit_click(ukey)

def wait_for_device_ready() -> None:
    sleep(0.1)

