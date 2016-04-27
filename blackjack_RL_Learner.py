import random

class BlackJackLearner(object):
   
    def __init__():
	self.blackjack = BlackJack()
	self.blackjack_player = BlackJackPlayer()

	
 
    def interact_with_environment_episode():
        self.blackjack.start_new_game()
	self.blackjack_player.set_policy_function(self.fixed_policy_function)
	episode = []
	while self.blackjack.game_on:
	       state = copy(self.blackjack.state)
	       action = self.blackjack_player.take_action(state)
	       new_state, reward = self.blackjack.feed_back(action)
	       episode.append((state, action, reward))
	return episode


    def fixed_policy_function(state):
        if type(state) == type((True, 1, 1)):
            if state[2] < 20: return 'hits'
	return 'sticks'

learner = BlackJackLearner
episode = learner.interact_with_environment_episode()
