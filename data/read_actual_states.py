import csv
from pathlib import Path

data_file = str(Path(__file__).parent) + "/actual_states_initial.csv"

def read_state_data():
    state_data = list(csv.reader(open(data_file)))
    return state_data