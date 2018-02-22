import numpy as np

class Gridworld(object):
    def __init__ (self, num_rows = 5, num_cols = 5, epsilon = 0.1):
        '''Initialises grid environment with agent, bomb and gold'''
        # Initialise Grid
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.num_cells = self.num_cols * self.num_rows
        self.epsilon = epsilon
        
        #Load initial agent position (random) in 1D array
        self.agent_position = np.random.randint(0,num_cols)
        
        #Load intial position of gold and bomb (fixed) in 1D array
        self.bomb_positions = np.array([18])
        self.gold_positions = np.array([23])
        self.terminal_states = np.array([self.bomb_positions, self.gold_positions])
        
        #Specify rewards
        self.rewards = np.zeros(self.num_cells)
        self.rewards[self.bomb_positions] = -10
        self.rewards[self.gold_positions] = 10
        
        #Specify available actions
        self.actions = ["UP", "RIGHT", "DOWN", "LEFT"]
    
    def get_available_actions(self):
        '''Return available actions'''
        return self.actions
    
    def get_current_state(self):
        '''Returns current agent position'''
        return self.agent_position
    
    def reset_agent(self):
        '''Resets agent position'''
        self.agent_position = np.random.randint(0,5)
        
    def get_game_array(self):
        '''Creates and return current state of the game board for display'''
        # Create game board
        game = np.zeros(shape=(self.num_rows, self.num_cols), dtype = int)
        bomb = np.unravel_index([self.bomb_positions], (5,5))
        gold = np.unravel_index([self.gold_positions], (5,5))
        agent = np.unravel_index([self.agent_position], (5,5))
        game[bomb] = 3
        game[gold] = 2
        game[agent] = 1
        return game
    
    def make_step(self, action):
        '''Takes action and attempts to move the agent in that direction'''
        # Make a stochastic environment - random move 10% of the time
        stochastic = np.random.uniform(0,1)
        if stochastic < self.epsilon:
            rand_move = np.random.randint(0,4)
            action = self.actions[rand_move]
            
        old_position = self.agent_position
        new_position = self.agent_position
        
        # Update new_position based on the chosen action and check whether agent hits a wall.
        if action == "UP":
            # Move player along 1D array the number of columns (to go up 1)
            candidate_position = self.agent_position + self.num_cols
            if candidate_position < self.num_cells:
                new_position = candidate_position
                
        elif action == "RIGHT":
            candidate_position = self.agent_position + 1
            if candidate_position % self.num_cols > 0:
                new_position = candidate_position
                
        elif action == "DOWN":
             # Move player along 1D array the number of columns (to go up 1)
            candidate_position = self.agent_position - self.num_cols
            if candidate_position >= 0:
                new_position = candidate_position
                
        elif action == "LEFT": 
            candidate_position = self.agent_position - 1
            if candidate_position % self.num_cols < self.num_cols - 1:
                new_position = candidate_position
                
        else:
            raise ValueError('Action was mis-specified!')
        
        # Update the position of the agent.
        self.agent_position = new_position
        
        # Get reward 
        reward = self.rewards[new_position]
        
        # Deduct 1 from reward for taking action
        if old_position != new_position:
            reward -= 1
        
        return reward