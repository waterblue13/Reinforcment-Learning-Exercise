import random

class BlackJackPlayer(Agent):

    def __init__():
        self.policy_function = random_policy_function


    def take_action(state, policy_function = self.policy_function):
	return policy_function(state)

	
    def set_policy_function(policy_function):
        self.policy_function = policy_function
   	
	
    def random_policy_function(state):
        return random.choice(['hits', 'sticks'])
