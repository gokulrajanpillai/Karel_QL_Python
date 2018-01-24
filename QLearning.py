import KarelEnvironment
import threading
import time

# Array representing the final set of instructions
final_instruction = []

# Array representing the reward matrix
r_matrix = {}

# Array representing the Q-matrix
q_matrix = {}

# Array representing the states of the system
states = []

# Array representing the possible set of actions for the states in the system
actions = []

# Gamma, a.k.a discount value, determines the effect of current rewards on the Q-matrix
# If discount is close to one, current rewards will have direct effect on
# values in Q-matrix and if it is close to zero, they would not have any
# effect at all
gamma = 0.7

# Alpha represents the learning rate of the algorithm
alpha = 1

# Configure states for the Q_matrix
def configure_states():
    # Add states for QL from the KarelEnvironment
    for i in range(KarelEnvironment.DIM_X):
        for j in range(KarelEnvironment.DIM_Y):
            states.append((i, j))

# Configure actions for the Q matrix
def configure_actions():
    # Add actions for QL
    for action in KarelEnvironment.karel_actions:
        actions.append(action)

# Update Q-matrix values
def initialize_qmatrix_values():
    print("States: ",states)
    for state in states:
        temp = {}
        print("Actions: ",actions)
        for action in actions:
            temp[action] = 0
            if state == KarelEnvironment.KAREL_END_STATE:
                temp[action] = 1
        q_matrix[state] = temp
    print("Q-matrix is ",q_matrix)

# Initialize QLearning algorithm
def initialize_qlearning():
    configure_states()
    configure_actions()
    initialize_qmatrix_values()

# Fetch q-value for state and action from the Q-matrix
def qvalue_for_state_and_action(state, action):
    return q_matrix[state][action]

# Fetch action with maximum Q-value using the current state and Q-matrix
def best_action_for_state(current_state):
    action = None
    q_value = None
    # Go through all the action and q_value combinations of the Q-matrix for the provided current state
    for i_action, i_q_value in q_matrix[current_state].items():
        # If no action has been assigned so far, then assign the selected action from the Q-matrix
        # Or, if the q_value of iterated action (i_action) is greater than the q_value of the selected action, then assign the selected action as the iterated action
        if action is None or (i_q_value > q_value):
            q_value = i_q_value
            action = i_action
    print("best action is ",action," for state ",current_state," with q-value ",q_value)
    return action, q_value

# Update q-value for a given state and action
def update_qvalue_for_state_and_action(state, action, reward):
    q_matrix[state][action] += alpha * ()
    return "Hello"

# Perform the action for the given state
def perform(state, action):
    print("perform action ",action," for state ",state)
    import KarelController
    reward = KarelController.perform_action(action)
    return reward

# Q-Learning algorithm
def run():
    time.sleep(1)
    print("Q-Learning invoked")
    while True:
        # Fetch the current state of Karel in the environment
        state = KarelEnvironment.karel_current_state
        # Select the best action to perform for the current state using the Q-matrix
        action, q_value = best_action_for_state(state)
        # Perform the action for the current state and retrieve the new state and reward
        (new_state, reward) = perform(state, action)
        # Fetch the q_value for the new state using the Q-matrix
        action, q_value = best_action_for_state(new_state)
        # Update the q-value in the Q-matrix using the reward from the KarelEnvironment
        update_qvalue_for_state_and_action(state, action)
        # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.1)

# Start daemon for Q-Learning algorithm
def start_daemon():
    thread = threading.Thread(target=run)
    thread.daemon = True
    thread.start()

# Initialize and start the algorithm
def init_and_start():
    print("init and start q-learning")
    initialize_qlearning()
    start_daemon()
