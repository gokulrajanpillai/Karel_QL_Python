import QLearning
import KarelEnvironment

# Perform action for current state
def perform_action(action):
    state = KarelEnvironment.karel_current_state
    if action == KarelEnvironment.karel_actions[0]:
        state = KarelEnvironment.move_karel(-1, 0)
    elif action == KarelEnvironment.karel_actions[1]:
        state = KarelEnvironment.move_karel(1, 0)
    elif action == KarelEnvironment.karel_actions[2]:
        state = KarelEnvironment.move_karel(0, -1)
    elif action == KarelEnvironment.karel_actions[3]:
        state = KarelEnvironment.move_karel(0, 1)
    return state, reward(state)

def main():
    print("Q.L invoked")
    QLearning.init_and_start()
    print("K.E invoked")
    KarelEnvironment.init_and_start()
    print("main-method invoked")

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()
