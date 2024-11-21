from random import randint
from pyscreeze import Box

def get_random_cords(box: Box) -> tuple[int, int]:
    return (randint(int(box.left) + 5, int(box.left) + box.width - 5),
           randint(int(box.top) + 3, int(box.top) + box.height - 3)) 
