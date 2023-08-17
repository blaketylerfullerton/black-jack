import random
import array
import time



print("********Welcome to my blackjack game********")
print("--------------------------------------------")
print("********Creating and shuffling deck********")

sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
deck_of_cards = []
my_hand = []
dealers_hand = []
bet_balance = 100
temp = 0
current_bet = 0



#Giving each card 4 suits
for size in sizes:
    deck_of_cards.extend([size] * 4)  # Each size represents a suit with 4 cards

#my_array = array.array('i', deck_of_cards)
#print("Deck: ",my_array)
#print("\n")

#Shuffle
random.shuffle(deck_of_cards)
def shuffle_animation():
    print("-----Shuffling----")
    bar = [
        "     [=       ]",
        "     [ =      ]",
        "     [   =    ]",
        "     [    =   ]",
        "     [     =  ]",
        "     [       =]",
        "     [     =  ]",
        "     [   =    ]",
        "     [ =      ]",
        "     [=       ]",
        ]
    i = 0
    loadcount = 0
    while loadcount < 15:
        print(bar[i % len(bar)], end="\r")
        time.sleep(.2)
        i+=1
        loadcount +=1



shuffle_animation()
print("-----Shuffled----")
print("--------------------------------------------\n\n\n")


def start():


    #bet_balance = int(input("How much would you like to bet today?: "))
    print("Your starting balance: ", bet_balance)
    current_bet = int(input("How much would you like to bet?  "))
    print("Your hand: ", deck_of_cards[-1])
    _ = deck_of_cards[-1]
    my_hand.append(_)
    print(my_hand)
    deck_of_cards.pop(-1)

    print("Dealers hand: ")
    _ = deck_of_cards[-1]
    dealers_hand.append(_)
    print(dealers_hand)
    deck_of_cards.pop(-1)


def run_sim(): 
    #print(deck_of_cards)

    def my_hit():
        _ = deck_of_cards[-1]
        my_hand.append(_)
        deck_of_cards.pop(-1)
        print("Your hand: ")
        print(my_hand)
        print ("Total: ",sum(my_hand))
        if sum(my_hand) > 21:
            print("Sorry! You busted. Total", sum(my_hand) )
            print(bet_balance - current_bet)
            next_turn()
    def dealer_hit():
        while sum(dealers_hand) <= 17:
            _ = deck_of_cards[-1]
            dealers_hand.append(_)
            deck_of_cards.pop(-1)
            time.sleep(1)
            print("Dealers hand: ", sum(dealers_hand))
            if (sum(dealers_hand) > sum(my_hand)) & (sum(dealers_hand) < 22):
                print(dealers_hand)
                print("Dealer Won")
                next_turn()
            if sum(dealers_hand) > 22:
                print(dealers_hand)
                print("Dealer busted. Total", sum(dealers_hand) )
                next_turn()
                
            print(dealers_hand)
        if sum(dealers_hand) > sum(my_hand):
            print("You lost")
            next_turn()
            

    user_do = input("Would you like to hit?. Y/N:   ")
    if user_do == 'y':
        my_hit()
    if user_do == 'n':
        dealer_hit()


def next_turn():
    user_do1 = input("Would you like to keep playing?: y/n\t")

    if user_do1 == 'y':
        start()
        run_sim()
    if user_do1 == 'n':
        quit()
    

start()
while sum(dealers_hand) & sum(my_hand) < 22:
    run_sim() 
