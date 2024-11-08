import matplotlib.pyplot as plt
from typing import List

from scenario_manager import Scenario

def compare_scenarios(scenarios: List[Scenario]):
    reward_data = []
    fulfillment_cost_data = []
    late_pct_data = []
    conversion_rate_change_data = []
    labels = []

    for scenario in scenarios:
        scenario.final_policy.print_summary(scenario.label)

        reward_data.append(scenario.reward_data)
        fulfillment_cost_data.append(scenario.fulfillment_cost_data)
        late_pct_data.append(scenario.late_pct_data)
        conversion_rate_change_data.append(scenario.conversion_rate_change_data)
        labels.append(scenario.label)

    plot_box(reward_data, labels, "Reward Distribution", "Scenarios", "Reward Distribution")
    plot_box(fulfillment_cost_data, labels, "Fulfillment Cost Distribution", "Scenarios", "Fulfillment Cost Per Delivery ($)")
    plot_box(late_pct_data, labels, "Late Pct Distribution", "Scenarios", "Late %")
    plot_box(conversion_rate_change_data, labels, "Conversion Rate Change Distribution", "Scenarios", "Conversion Rate Change")


def plot_box(data: List[List[float]], labels: List[str], chart_title: str, x_axis: str, y_axis: str):

    if len(data) != len(labels):
        raise ValueError("Length of data and labels do not match")

    fig = plt.figure()
    plt.boxplot(data,tick_labels=labels)
    plt.title(chart_title)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()