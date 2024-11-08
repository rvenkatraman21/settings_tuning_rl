from typing import List

from .action import Action
from .reward import Reward, RewardFunction
from .state import ActualState, State

class Step:
    time_period: int
    actual_state: ActualState
    reward_function: RewardFunction
    state: State
    action: Action
    reward: Reward

    def __init__(self, time_period, actual_state, state, reward_function):
        self.time_period = time_period
        self.actual_state = actual_state
        self.state = state
        self.reward_function = reward_function

    def set_action(self, action: Action) -> None:
        self.action = action

    def set_reward(self) -> None:
        self.reward = self.reward_function.get_reward_from_action(self.state, self.action)

class Episode:
    steps: List[Step]
    total_reward: float
    total_fulfillment_cost: float
    total_late_deliveries: float
    total_converted_deliveries: float
    net_reward: Reward

    def __init__(self, steps: List[Step]):
        self.steps = steps

    @classmethod
    def initialize(cls, actual_states: List[ActualState]): #-> Episode
        states: List[State] = []
        for actual_state in actual_states:
            states.append(State(actual_state))

        reward_function = RewardFunction.initialize(states)

        steps: List[Step] = []
        for i in range(len(actual_states)):
            step = Step(i, actual_states[i], states[i], reward_function)
            steps.append(step)

        return cls(steps)

    def compute_total_reward(self) -> None:
        self.total_reward = 0.0
        self.total_fulfillment_cost = 0.0
        self.total_late_deliveries = 0.0
        self.total_converted_deliveries = 0.0
        total_deliveries = 0.0

        for step in self.steps:
            self.total_reward += step.reward.get_net_reward(step.actual_state.num_deliveries)
            self.total_fulfillment_cost += step.reward.fulfillment_cost * step.actual_state.num_deliveries
            self.total_late_deliveries += (step.reward.late_pct/100) * step.actual_state.num_deliveries
            self.total_converted_deliveries += (1 + step.reward.conversion_rate_change/100) * step.actual_state.num_deliveries
            total_deliveries += step.actual_state.num_deliveries

            fulfillment_cost_per_delivery = self.total_fulfillment_cost/total_deliveries
            late_pct = (self.total_late_deliveries/total_deliveries)*100
            conversion_rate_change = (self.total_converted_deliveries/total_deliveries - 1.0)*100
            self.net_reward = Reward(fulfillment_cost_per_delivery, late_pct, conversion_rate_change)





