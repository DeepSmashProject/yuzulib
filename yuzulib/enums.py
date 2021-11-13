from enum import Enum
from pynput.keyboard import Key

class Button(Enum):
    """A single button on a PRO controller"""
    BUTTON_A = "c"
    BUTTON_B = "x"
    BUTTON_X = "v"
    BUTTON_Y = "z"
    BUTTON_ZL = "r"
    BUTTON_ZR = "t"
    BUTTON_L = "q"
    BUTTON_R = "e"
    BUTTON_PLUS = "m"
    BUTTON_MINUS = "n"
    BUTTON_D_UP = Key.up
    BUTTON_D_DOWN = Key.down
    BUTTON_D_LEFT = Key.left
    BUTTON_D_RIGHT = Key.right
    BUTTON_C_UP = "i"
    BUTTON_C_DOWN = "k"
    BUTTON_C_LEFT = "j"
    BUTTON_C_RIGHT = "l"
    BUTTON_S_UP = "w"
    BUTTON_S_DOWN = "s"
    BUTTON_S_LEFT = "a"
    BUTTON_S_RIGHT = "d"
    BUTTON_MODIFIER = Key.shift
