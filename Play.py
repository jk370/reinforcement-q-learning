import matplotlib.pyplot as plt
from IPython.display import clear_output
%matplotlib inline

# State = agents position
# Action = Movement chosen

def play(environment, agent, episodes = 500):
    '''Plays the game and learns how to improve'''
    for games in range(0, episodes):
        # Reset agent position and initialise plotter
        environment.reset_agent()

        # Keep track of reward for learning graph
        total_reward = 0

        # Loop for one episode
        while (env.agent_position not in env.terminal_states):
            # Get state for current step in episode
            state_t = environment.get_current_state()

            # Get available actions for current state - currently fixed
            available_actions = env.get_available_actions()  

            # Choose action taken
            action_t = agent.choose_action()

            # Receive reward from action taken and observe new state
            reward_t = env.make_step(action_t)
            state_t1 = env.get_current_state()

            # Let the agent learn from the action
            agent.learn(state_t, action_t, state_t1, reward_t)

            # Add to total reward
            total_reward += reward_t
            '''
            # Update plotter - visualization of learning process
            step = env.get_game_array()
            plt.matshow(step)
            plt.show()
            clear_output(wait=True)
            '''
            '''
            # Print information:
            print("Current position of the agent = ", state_t)
            print("Available_actions =", available_actions)
            print("Chosen action =", action_t)
            print("Reward obtained =", reward_t)
            print("New state =", state_t1)
            print()
            '''
        reward_array.append(total_reward)

# Play scenario
env = Gridworld()
agent = Agent(env, epsilon = 0.1, alpha = 0.1, gamma = 1)
reward_array = []
play(env, agent, episodes = 500)

# Plot reward graph
plt.figure(1)
plt.plot(reward_array)
plt.title("Learning Graph")
plt.xlabel("Episode")
plt.ylabel("Reward Received")