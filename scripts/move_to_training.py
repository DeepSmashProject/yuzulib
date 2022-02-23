from yuzulib.game.ssbu import UltimateController, Stage, Fighter

controller = UltimateController()

config = {
    "stage": Stage.STAGE_HANENBOW, 
    "player": {"fighter": Fighter.FIGHTER_MARIO, "color": 0}, 
    "cpu": {"fighter": Fighter.FIGHTER_DONKEY_KONG, "color": 0, "level": 9},
    "setting": {"quick_mode": True, "cpu_behavior": "cpu", "diable_combo_display": True}
}
controller.mode.training.start(config)
