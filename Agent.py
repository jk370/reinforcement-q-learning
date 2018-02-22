
import numpy as np
import Environment

class Agent(object):
    def __init__(self, environment, epsilon = 0.1, alpha = 0.1, gamma = 1):
        ''' Initialises all learning variables and Q table'''
        # Set up initial variables and learning tables
        self.environment = environment
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.Q = {}
        
        # Initialise Q
        for state in range(0, self.environment.num_cells):
            for action in self.environment.get_available_actions():
                self.Q[(state,action)] = 0
        
      
    def choose_action(self):
        '''Chooses to exploit Q table, or explore'''
        # Random action to explore, probability depends on epsilon
        chance = np.random.uniform(0,1)
        if (chance < self.epsilon):
            return self.random_action()
        
        # Otherwise, try to be greedy
        else:
            # Find max Q value and corresponding action from state
            state_t = self.environment.get_current_state()
            available_actions = self.environment.get_available_actions()
            max_Q = max(self.Q[(state_t, action)] for action in available_actions)
            
            # Choose random action that corresponds to max_Q
            max_actions = []
            for action in available_actions:
                if (self.Q[(state_t, action)] == max_Q):
                    max_actions.append(action)
                    
            max_action = np.random.choice(max_actions)
            return max_action
    
    def random_action(self):
        ''' Chooses a random action from those available'''
        available_actions = self.environment.get_available_actions()
        number_of_actions = len(available_actions)
        random_index = np.random.randint(0, number_of_actions)
        action = available_actions[random_index]
        return action
    
    def learn(self, old_state, action_t, new_state, reward):
        '''Updates Q table with value corresponding to latest state-action-reward'''
        available_actions = self.environment.get_available_actions()
        factor = max([self.Q[(new_state, action)] for action in available_actions])
        self.Q[(old_state, action_t)] = ((1-self.alpha) * self.Q[(old_state, action_t)]) + (self.alpha * (reward + factor))
