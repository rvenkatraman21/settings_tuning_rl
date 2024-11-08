
# Simulation Configs
TIME_PERIODS = 56
NUM_EPISODES = 100
NUM_SIMULATIONS = 100

# Data Processing
# This is used to classify continuous data into categories to discretize states
STATE_DELIVERIES_CATEGORIES = [0, 50, 150, 500]
STATE_COURIERS_CATEGORIES = [0, 50, 150, 500]
STATE_ETA_ERROR_CATEGORIES = [-100, -1, 0, 1, 100]
STATE_ENGAGED_TIME_CATEGORIES = [-50, 30, 40, 100]

# Reward Configs
REWARD_WEIGHT_LATE_PCT = 15.0
REWARD_WEIGHT_CONVERSION = 2.0

# Actions

# Dispatch Actions
ACTION_MIN_DISPATCH_SETTING = 0.6
ACTION_MAX_DISPATCH_SETTING = 2.0
DISPATCH_SETTING_STEP_SIZE = 0.1

# Pay Actions
# This represents a budget injection per delivery
ACTION_MIN_PAY_SETTING = -2.0
ACTION_MAX_PAY_SETTING = 2.0
PAY_SETTING_STEP_SIZE = 1.0

# ETA Actions
# This represents ETA adjustments per delivery
ACTION_MIN_ETA_SETTING = -2.0
ACTION_MAX_ETA_SETTING = 2.0
ETA_SETTING_STEP_SIZE = 1.0