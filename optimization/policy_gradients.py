import random
from rl_classes.policy import Policy

def update_policy(curr_policy: Policy, prev_policy: Policy, prev_prev_policy: Policy) -> Policy:

    action_component = random.random()
    anneal_component = random.random()

    curr_reward = curr_policy.policy_reward.avg_reward
    prev_reward = prev_policy.policy_reward.avg_reward
    prev_prev_reward = prev_prev_policy.policy_reward.avg_reward

    policy1 = curr_policy
    if prev_reward > prev_prev_reward:
        policy2 = prev_policy
    else:
        policy2 = prev_prev_policy

    new_policy = curr_policy

    if curr_policy.policy_attributes_dispatch.if_update and curr_policy.policy_attributes_dispatch.probability_update >= action_component:
        for state in curr_policy.policy.keys():
            current_action = policy1.policy[state]
            new_policy.policy[state] = current_action.get_new_action_dispatch(policy2.policy[state].dispatch_settings, curr_policy.policy_attributes_dispatch.probability_anneal > anneal_component)
        new_policy.iteration_dispatch +=1
        new_policy.iteration +=1

    elif curr_policy.policy_attributes_pay.if_update and curr_policy.policy_attributes_pay.probability_update >= action_component:
        for state in curr_policy.policy.keys():
            current_action = policy1.policy[state]
            new_policy.policy[state] = current_action.get_new_action_pay(policy2.policy[state].pay_settings, curr_policy.policy_attributes_pay.probability_anneal > anneal_component)
        new_policy.iteration_pay +=1
        new_policy.iteration +=1

    elif curr_policy.policy_attributes_eta.if_update:
        for state in curr_policy.policy.keys():
            current_action = policy1.policy[state]
            new_policy.policy[state] = current_action.get_new_action_eta(policy2.policy[state].eta_settings, curr_policy.policy_attributes_eta.probability_anneal > anneal_component)
        new_policy.iteration_eta +=1
        new_policy.iteration +=1

    return new_policy