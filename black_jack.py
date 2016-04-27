import random

random.seed( 10 )


def value_function_init():
    V = {} # Value Function
    for useful_arc in [True, False]:
        for Dealer_Card_Index in range(1, 11): #[1,10]
            for Player_Sum_Index in range(1, 22): #[12,21]
                V[(useful_arc, Dealer_Card_Index, Player_Sum_Index)] = 0.0
    return V

def player_hit(card_state):
    point = get_point(card_state)
    if point >= 20: return False # False for stick
    return True # True for hit

def get_card():
    cards = [i if i<=10 else 10 for i in range(1, 14)]
    #id = random.randint(0,14)
    #return cards[id]
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
    if point >= 17: return False  # False for stick
    return True # True for hit


def black_jack_process():
    dealer_state = {"hold_arc":False, "sum":0}
    dealer_card = get_card()
    person_get_card(dealer_state, dealer_card)
    card = get_card()
    person_get_card(dealer_state, card)

    player_state = {"hold_arc":False, "sum":0}
    card = get_card()
    person_get_card(player_state, card)
    card = get_card()
    person_get_card(player_state, card)

    episode = []
    reward = 0

    while True:
        state = (player_state["hold_arc"], dealer_card, get_point(player_state))

        #print "player_state", player_state
        player_action = player_hit(player_state)
        if player_action: 
            card = get_card()
            person_get_card(player_state, card)
        
       # print "dealer_state", dealer_state
        dealer_action = dealer_hit(dealer_state)
        if dealer_action: 
            card = get_card()
            person_get_card(dealer_state, card)

        episode.append((state, "hits" if player_action else "sticks"))
 #       print episode

        if not player_action and not dealer_action:
           dealer_point = final_point(dealer_state) 
           player_point = final_point(player_state) 
           if dealer_point == player_point: 
               reward = 0
           elif dealer_point > player_point: 
               reward = -1
           else: 
               reward = 1
           break
    return episode, reward

#episode, reward = black_jack_process()
#print episode
#print reward


def MC_Policy_Evaluation():
    V = value_function_init()
    COUNT= value_function_init()

    episodes_num = 10000
    for i in range(1, episodes_num+1):
        episode, reward = black_jack_process()
        #print  episode, reward 
        for (state, action) in episode:
            if state[2] > 21: continue
            #V[state] = V[state] + 1.0 * (reward - V[state])/i
            V[state] = V[state] + reward 
            COUNT[state] = COUNT[state] + 1
        #print reward
    for state in V.keys():
        if state[2] > 21 or COUNT[state] == 0: continue
        V[state] = V[state]/COUNT[state]
    return V



def print_useable_arc(V):
    for Player_Sum_Index in reversed(range(12, 22)): #[12,21]
         line = " "
         for Dealer_Card_Index in range(1, 11): #[1,10]
             line += str(V[(True, Dealer_Card_Index, Player_Sum_Index)]) + " "
         print line


def print_nouseable_arc(V):
    for Player_Sum_Index in reversed(range(12, 22)): #[12,21]
         line = " "
         for Dealer_Card_Index in range(1, 11): #[1,10]
             line += str(int(V[(False, Dealer_Card_Index, Player_Sum_Index)] * 100) / 100.0) + " "
         print line


V = MC_Policy_Evaluation()
print_nouseable_arc(V) 

print ""

