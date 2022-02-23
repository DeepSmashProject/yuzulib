from enum import Enum
from yuzulib.enums import Button
class Action:
    """A single button on a PRO controller"""
    ACTION_JAB = {"name": "ACTION_JAB", "buttons": [Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_TILT = {"name": "ACTION_RIGHT_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_TILT = {"name": "ACTION_LEFT_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_TILT = {"name": "ACTION_UP_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_UP, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_DOWN_TILT = {"name": "ACTION_DOWN_TILT", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_DOWN, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_SMASH = {"name": "ACTION_RIGHT_SMASH", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_SMASH = {"name": "ACTION_LEFT_SMASH", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_SMASH = {"name": "ACTION_UP_SMASH", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_DOWN_SMASH = {"name": "ACTION_DOWN_SMASH", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_A], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_NEUTRAL_SPECIAL = {"name": "ACTION_NEUTRAL_SPECIAL", "buttons": [Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_SPECIAL = {"name": "ACTION_RIGHT_SPECIAL", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_SPECIAL = {"name": "ACTION_LEFT_SPECIAL", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_SPECIAL = {"name": "ACTION_UP_SPECIAL", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_RIGHT_SPECIAL = {"name": "ACTION_UP_RIGHT_SPECIAL", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_S_RIGHT, Button.BUTTON_B], "hold": False, "sec": 0.03, "wait": 0.05, "refresh": False}
    ACTION_UP_LEFT_SPECIAL = {"name": "ACTION_UP_LEFT_SPECIAL", "buttons": [Button.BUTTON_S_UP, Button.BUTTON_S_LEFT, Button.BUTTON_B], "hold": False, "sec": 0.03, "wait": 0.05, "refresh": False}
    ACTION_DOWN_SPECIAL = {"name": "ACTION_DOWN_SPECIAL", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_B], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_GRAB = {"name": "ACTION_GRAB", "buttons": [Button.BUTTON_R], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_SHIELD = {"name": "ACTION_SHIELD", "buttons": [Button.BUTTON_ZR], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_JUMP = {"name": "ACTION_JUMP", "buttons": [Button.BUTTON_Y], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_RIGHT_JUMP = {"name": "ACTION_RIGHT_JUMP", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_Y], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_LEFT_JUMP = {"name": "ACTION_LEFT_JUMP", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_Y], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_SHORT_HOP = {"name": "ACTION_SHORT_HOP", "buttons": [Button.BUTTON_Y, Button.BUTTON_X], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_RIGHT_SHORT_HOP = {"name": "ACTION_RIGHT_SHORT_HOP", "buttons": [Button.BUTTON_S_RIGHT, Button.BUTTON_Y, Button.BUTTON_X], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_LEFT_SHORT_HOP = {"name": "ACTION_LEFT_SHORT_HOP", "buttons": [Button.BUTTON_S_LEFT, Button.BUTTON_Y, Button.BUTTON_X], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": True}
    ACTION_UP_TAUNT = {"name": "ACTION_UP_TAUNT", "buttons": [Button.BUTTON_D_UP], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_DOWN_TAUNT = {"name": "ACTION_DOWN_TAUNT", "buttons": [Button.BUTTON_D_DOWN], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_TAUNT = {"name": "ACTION_LEFT_TAUNT", "buttons": [Button.BUTTON_D_LEFT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_TAUNT = {"name": "ACTION_RIGHT_TAUNT", "buttons": [Button.BUTTON_D_RIGHT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_SPOT_DODGE = {"name": "ACTION_SPOT_DODGE", "buttons": [Button.BUTTON_ZR, Button.BUTTON_S_DOWN], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_ROLL = {"name": "ACTION_RIGHT_ROLL", "buttons": [Button.BUTTON_ZR, Button.BUTTON_S_RIGHT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_ROLL = {"name": "ACTION_LEFT_ROLL", "buttons": [Button.BUTTON_ZR, Button.BUTTON_S_LEFT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_DASH = {"name": "ACTION_RIGHT_DASH", "buttons": [Button.BUTTON_S_RIGHT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_DASH = {"name": "ACTION_LEFT_DASH", "buttons": [Button.BUTTON_S_LEFT], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_WALK = {"name": "ACTION_RIGHT_WALK", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_WALK = {"name": "ACTION_LEFT_WALK", "buttons": [Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_CROUCH = {"name": "ACTION_CROUCH", "buttons": [Button.BUTTON_S_DOWN], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_CRAWL = {"name": "ACTION_RIGHT_CRAWL", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_MODIFIER, Button.BUTTON_S_RIGHT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_CRAWL = {"name": "ACTION_LEFT_CRAWL", "buttons": [Button.BUTTON_S_DOWN, Button.BUTTON_MODIFIER, Button.BUTTON_S_LEFT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_RIGHT_STICK = {"name": "ACTION_RIGHT_STICK", "buttons": [Button.BUTTON_S_RIGHT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_LEFT_STICK = {"name": "ACTION_LEFT_STICK", "buttons": [Button.BUTTON_S_LEFT], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_UP_STICK = {"name": "ACTION_UP_STICK", "buttons": [Button.BUTTON_S_UP], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_DOWN_STICK = {"name": "ACTION_DOWN_STICK", "buttons": [Button.BUTTON_S_DOWN], "hold": True, "sec": 0.02, "wait": 0.05, "refresh": False}
    ACTION_NO_OPERATION = {"name": "ACTION_NO_OPERATION", "buttons": [], "hold": False, "sec": 0.02, "wait": 0.05, "refresh": False}
    
class Stage(Enum):
    STAGE_BATTLE_FIELD=1
    STAGE_FINAL_DESTINATION=4
    STAGE_POKEMON_STADIUM2=41
    STAGE_SMASH_VILLE=45
    STAGE_HANENBOW=55
    STAGE_TOWN_AND_CITY=86

class Fighter(Enum):
    FIGHTER_MARIO=0
    FIGHTER_DONKEY_KONG=1
    FIGHTER_LINK=2
    FIGHTER_SAMUS=3
    FIGHTER_YOSHI=4
    FIGHTER_KIRBY=5
    FIGHTER_FOX=6
