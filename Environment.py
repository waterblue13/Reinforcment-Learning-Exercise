
class Environment(object):

	def __init__(state):
		self.state = state

	def feed_back(action, state_function, reward_function):
		new_state = state_function(state, action)
		reward = reward_function(state, action, new_state)
		self.state = new_state
		return self.state, reward
