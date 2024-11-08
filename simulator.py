from typing import List, Tuple

import config
from rl_classes.environment import Episode
from optimization.policy_gradients import update_policy
from rl_classes.policy import Policy
from rl_classes.reward import Reward

class Simulator:

    @staticmethod
    def simulate_episode(episode: Episode, policy: Policy) -> Tuple[float, Reward]:

        time_periods = len(episode.steps)
        for t in range(time_periods):
            step = episode.steps[t]
            step.action = policy.policy[step.state]
            step.set_reward()

            # state transition logic goes here

        episode.compute_total_reward()
        return episode.total_reward, episode.net_reward

    @staticmethod
    def simulate_given_policy(policy: Policy, episode: Episode):

        episode_rewards: List[Tuple[float, Reward]] = []
        for i in range(config.NUM_EPISODES):
            episode_rewards.append(Simulator.simulate_episode(episode, policy))

        policy.set_policy_reward(episode_rewards)
        policy.policy_reward.compute_net_reward()

    @staticmethod
    def optimize_policy(episode: Episode, initial_policies: Tuple[Policy, Policy, Policy]) -> Policy:

        policy1, policy2, policy3 = initial_policies

        Simulator.simulate_given_policy(policy1, episode)
        Simulator.simulate_given_policy(policy2, episode)
        Simulator.simulate_given_policy(policy3, episode)

        curr_policy = policy3
        print("\n\n")
        for i in range(config.NUM_SIMULATIONS):
            new_policy = update_policy(curr_policy, policy2, policy1)
            Simulator.simulate_given_policy(new_policy, episode)

            policy1 = policy2
            policy2 = curr_policy
            curr_policy = new_policy

        return curr_policy