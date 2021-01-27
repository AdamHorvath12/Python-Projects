import random

dealer_cards = []
user_cards = []
sum_of_dealer_cards = []
sum_of_user_cards = []
action = ""

while len(dealer_cards) < 2 or sum_of_dealer_cards < 16:
    dealer_cards.append(random.randint(1,11))
    sum_of_dealer_cards = sum(dealer_cards)

while len(user_cards) < 2 or sum_of_user_cards < 16:
    user_cards.append(random.randint(1,11))
    sum_of_user_cards = sum(user_cards)
    print('User score: ', sum_of_user_cards)
    # if sum_of_user_cards == 21 and len(user_cards) == 2:
    #     print('You have Black Jack! You WIN!')
    # elif sum_of_user_cards == 21:
    #     print('You have 21!')
    if sum_of_user_cards >= 16:
        while action != "STAY" and sum_of_user_cards < 21:
            action = str(input('Do you want to stay or hit?')).upper()
            if action == "HIT":
                user_cards.append(random.randint(1,11))
                sum_of_user_cards = sum(user_cards)
                print('User score: ', sum_of_user_cards)

if sum_of_user_cards > 21:
    print('You are BUSTED! Dealer wins!, total score: ',sum_of_user_cards)
elif sum_of_user_cards == 21 and len(user_cards) == 2:
    print('You have Black Jack! You WIN!')
elif sum_of_dealer_cards > 21:
    print('Dealer is BUSTED! User wins!, total score: ',sum_of_user_cards)
elif sum_of_user_cards > sum_of_dealer_cards:
    print('You WIN! - Your final score is: ', sum_of_user_cards,'You have these cards:', user_cards, 'Final score of the dealer: ', sum_of_dealer_cards)
else:
    print('Dealer wins! Final score of the dealer: ', sum_of_dealer_cards, 'Final score of the user: ',sum_of_user_cards)  


