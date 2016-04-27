import random

class BlackJack(object):
	
    def start_new_game():
	self.game_on = True

        self.dealer_state = {"hold_arc":False, "sum":0}
        self.dealer_card = self.get_card()
        self.person_get_card(self.dealer_state, self.dealer_card)
        card = self.get_card()
        self.person_get_card(self.dealer_state, card)
	
        self.player_state = {"hold_arc":False, "sum":0}
        card = self.get_card()
        self.person_get_card(self.player_state, card)
        card = self.get_card()
        self.person_get_card(self.player_state, card)

        self.state = (self.player_state["hold_arc"], self.dealer_card, self.get_point(self.player_state))
	

    def feed_back(action):
	if self.game_on:	    
	    new_state = self.state_function(action)
            reward = self.reward_function(self.state, action, new_state)
            self.state = new_state
            return self.state, reward
        else:
	    return self.state, 0
		

    def state_function(action):
        if action == 'hits': 
            card = get_card()
            self.person_get_card(self.player_state, card)
		
        dealer_action = dealer_hit(self.dealer_state)
        if dealer_action == 'hits': 
            card = self.get_card()
            self.person_get_card(self.dealer_state, card)
		
        if action != 'hits':
            dealer_action = dealer_hit(self.dealer_state)
            while dealer_action == 'hits': 
                card = self.get_card()
                self.person_get_card(self.dealer_state, card)
                dealer_action = self.dealer_hit(self.dealer_state)
		
        if action != 'hits' and dealer_action != 'hits':
            dealer_point = final_point(dealer_state) 
            player_point = final_point(player_state) 
            if dealer_point == player_point: 
                state = 'Tie'
            elif dealer_point > player_point: 
                state = 'Lose'
            else: 
                state = 'Win'
	    self.game_on = False	
        else:
            state = (self.player_state["hold_arc"], self.dealer_card, self.get_point(player_state))
        return state


    def reward_function(state, action, new_state):
        if type(new_state) == type(''):
            if new_state == 'Win':
                return 1
            elif new_state == 'Lose':
                return -1
	    else:
		return 0
        return 0

	    
    def get_card():
        cards = [i if i<=10 else 10 for i in range(1, 14)]
        return random.choice(cards)


    def person_get_card(card_state, card = get_card()): # card_state = [hold_arc: True or False, sum: number]
        if card == 1: card_state["hold_arc"] = True
        card_state["sum"] = card_state["sum"] + card


    def get_point(card_state):
        if card_state["hold_arc"] and card_state["sum"] + 10 <= 21:
            return card_state["sum"] + 10
	return card_state["sum"]


    def final_point(card_state):
        point = get_point(card_state)
        if point > 21: return 0
        return point


    def dealer_hit(card_state):
        point = get_point(card_state)
        if point >= 17: return 'sticks'  # False for stick
        return 'hits' # True for hit


actions = ['hits' for i in range(4)]
game = BlackJack()

print game.get_card()
