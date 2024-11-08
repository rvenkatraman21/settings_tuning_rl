from typing import List

from rl_classes.action import Action
from rl_classes.policy import Policy, PolicyAttributes
from rl_classes.state import State

class PolicyInitialization:

    @staticmethod
    def initialize_policy_static(states: List[State], dispatch_setting: float) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(dispatch_setting,0,0)
        dispatch_policy_attribute = PolicyAttributes(True, False, 0.0, 0.05)
        pay_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)
        eta_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)

        return Policy(0,0,0,0,dispatch_policy_attribute,pay_policy_attribute,eta_policy_attribute,policy)

    @staticmethod
    def initialize_policy_dispatch_low_end(states: List[State]) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(0.6,-2.0,-2)
        dispatch_policy_attribute = PolicyAttributes(True, True, 1.0, 0.0)
        pay_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)
        eta_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)

        return Policy(0,0,0,0,dispatch_policy_attribute,pay_policy_attribute,eta_policy_attribute,policy)

    @staticmethod
    def initialize_policy_dispatch_middle(states: List[State]) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(1.0, 0.0, 0)
        dispatch_policy_attribute = PolicyAttributes(True, True, 1.0, 0.0)
        pay_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)
        eta_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)

        return Policy(0, 0, 0, 0, dispatch_policy_attribute, pay_policy_attribute, eta_policy_attribute, policy)


    @staticmethod
    def initialize_policy_dispatch_high_end(states: List[State]) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(2.0, 2.0, 2)
        dispatch_policy_attribute = PolicyAttributes(True, True, 1.0, 0.0)
        pay_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)
        eta_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)

        return Policy(0, 0, 0, 0, dispatch_policy_attribute, pay_policy_attribute, eta_policy_attribute, policy)


    @staticmethod
    def initialize_policy_dispatch_pay_low_end(states: List[State]) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(0.6,-2.0,0)
        dispatch_policy_attribute = PolicyAttributes(True, True, 0.5, 0.0)
        pay_policy_attribute = PolicyAttributes(True, True, 1.0, 0.0)
        eta_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)

        return Policy(0,0,0,0,dispatch_policy_attribute,pay_policy_attribute,eta_policy_attribute,policy)

    @staticmethod
    def initialize_policy_dispatch_pay_middle(states: List[State]) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(1.0, 0.0, 0)
        dispatch_policy_attribute = PolicyAttributes(True, True, 0.5, 0.0)
        pay_policy_attribute = PolicyAttributes(True, True, 1.0, 0.0)
        eta_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)

        return Policy(0, 0, 0, 0, dispatch_policy_attribute, pay_policy_attribute, eta_policy_attribute, policy)


    @staticmethod
    def initialize_policy_dispatch_pay_high_end(states: List[State]) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(2.0, 2.0, 0)
        dispatch_policy_attribute = PolicyAttributes(True, True, 0.5, 0.0)
        pay_policy_attribute = PolicyAttributes(True, True, 1.0, 0.0)
        eta_policy_attribute = PolicyAttributes(True, False, 0.0, 0.0)

        return Policy(0, 0, 0, 0, dispatch_policy_attribute, pay_policy_attribute, eta_policy_attribute, policy)

    @staticmethod
    def initialize_policy_dispatch_pay_eta_low_end(states: List[State]) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(0.6,-2.0,-2)
        dispatch_policy_attribute = PolicyAttributes(True, True, 0.5, 0.0)
        pay_policy_attribute = PolicyAttributes(True, True, 0.75, 0.0)
        eta_policy_attribute = PolicyAttributes(True, True, 1.0, 0.0)

        return Policy(0,0,0,0,dispatch_policy_attribute,pay_policy_attribute,eta_policy_attribute,policy)

    @staticmethod
    def initialize_policy_dispatch_pay_eta_middle(states: List[State]) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(1.0, 0.0, 0)
        dispatch_policy_attribute = PolicyAttributes(True, True, 0.5, 0.0)
        pay_policy_attribute = PolicyAttributes(True, True, 0.75, 0.0)
        eta_policy_attribute = PolicyAttributes(True, True, 1.0, 0.0)

        return Policy(0, 0, 0, 0, dispatch_policy_attribute, pay_policy_attribute, eta_policy_attribute, policy)


    @staticmethod
    def initialize_policy_dispatch_pay_eta_high_end(states: List[State]) -> Policy:
        policy = {}
        for state in states:
            policy[state] = Action(2.0, 2.0, 2)
        dispatch_policy_attribute = PolicyAttributes(True, True, 0.5, 0.0)
        pay_policy_attribute = PolicyAttributes(True, True, 0.75, 0.0)
        eta_policy_attribute = PolicyAttributes(True, True, 1.0, 0.0)

        return Policy(0, 0, 0, 0, dispatch_policy_attribute, pay_policy_attribute, eta_policy_attribute, policy)

