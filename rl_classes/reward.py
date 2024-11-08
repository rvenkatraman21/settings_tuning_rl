import numpy as np

import config
from .action import Action
from .state import State
from typing import Dict, List, Tuple



class Reward:
    fulfillment_cost: float
    late_pct: float
    conversion_rate_change: float

    def __init__(self, fulfillment_cost, late_pct, conversion_rate_change):
        self.fulfillment_cost = fulfillment_cost
        self.late_pct = late_pct
        self.conversion_rate_change = conversion_rate_change

    def __mul__(self, other):
        return Reward(self.fulfillment_cost * other, self.late_pct * other, self.conversion_rate_change * other)

    def __add__(self, other):
        return Reward(self.fulfillment_cost + other.fulfillment_cost, self.late_pct + other.late_pct, self.conversion_rate_change + other.conversion_rate_change)

    def get_reward_from_normal(self, stdev: List[float]):
        fc = np.random.normal(self.fulfillment_cost, stdev[0], 1)[0]
        lp = np.random.normal(self.late_pct, stdev[1], 1)[0]
        c = np.random.normal(self.conversion_rate_change, stdev[2], 1)[0]
        return Reward(fc, lp, c)

    def get_net_reward(self, num_deliveries: int) -> float:
        return ((1 + self.conversion_rate_change/100) * config.REWARD_WEIGHT_CONVERSION - (self.late_pct / 100) * config.REWARD_WEIGHT_LATE_PCT - self.fulfillment_cost) * num_deliveries


class RewardFunction:
    reward_function_dispatch: Dict[Tuple[State, float], Reward]
    reward_function_pay: Dict[Tuple[State, float], Reward]
    reward_function_eta: Dict[Tuple[State, float], Reward]

    stdev_dispatch: List[float]
    stdev_pay: List[float]
    stdev_eta: List[float]

    def __init__(self, reward_function_dispatch: Dict[Tuple[State, float], Reward], reward_function_pay: Dict[Tuple[State, float], Reward], reward_function_eta: Dict[Tuple[State, float], Reward], stdev_dispatch: List[float], stdev_pay: List[float], stdev_eta: List[float]):
        self.reward_function_dispatch = reward_function_dispatch
        self.reward_function_pay = reward_function_pay
        self.reward_function_eta = reward_function_eta
        self.stdev_dispatch = stdev_dispatch
        self.stdev_pay = stdev_pay
        self.stdev_eta = stdev_eta

    @classmethod
    def initialize(cls, states: List[State]): #-> RewardFunction

        reward_function_dispatch = {}
        setting = config.ACTION_MIN_DISPATCH_SETTING
        while setting <= config.ACTION_MAX_DISPATCH_SETTING:
            for state in states:
                fulfillment_cost = max(5,
                                       0.5 + 4 * state.num_deliveries - 2 * state.num_couriers - 0.35 * setting * setting - 0.8 * setting + 0.8 * state.avg_engaged_minutes)
                late_pct = 10 + state.num_deliveries - 0.7 * state.num_couriers + 2 * state.avg_eta_error_minutes + 0.75 * setting * setting + 0.55 * setting
                conversion_rate_change = 0

                reward_function_dispatch[(state, setting)] = Reward(fulfillment_cost, late_pct, conversion_rate_change)

            setting = round(setting + config.DISPATCH_SETTING_STEP_SIZE, 1)

        reward_function_pay = {}
        setting = config.ACTION_MIN_PAY_SETTING
        while setting <= config.ACTION_MAX_PAY_SETTING:
            for state in states:
                fulfillment_cost = setting
                late_pct = (state.num_deliveries - 0.7 * state.num_couriers) * setting
                conversion_rate_change = 0

                reward_function_pay[(state, setting)] = Reward(fulfillment_cost, late_pct, conversion_rate_change)

            setting += config.PAY_SETTING_STEP_SIZE

        reward_function_eta = {}
        setting = config.ACTION_MIN_ETA_SETTING
        while setting <= config.ACTION_MAX_ETA_SETTING:
            for state in states:
                fulfillment_cost = -1.0 * setting * 0.4
                late_pct = (state.num_deliveries - 0.6 * state.num_couriers) * setting * -1.0
                conversion_rate_change = -5 * setting

                reward_function_eta[(state, setting)] = Reward(fulfillment_cost, late_pct, conversion_rate_change)

            setting += config.ETA_SETTING_STEP_SIZE

        stdev_dispatch = [3, 3, 0]
        stdev_pay = [3, 3, 0]
        stdev_eta = [3, 3, 1.0]

        return cls(reward_function_dispatch, reward_function_pay, reward_function_eta, stdev_dispatch, stdev_pay, stdev_eta)


    def get_reward_from_action(self, state: State, action: Action) -> Reward:
        dispatch_setting = max(min(action.dispatch_settings, config.ACTION_MAX_DISPATCH_SETTING), config.ACTION_MIN_DISPATCH_SETTING)
        pay_setting = max(min(action.pay_settings, config.ACTION_MAX_PAY_SETTING), config.ACTION_MIN_PAY_SETTING)
        eta_setting = max(min(action.eta_settings, config.ACTION_MAX_ETA_SETTING), config.ACTION_MIN_ETA_SETTING)

        dispatch_setting_reward: Reward = self.reward_function_dispatch[(state, dispatch_setting)].get_reward_from_normal(self.stdev_dispatch)
        pay_setting_reward: Reward = self.reward_function_pay[(state, pay_setting)].get_reward_from_normal(self.stdev_pay)
        eta_setting_reward: Reward = self.reward_function_eta[(state, eta_setting)].get_reward_from_normal(self.stdev_eta)
        net_reward: Reward = dispatch_setting_reward + pay_setting_reward + eta_setting_reward
        return net_reward
