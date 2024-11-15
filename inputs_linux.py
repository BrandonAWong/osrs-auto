from time import sleep
import uinput

def click(x: int, y: int) -> None:
    with uinput.Device([uinput.ABS_X, uinput.ABS_Y, uinput.BTN_LEFT]) as device:
        wait_for_device_ready()
        device.emit(uinput.ABS_X, x)
        device.emit(uinput.ABS_Y, y)
        device.emit_click(uinput.BTN_LEFT)
        device.syn()

def press(key: "str") -> None:
    ukey = getattr(uinput, f"KEY_{key.upper()}")
    with uinput.Device([ukey]) as device:
        wait_for_device_ready()
        device.emit_click(ukey)

def wait_for_device_ready() -> None:
    sleep(0.1)

