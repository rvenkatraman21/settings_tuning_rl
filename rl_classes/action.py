import numpy as np
import random
import config


class Action:
    dispatch_settings: float
    pay_settings: float
    eta_settings: float

    def __init__(self, dispatch_settings, pay_settings, eta_settings):
        self.dispatch_settings = dispatch_settings
        self.pay_settings = pay_settings
        self.eta_settings = eta_settings

    def get_new_action_dispatch(self, reference_setting: float, if_randomize: bool):# -> Action
        if if_randomize:
            new_setting = random.random() * (
                    config.ACTION_MAX_DISPATCH_SETTING - config.ACTION_MIN_DISPATCH_SETTING) + config.ACTION_MIN_DISPATCH_SETTING
            new_setting = round(
                config.DISPATCH_SETTING_STEP_SIZE * np.floor(round(new_setting / config.DISPATCH_SETTING_STEP_SIZE, 2)),
                1)
            return Action(new_setting, self.pay_settings, self.eta_settings)
        else:
            new_setting = (self.dispatch_settings + reference_setting) / 2
            new_setting = round(
                config.DISPATCH_SETTING_STEP_SIZE * np.floor(round(new_setting / config.DISPATCH_SETTING_STEP_SIZE, 2)),
                1)

            return Action(new_setting,
                          self.pay_settings,
                          self.eta_settings
                          )

    def get_new_action_pay(self, reference_setting: float, if_randomize: bool): # -> Action:
        if if_randomize:
            new_setting = random.random() * (config.ACTION_MAX_PAY_SETTING - config.ACTION_MIN_PAY_SETTING) + config.ACTION_MIN_PAY_SETTING
            new_setting = round(
                config.PAY_SETTING_STEP_SIZE * np.floor(round(new_setting / config.PAY_SETTING_STEP_SIZE, 2)), 1)
            return Action(self.dispatch_settings, new_setting, self.eta_settings)
        else:
            new_setting = (self.pay_settings+ reference_setting)/2
            new_setting = round(
                config.PAY_SETTING_STEP_SIZE * np.floor(round(new_setting / config.PAY_SETTING_STEP_SIZE, 2)), 1)
            return Action(self.dispatch_settings,
                           new_setting,
                          self.eta_settings
                          )

    def get_new_action_eta(self, reference_setting: float, if_randomize: bool): # -> Action:
        if if_randomize:
            new_setting = random.random() * (config.ACTION_MAX_ETA_SETTING - config.ACTION_MIN_ETA_SETTING) + config.ACTION_MIN_ETA_SETTING
            new_setting = round(
                config.ETA_SETTING_STEP_SIZE * np.floor(round(new_setting / config.ETA_SETTING_STEP_SIZE, 2)), 1)
            return Action(self.dispatch_settings, self.pay_settings, new_setting)
        else:
            new_setting = (self.eta_settings + reference_setting)/2
            new_setting = round(
                config.ETA_SETTING_STEP_SIZE * np.floor(round(new_setting / config.ETA_SETTING_STEP_SIZE, 2)), 1)
            return Action(self.dispatch_settings,
                          self.pay_settings,
                          new_setting
                          )
