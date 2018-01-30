import KarelController
import KarelEnvironment
import threading
import time

# Discount or gamma value defining whether immediate rewards should have priority
# Here it is set close to zero to give more importance to future rewards
discount = 0.3

# States and actions defining the behavior of the system
actions = []
states = []

# Q-matrix defining the policies for what action should be taken on each particular state of the system
q_matrix = {}

# Initialize the actions of the environment
def init_actions():
    global actions
    actions = KarelController.karel_actions()

# Initialize the states of the system
def init_states():
    global states
    states = KarelController.karel_states()

# Initialize q-matrix values
def init_q_matrix_values():
    for state in states:
        temp = {}
        for action in actions:
            temp[action] = 0.1
        q_matrix[state] = temp

# Initialize reward matrix from the special cells that are defined
def init_r_matrix_values():
    special_cells = KarelController.special_cells()
    for (i, j, color, reward) in special_cells:
        for action in actions:
            q_matrix[(i, j)][action] = reward

# Get the best action for the given state by finding the action with the highest Q-value
def max_q_value_for_state(state):
    best_q_value = None
    best_action = None
    for action, q_value in q_matrix[state].items():
        if best_q_value is None or (q_value > best_q_value):
            best_q_value = q_value
            best_action = action
    return best_action, best_q_value

# Update the value of Q-matrix
def update_q_matrix(state, action, alpha, inc):
    q_matrix[state][action] *= 1 - alpha
    q_matrix[state][action] += alpha * inc

def run():
    global discount
    time.sleep(1)
    alpha = 1
    count = 1
    while True:
        # Find the current position of Karel
        karel_position = KarelController.current_position_of_karel()
        current_state = karel_position
        # Retrieve the best action for the state
        best_action, max_val = max_q_value_for_state(current_state)
        # Append action to KarelController final set of actions
        KarelController.final_set_of_actions.append(best_action)
        # Perform the action and retrieve the reward and future state
        (current_state, best_action, reward, future_state) = KarelController.perform_action(best_action)

        # Find the best action for the future state retrieved
        best_future_action, max_val = max_q_value_for_state(future_state)
        # Calculate value to increment
        increment = reward + discount * max_val
        # Update Q-matrix with the incremented value
        update_q_matrix(current_state, best_action, alpha, increment)

        # Check if the game has restarted
        count += 1.0
        if KarelController.should_restart():
            if KarelController.should_terminate():
                print ("Final actions: ",KarelController.final_set_of_actions)
                sys.exit(0)
            else:
                # Clear action array of controller
                KarelController.final_set_of_actions = []
            time.sleep(0.01)
            count = 1.0

        # Reduce the learning rate
        alpha = pow(count, -0.1)

        # MODIFY THIS SLEEP IF THE GAME IS GOING TOO FAST.
        time.sleep(0.1)

def init_and_start():
    init_actions()
    init_states()
    init_q_matrix_values()
    init_r_matrix_values()
    t = threading.Thread(target=run)
    t.daemon = True
    t.start()
