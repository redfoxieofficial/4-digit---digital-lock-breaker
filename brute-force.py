import time
import random
from pynput import keyboard
from pynput.keyboard import Controller as ControllerKeyboard
from pynput.mouse import Button, Controller

keyboard = ControllerKeyboard()
time.sleep(0)
keyboard.press("e")
time.sleep(0.3)
keyboard.release("e")
sayac = 0

while sayac <= 4:

    time.sleep(0.1)
    n1 = [131, 114]
    n2 = [207, 116]
    n3 = [282, 109]
    n4 = [125, 174]
    n5 = [232, 176]
    n6 = [290, 181]
    n7 = [131, 237]
    n8 = [202, 241]
    n9 = [272, 246]
    n0 = [220, 304]

    randomsec = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n0]
    enter = [368, 253]
    mouse = Controller()
    position = mouse.position

    x = random.choice(randomsec)

    mouse.position = (x)
    mouse.press(Button.left)
    mouse.release(Button.left)
    time.sleep(0.25)
    print(x)
    sayac += 1
    if sayac == 4:
        mouse.position = (enter)
        mouse.press(Button.left)
        time.sleep(0.1)
        mouse.release(Button.left)
        time.sleep(0.1)
        keyboard = ControllerKeyboard()
        time.sleep(0)
        keyboard.press("e")
        time.sleep(0.5)
        keyboard.release("e")
        print("---------------")
        sayac = 0
