import itertools
import random

#######################################################################################################
#The following methods until the marked point were written by an anonymous coder on the following link
#https://codereview.stackexchange.com/questions/144551/find-and-display-best-poker-hand
#######################################################################################################

def numeric_ranks(cards):
    suits = get_suits(cards)
    face_numbers = {'A': 14, 'J': 11, 'Q': 12, 'K': 13}
    for index, card in enumerate(cards):
        rank = card[0:-1]
        try: 
            int(rank)
        except:
            # Rank is a letter, not a number
            cards[index] = str(face_numbers[rank])+suits[index]
    return cards


def get_ranks(cards):
    cards = numeric_ranks(cards) # Convert rank letters to numbers (e.g. J to 11)
    return [int(card[0:-1]) for card in cards]


def get_suits(cards):
    return [card[-1] for card in cards]


def evaluate_hand(hand):
    hand = numeric_ranks(hand)
    ranks = get_ranks(hand)
    suits = get_suits(hand)
    if isconsecutive(ranks):
        # The hand is a type of straight
        if all_equal(suits):
            # Hand is a flush
            if max(ranks) == 14:
                # Highest card is an ace
                return 'Royal flush'
            return 'Straight flush'
        return 'Straight'
    if all_equal(suits):
        return 'Flush'
    total = sum([ranks.count(x) for x in ranks])
    hand_names = {
        17: 'Four of a kind',
        13: 'Full house',
        11: 'Three of a kind',
        9: 'Two pair',
        7: 'One pair',
        5: 'High card'
        }
    return hand_names[total]


def all_equal(lst):
    return len(set(lst)) == 1


def show_cards(cards):
    cards = sort_cards(cards)
    all_suits = ['C','D','H','S']
    symbols = dict(zip(all_suits,[' of Clubs', ' of Diamonds', ' of Hearts', ' of Spades']))
    faces = {14: 'Ace', 11: 'Jack', 12: 'Queen', 13: 'King'}
    card_symbols = []
    for card in cards:  
        rank = card[0:-1]
        if int(rank) in faces:
            card_symbols.append(faces[int(rank)] + symbols[card[-1]])
        else:
            card_symbols.append(rank + symbols[card[-1]])
    return card_symbols

def isconsecutive(lst):
    return len(set(lst)) == len(lst) and max(lst) - min(lst) == len(lst) - 1    


def sort_cards(cards):
    cards = numeric_ranks(cards)
    rank_list = get_ranks(cards)
    # Keep track of the sorting permutation
    new_order = sorted((e,i) for i,e in enumerate(rank_list))
    unsorted_cards = list(cards)
    for index, (a, b) in enumerate(new_order):
        cards[index] = unsorted_cards[b]
    return cards


def get_best_hand(cards):
    """ 
    Returns the best hand of five cards, from a larger list of cards.
    If ranks are alphabetical (e.g., A for ace), it will convert the rank to a number.
    ex.
    get_best_hand(['7C', '7S', '2H', '3C', 'AC', 'AD', '5S'])
    returns
    ['5S', '7C', '7S', '14C', '14D']
    """
    # All combinations of 5 cards from the larger list
    all_hand_combos = itertools.combinations(cards, 5) 
    hand_name_list = [
        'High card',
        'One pair',
        'Two pair',
        'Three of a kind',
        'Straight',
        'Flush',
        'Full house',
        'Four of a kind',
        'Straight flush',
        'Royal flush'
        ]
    num_hand_names = len(hand_name_list)
    max_value = 0
    best_hands = {x: [] for x in range(num_hand_names)}
    for combo in all_hand_combos:
        hand = list(combo)
        hand_name = evaluate_hand(hand) # Get the type of hand (e.g., one pair)
        hand_value = hand_name_list.index(hand_name)
        if hand_value >= max_value:
            # Stronger or equal hand has been found
            max_value = hand_value
            best_hands[hand_value].append(hand) # Store hand in dictionary
    max_hand_idx = max(k for k, v in best_hands.items() if len(best_hands[k])>0)
    rank_sum, max_sum = 0, 0
    # The strongest hand type out of the combinations has been found
    for hand in best_hands[max_hand_idx]: 
        # Iterate through hands of this strongest type
        ranks = get_ranks(hand)
        rank_sum = sum(ranks)
        if rank_sum > max_sum:
            max_sum = rank_sum
            best_hand = hand # Choose hand with highest ranking cards
    return best_hand

######################################################################################
#End of other user's code, Beginning of our code
######################################################################################

def findWinner(playerCards,playersList):
    i = 0
    player_rank = [0,0]
    hand_name_dict = {
        'High card':1,
        'One pair':2,
        'Two pair':3,
        'Three of a kind':4,
        'Straight':5,
        'Flush':6,
        'Full house':7,
        'Four of a kind':8,
        'Straight flush':9,
        'Royal flush':10
    }
    if playersList[0] == playersList[1]:
        return "Tie"
    while i < len(playersList):
        player_rank[i] = hand_name_dict[playersList[i]]
        i+=1
    if player_rank[0] > player_rank[1]:
        return "Computer Wins"
    else:
        return "Player Wins"

