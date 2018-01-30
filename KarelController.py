import KarelEnvironment
import QLearning

# To terminate the algorithm and define a path after Karel used one particular
# path for the following number of times
COUNT_FOR_TERMINATE = 10

# Array to store the path scores
path_scores = []

# Array path
final_set_of_actions = []

# Actions from the KarelEnvironment
def karel_actions():
    return KarelEnvironment.karel_actions

# Actions from the KarelEnvironment
def karel_states():
    karel_states = []
    for i in range(KarelEnvironment.DIM_X):
        for j in range(KarelEnvironment.DIM_Y):
            karel_states.append((i, j))
    return karel_states

# Current position of karel
def current_position_of_karel():
    return KarelEnvironment.karel_position

# Special cells in the KarelEnvironment
def special_cells():
    return KarelEnvironment.rewarding_cells

# Check if the algorithm should terminate
def should_terminate():
    global path_scores
    if len(path_scores) > COUNT_FOR_TERMINATE:
        scores_are_same = True
        last_score = path_scores[-1]
        for n in range(2, COUNT_FOR_TERMINATE + 1):
            if last_score != path_scores[-n]:
                scores_are_same = False
        return scores_are_same
    else:
        return False

# If the KarelEnvironment had reached a terminal state (rewarding state) and should restart
def should_restart():
    if KarelEnvironment.has_restarted():
        KarelEnvironment.restart_game()
        return True
    return False

# Perform action for current state of the KarelEnvironment
def perform_action(action):
    karel_position = current_position_of_karel()
    state = karel_position
    reward = -KarelEnvironment.karel_score
    if action == KarelEnvironment.karel_actions[0]:
        KarelEnvironment.move_karel(0, -1)
    elif action == KarelEnvironment.karel_actions[1]:
        KarelEnvironment.move_karel(0, 1)
    elif action == KarelEnvironment.karel_actions[2]:
        KarelEnvironment.move_karel(-1, 0)
    elif action == KarelEnvironment.karel_actions[3]:
        KarelEnvironment.move_karel(1, 0)
    else:
        return
    new_state = KarelEnvironment.karel_position
    reward += KarelEnvironment.karel_score
    return state, action, reward, new_state


def main():
    print("Q.L invoked")
    QLearning.init_and_start()
    print("K.E invoked")
    KarelEnvironment.init_and_start()
    print("main-method invoked")

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
