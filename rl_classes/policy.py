import statistics

from .action import Action
from .reward import Reward
from .state import State
from typing import Dict, List, Tuple

class PolicyAttributes:
    is_static: bool
    if_update: bool
    probability_update: float
    probability_anneal: float

    def __init__(self, is_static: bool, if_update: bool, probability_update: float, probability_anneal: float):
        self.is_static = is_static
        self.if_update = if_update
        self.probability_update = probability_update
        self.probability_anneal = probability_anneal


class PolicyReward:
    episode_total_rewards: List[float]
    episode_reward_objects: List[Reward]

    avg_reward: float
    median_reward: float

    avg_fulfillment_cost: float
    median_fulfillment_cost: float

    avg_late_pct: float
    median_late_pct: float

    avg_conversion_rate: float
    median_conversion_rate: float

    def __init__(self, episode_rewards: List[Tuple[float, Reward]]):
        self.episode_total_rewards = [total_reward for total_reward, _ in episode_rewards]
        self.episode_reward_objects = [reward_objects for _, reward_objects in episode_rewards]

    def compute_net_reward(self):
        self.avg_reward = statistics.mean(self.episode_total_rewards)
        self.median_reward = statistics.median(self.episode_total_rewards)

        self.avg_fulfillment_cost = statistics.mean([reward.fulfillment_cost for reward in self.episode_reward_objects])
        self.median_fulfillment_cost = statistics.median([reward.fulfillment_cost for reward in self.episode_reward_objects])
        self.avg_late_pct = statistics.mean([reward.late_pct for reward in self.episode_reward_objects])
        self.median_late_pct = statistics.median([reward.late_pct for reward in self.episode_reward_objects])
        self.avg_conversion_rate = statistics.mean([reward.conversion_rate_change for reward in self.episode_reward_objects])
        self.median_conversion_rate = statistics.median([reward.conversion_rate_change for reward in self.episode_reward_objects])

    def print_summary(self):
        print("Avg Reward: " + str(self.avg_reward))
        print("Median Reward: " + str(self.median_reward))
        print("Avg Fulfillment Cost: " + str(self.avg_fulfillment_cost))
        print("Median Fulfillment Cost: " + str(self.median_fulfillment_cost))
        print("Avg Late Pct: " + str(self.avg_late_pct))
        print("Median Late Pct: " + str(self.median_late_pct))
        print("Avg Conversion Rate Change: " + str(self.avg_conversion_rate))
        print("Median Conversion Rate Change: " + str(self.median_conversion_rate))

class Policy:
    iteration: int
    iteration_dispatch: int
    iteration_pay: int
    iteration_eta: int

    policy_attributes_dispatch: PolicyAttributes
    policy_attributes_pay: PolicyAttributes
    policy_attributes_eta: PolicyAttributes

    policy: Dict[State, Action]

    policy_reward: PolicyReward


    def __init__(self, iteration, iteration_dispatch, iteration_pay, iteration_eta, policy_attributes_dispatch,policy_attributes_pay,policy_attributes_eta, policy):
        self.iteration = iteration
        self.iteration_dispatch = iteration_dispatch
        self.iteration_pay = iteration_pay
        self.iteration_eta = iteration_eta
        self.policy_attributes_dispatch = policy_attributes_dispatch
        self.policy_attributes_pay = policy_attributes_pay
        self.policy_attributes_eta = policy_attributes_eta
        self.policy = policy

    def set_policy_reward(self, episode_rewards: List[Tuple[float, Reward]]):
        self.policy_reward = PolicyReward(episode_rewards)

    def print_summary(self, scenario_name: str):
        print("\nScenario: " + scenario_name)
        self.policy_reward.print_summary()