def computerChoice(computermoney,bet,playermoney):
    i = random.randint(1,3)
    if i == 1:
        if computermoney > playermoney:
            return bet + random.randint(1,playermoney)
        else:
            return bet+random.randint(1,computermoney)
    elif i == 2:
        return bet
    else:
        return -1


suits = ('C', 'D', 'H', 'S')
number = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
deck = tuple(''.join(card) for card in itertools.product(number, suits))
gameDeck = list(deck)
playercards = 0
tablecards = 0
computercards = 0
table = ["","","","",""]
hand = ["",""]
cC = ["",""]
playermoney = 500
computermoney = 500
pool = 0
bettingRound = 1
i = 0
play = str(input("Would you like to play? (Type 'Y'(Yes) or 'N'(No)) : "))
print(" --------------------------------------- ")
while i == 0:
    if play == "Y":
        rules = input("Would you like to read the rules? (Type 'Y' or 'N') : ")
        print(" --------------------------------------- ")
        if rules == "Y":
            #Rule book
            print("You will be playing a simplified version of Texas hold 'em Poker.")
            print("You and the computer will be dealt 2 cards, and then 5 community")
            print("cards will be shown in 3 stages so that you and the computer may ")
            print("use them to form the best poker hand. To begin the game, 3 of the  ")
            print("community cards are shown and both players must bet at least $50.   ")
            print("Afterwards, you may 'Raise' the bet by increasing the amount of ")
            print("money in the pool. If your opponent 'Raises' you must 'Match' the  ")
            print("amount bet, or 'Fold' where you give up the money you had already ")
            print("bet. If neither of you wish to 'Raise' you may 'Check' the next")
            print("community card. After the card has been revealed, the next round of")
            print("betting begins. This continues until all 5 cards have been shown.")
            print("The program will determine your best possible hand at the end, but")
            print("the ranking of each poker hand is shown below for your reference.")
            print(" --------------------------------------- ")
            print('Royal flush (Best hand) Must be A-K-Q-J-10 with the same suit')
            print('Straight flush (5 consecutive numbers with the same suit)')
            print('Four of a kind')
            print('Full house (3 of a kind and a different pair Ex: 3-3-3-2-2)')
            print('Flush (5 cards with the same suit)')
            print('Straight (5 consecutive numbers Ex: 2-3-4-5-6)')
            print('Three of a kind')
            print('Two pair')
            print('One pair')
            print('High card (Worst hand)' )
            print(" --------------------------------------- ")
            print("Important notes: Each poker hand is made of 5 cards.")
            print("Ace can either be the lowest card or the highest.")
            print("You do not have to use the 2 cards dealt to you.")
            print("To simplify the game, there will be no tie breakers.")
            print("Ex: A pair of Kings is not better than a pair of Twos.")
            print("This would result in a tie, and the pool would be split")
            print(" --------------------------------------- ")
        else:
            print ("You are now going to play Texas Hold'em.")
            print ("You will start off with $500 Good luck") 
            print(" --------------------------------------- ")
            print(" --------------------------------------- ")

            while playermoney > 0:
                #Next 3 while loops choose cards for everyone
                while playercards < 2:
                    hand[playercards] = random.choice (gameDeck)
                    gameDeck.remove(hand[playercards])
                    playercards +=1
                while tablecards < 5:
                    table[tablecards] = random.choice (gameDeck)
                    gameDeck.remove(table[tablecards])
                    tablecards +=1
                while computercards < 2:
                    cC[computercards] = random.choice (gameDeck)
                    gameDeck.remove(cC[computercards])
                    computercards +=1    
                #start betting 
                while bettingRound < 5:
                    fold = False
                    #first round, must bet $50
                    if bettingRound == 1 and (computermoney>50 and playermoney >50):
                        computerbet = 50
                        bet = 50
                    #if not first round, choose other bet
                    elif computermoney>0 and playermoney >0:
                        choice = input("Would you like to 'Raise' , 'Fold' , or 'Check'? (R/F/C): ")
                        if choice == 'R':
                            bet = int(input(" How much money would you like to bet? : $ "))
                            if bet > playermoney or bet < 0:
                                while bet > playermoney or bet < 0:
                                    print ("Invalde amount you can not bet what you don't have")
                                    bet = int(input(" How much money would you like to bet? : $"))
                            computerbet = computerChoice(computermoney,bet,playermoney)
                        elif choice == 'F':
                            computermoney = computermoney + pool
                            print("computer money $" + str(computermoney))
                            print("Player money $" + str(playermoney))
                            bet = -1
                        else:
                            bet = 0
                            computerbet = computerChoice(computermoney,0,playermoney)
                    else:
                        print('Someone does not have enough money to play. Please close the program to reset amounts.')
                        break;
                    if computerbet < 0:
                        print("The computer 'Folds'")
                        playermoney = playermoney + pool
                        print("computer money $" + str(computermoney))
                        print("Player money $" + str(playermoney))
                        break;
                    elif bet < 0:
                        break;
                    while computerbet != bet:
                        if computerbet < 0:
                            print("The computer 'Folds'")
                            playermoney = playermoney + pool
                            print("computer money $" + str(computermoney))
                            print("Player money $" + str(playermoney))
                            fold = True
                            break;
                        elif bet <0:
                            fold = True
                            break;
                       #print cards
                        print ("The computer bet $" + str(computerbet))
                        choice = input("Would you like to 'Raise' , 'Fold' , or 'Match'? (R/F/M): ")
                        if choice == 'R':
                            bet = int(input(" How much money would you like to bet? : $ "))
                            computerbet = computerChoice(computermoney,bet,playermoney)
                        elif choice == 'F':
                            fold = True
                            computermoney = computermoney + pool
                            print("computer money $" + str(computermoney))
                            print("Player money $" + str(playermoney))
                            bet = -1
                        else:
                            bet = computerbet
                    if fold:
                        break;
                    computermoney = computermoney - computerbet
                    playermoney = playermoney - bet
                    print ("The computer bet $" + str(computerbet))
                    pool = pool+bet + computerbet
                    print ("---------------------")
                    print ("The pool of money is $" + str(pool))
                    print ("---------------------")        
                    print ("    Here is your hand")
                    print(show_cards(hand)[0] + ' | ' + show_cards(hand)[1])
                    print (" ------------------ ")
                    print ("    Table cards")
                    if bettingRound == 1:
                        print(show_cards(table)[0])
                        print(show_cards(table)[1])
                        print(show_cards(table)[2])
                        print (" ------------------ ")
                    elif bettingRound == 2:
                        print(show_cards(table)[0])
                        print(show_cards(table)[1])
                        print(show_cards(table)[2])
                        print(show_cards(table)[3])
                        print (" ------------------ ")
                    elif bettingRound == 3:
                        print(show_cards(table)[0])
                        print(show_cards(table)[1])
                        print(show_cards(table)[2])
                        print(show_cards(table)[3])
                        print(show_cards(table)[4])
                        print (" ------------------ ")
                    #last round of betting, important stuff happens
                    elif bettingRound == 4:
                        #print all cards
                        print(show_cards(table)[0])
                        print(show_cards(table)[1])
                        print(show_cards(table)[2])
                        print(show_cards(table)[3])
                        print(show_cards(table)[4])
                        print (" ------------------ ")
                        print ("    AI cards")
                        print(show_cards(cC)[0] + ' | ' + show_cards(cC)[1])
                        print (" ------------------ ")
                        playCards = hand + table
                        pbest_hand = get_best_hand(playCards)
                        compCards = cC+table
                        cbest_hand = get_best_hand(compCards)
                        #prints computer best hand
                        print()
                        print("Here is the AI's best hand")
                        print()
                        j=0
                        while j < len(cbest_hand):
                            print(show_cards(cbest_hand)[j])
                            j+=1
                        print (" ------------------ ")
                        print(evaluate_hand(cbest_hand))
                        #prints best your best hand
                        print (" ------------------ ")
                        print("Here is your best hand")
                        print()
                        j=0
                        while j < len(pbest_hand):
                            print(show_cards(pbest_hand)[j])
                            j+=1
                        print (" ------------------ ")
                        print(evaluate_hand(pbest_hand))
                        print (" ------------------ ")
                        print()
                        #finds the winner
                        allPlayerCards = [cbest_hand,pbest_hand]
                        playersList = [evaluate_hand(cbest_hand), evaluate_hand(pbest_hand)]
                        print()
                        print(findWinner(allPlayerCards,playersList))
                        if (findWinner(allPlayerCards,playersList)) == "Player Wins":
                            playermoney = playermoney + pool
                            print("computer money $" + str(computermoney))
                            print("Player money $" + str(playermoney))
                        elif (findWinner(allPlayerCards,playersList)) == "Computer Wins":
                            computermoney = computermoney + pool
                            print("computer money $" + str(computermoney))
                            print("Player money $" + str(playermoney))
                        else:
                            playermoney = playermoney + int(pool / 2)
                            computermoney = computermoney + int(pool / 2)
                            print("computer money $" + str(computermoney))
                            print("Player money $" + str(playermoney))
                    bettingRound+=1
                #reset counters and stuff
                bettingRound = 1
                pool = 0
                computercards = 0
                playercards = 0
                tablecards = 0
                table = ["","","","",""]
                hand = ["",""]
                cC = ["",""]
                gameDeck = list(deck)
                #continue option
                if playermoney > 0:
                    continuePlaying =input("Would you like to continue? (Type 'Y' or 'N') : ")
                    if continuePlaying == 'N':
                        play = "N"
                        playermoney = -1
            #run out of money
            if playermoney == 0:
                print ("You lost all of your money tuff luck")
    #leaveing the table
    else:
        print("See you soon")
        i = 1
        


