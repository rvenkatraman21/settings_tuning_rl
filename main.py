import random
from typing import List

from analytics import compare_scenarios
from data.read_actual_states import read_state_data
from rl_classes.state import ActualState
from scenario_manager import run_static_scenarios, run_dispatch_scenario, run_dispatch_pay_scenario, \
    run_dispatch_pay_eta_scenario, Scenario


def main():
    random.seed(99)
    state_data = read_state_data()
    actual_states = [ActualState.from_csv(i) for i in state_data[1:]]

    scenarios: List[Scenario] = []

    scenarios.extend(run_static_scenarios(actual_states))
    scenarios.append(run_dispatch_scenario(actual_states))

    # scenarios.append(run_dispatch_pay_scenario(actual_states))
    # scenarios.append(run_dispatch_pay_eta_scenario(actual_states))

    compare_scenarios(scenarios)

if __name__ == "__main__":
    main()
