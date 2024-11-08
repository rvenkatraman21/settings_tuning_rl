import numpy as np
from typing import Dict, Tuple

from .action import Action
import config


class ActualState:
    num_deliveries: int
    num_couriers: int
    # the following metrics are for the average of the past _n_ states
    avg_eta_error_minutes: float
    avg_engaged_minutes: float

    def __init__(self, num_deliveries, num_couriers, avg_eta_error_minutes, avg_engaged_time_minutes):
        self.num_deliveries = int(num_deliveries)
        self.num_couriers = int(num_couriers)
        self.avg_eta_error_minutes = float(avg_eta_error_minutes)
        self.avg_engaged_minutes = float(avg_engaged_time_minutes)

    @classmethod
    def from_csv(cls, row):
        return cls(row[3], row[4], row[5], row[6])

    def __add__(self, other):
        return ActualState(self.num_deliveries + other.num_deliveries, self.num_couriers + other.num_couriers, self.avg_eta_error_minutes + other.avg_eta_error_minutes, self.avg_engaged_minutes + other.avg_engaged_minutes)

    def get_state_from_normal(self, stdev: float):
        nd = np.random.normal(self.num_deliveries, stdev, 1)[0]
        nc = np.random.normal(self.num_couriers, stdev, 1)[0]
        eta_error = np.random.normal(self.avg_eta_error_minutes, stdev, 1)[0]
        engaged_minutes = np.random.normal(self.avg_eta_error_minutes, stdev, 1)[0]
        return ActualState(nd, nc, eta_error, engaged_minutes)


class State:
    num_deliveries: int
    num_couriers: int
    # the following metrics are for the average of the past _n_ states
    avg_eta_error_minutes: int
    avg_engaged_minutes: int

    def __init__(self, actual_state: ActualState):

        for idx, value in enumerate(config.STATE_DELIVERIES_CATEGORIES):
            if actual_state.num_deliveries > value:
                self.num_deliveries=idx+1
            else:
                break

        for idx, value in enumerate(config.STATE_COURIERS_CATEGORIES):
            if actual_state.num_couriers > value:
                self.num_couriers=idx+1
            else:
                break

        for idx, value in enumerate(config.STATE_ETA_ERROR_CATEGORIES):
            if actual_state.avg_eta_error_minutes > value:
                self.avg_eta_error_minutes=idx+1
            else:
                break

        for idx, value in enumerate(config.STATE_ENGAGED_TIME_CATEGORIES):
            if actual_state.avg_engaged_minutes > value:
                self.avg_engaged_minutes=idx+1
            else:
                break


class StateTransition:
    state_transition_dispatch: Dict[Tuple[State, float], State]
    state_transition_pay: Dict[Tuple[State, float], State]
    state_transition_eta: Dict[Tuple[State, float], State]

    stdev_dispatch: float
    stdev_pay: float
    stdev_eta: float

    def __init__(self):
        self.state_transition_dispatch = {}
        self.state_transition_pay = {}
        self.state_transition_eta = {}
        self.stdev_dispatch = 0.0
        self.stdev_pay = 0.0
        self.stdev_eta = 0.0

    @classmethod
    def initialize_state_transition_functions(cls): # -> StateTransition
        pass

    def update_next_state(self, current_action: Action, next_state_initial: State) -> State:
        pass