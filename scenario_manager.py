from typing import List, Optional, Tuple

import config
from rl_classes.environment import Episode
from optimization.policy_initialization import PolicyInitialization
from rl_classes.policy import Policy
from rl_classes.state import ActualState, State
from simulator import Simulator

class Scenario:
    actual_states: List[ActualState]
    initial_policies: Tuple[Policy, Optional[Policy], Optional[Policy]]
    if_optimize: bool
    label: str
    final_policy: Policy

    reward_data: List[float]
    fulfillment_cost_data: List[float]
    late_pct_data: List[float]
    conversion_rate_change_data: List[float]

    def __init__(self, actual_states: List[ActualState], initial_policies: Tuple[Policy, Optional[Policy], Optional[Policy]], if_optimize: bool, label: str):
        self.actual_states = actual_states
        self.initial_policies = initial_policies
        self.if_optimize = if_optimize
        self.label = label
        self.final_policy = initial_policies[0]
        self.reward_data = []
        self.fulfillment_cost_data = []
        self.late_pct_data = []
        self.conversion_rate_change_data = []

    def run(self):
        episode = Episode.initialize(self.actual_states)
        self.final_policy = self.initial_policies[0]
        if self.if_optimize:
            self.final_policy = Simulator.optimize_policy(episode, self.initial_policies)

        Simulator.simulate_given_policy(self.final_policy, episode)

        self.reward_data = self.final_policy.policy_reward.episode_total_rewards
        self.fulfillment_cost_data = [reward.fulfillment_cost for reward in self.final_policy.policy_reward.episode_reward_objects]
        self.late_pct_data.append = [reward.late_pct for reward in self.final_policy.policy_reward.episode_reward_objects]
        self.conversion_rate_change_data = [reward.conversion_rate_change for reward in self.final_policy.policy_reward.episode_reward_objects]


def run_static_scenarios(actual_states: List[ActualState]) -> List[Scenario]:
    episode = Episode.initialize(actual_states)
    states: List[State] = [step.state for step in episode.steps]

    all_scenarios: List[Scenario] = []

    dispatch_setting = config.ACTION_MIN_DISPATCH_SETTING
    while dispatch_setting < config.ACTION_MAX_DISPATCH_SETTING:
        episode = Episode.initialize(actual_states)
        states: List[State] = [step.state for step in episode.steps]
        static_policy = PolicyInitialization.initialize_policy_static(states, dispatch_setting)

        scenario = Scenario(actual_states, (static_policy, None, None), False, str(dispatch_setting))
        scenario.run()
        all_scenarios.append(scenario)

        dispatch_setting = round(dispatch_setting + config.DISPATCH_SETTING_STEP_SIZE,2)

    return all_scenarios

def run_dispatch_scenario(actual_states: List[ActualState]) -> Scenario:
    episode = Episode.initialize(actual_states)
    states: List[State] = [step.state for step in episode.steps]

    policy1 = PolicyInitialization.initialize_policy_dispatch_low_end(states)
    policy2 = PolicyInitialization.initialize_policy_dispatch_high_end(states)
    policy3 = PolicyInitialization.initialize_policy_dispatch_middle(states)

    optimized_scenario = Scenario(actual_states, (policy1, policy2, policy3), True, "Dispatch Only")
    optimized_scenario.run()

    return optimized_scenario

def run_dispatch_pay_scenario(actual_states: List[ActualState]) -> Scenario:
    episode = Episode.initialize(actual_states)
    states: List[State] = [step.state for step in episode.steps]

    policy1 = PolicyInitialization.initialize_policy_dispatch_pay_low_end(states)
    policy2 = PolicyInitialization.initialize_policy_dispatch_pay_high_end(states)
    policy3 = PolicyInitialization.initialize_policy_dispatch_pay_middle(states)

    optimized_scenario = Scenario(actual_states, (policy1, policy2, policy3), True, "Dispatch + Pay")
    optimized_scenario.run()

    return optimized_scenario


def run_dispatch_pay_eta_scenario(actual_states: List[ActualState]) -> Scenario:
    episode = Episode.initialize(actual_states)
    states: List[State] = [step.state for step in episode.steps]

    policy1 = PolicyInitialization.initialize_policy_dispatch_pay_eta_low_end(states)
    policy2 = PolicyInitialization.initialize_policy_dispatch_pay_eta_high_end(states)
    policy3 = PolicyInitialization.initialize_policy_dispatch_pay_eta_middle(states)

    optimized_scenario = Scenario(actual_states, (policy1, policy2, policy3), True, "Dispatch + Pay + ETA")
    optimized_scenario.run()

    return optimized_scenario