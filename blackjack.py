from email.headerregistry import HeaderRegistry
import random

from Begin_play import blackjack


def blackjack_game():


    Clubs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Hearts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    Spades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    player_hand = []
    dealer_hand = []

    deck = [Clubs, Diamonds, Hearts, Spades]

    my_b = blackjack(player_hand)
    dealer_b = blackjack(dealer_hand)
    game_running = True
    player_turn = True
    dealer_turn = False
    player_win = False
    dealer_win = False


    my_b.hit(deck)
    my_b.hit(deck)
    if my_b.Add_Cards() == 21:
        print('BLACKJACK. YOU WIN')
    if my_b.Add_Cards() > 21:
        print(f"--------------------OOOOOOOF Your starting hand was {player_hand} That is over 21. How unlucky--------------------")
        print('AUTOMATIC LOSS')
        game_running = False
    dealer_b.hit(deck)
    print('------------WELCOME TO BLACKJACK. ARE YOU READY TO LOSE??????------------')
    print(f'The Dealer cards are: {dealer_hand}')
    dealer_b.hit(deck)
    

    while game_running == True:

        while player_turn == True:
            player_choice = input(f"Your current hand is {player_hand}. Your total is {my_b.Add_Cards()}.\nWould you like to 'hit' or 'hold' ? ")
            if player_choice == 'hit':
                my_b.hit(deck)
                if my_b.Add_Cards() > 21:
                    print(player_hand)
                    print(f"OOOOOOOF That is a loss! you have **{my_b.Add_Cards()}** which is over the limit of 21!")
                    dealer_win = True
                    dealer_turn = True
                    break
            elif player_choice == 'hold':
                dealer_turn = True
                break
            else:
                print("Sorry that is not an option. Please type 'hit' or 'hold'")

        while dealer_turn == True:
            if dealer_win == True:
                break
            #This code below says that if the dealer has high card value but still under 21
            elif dealer_b.Add_Cards() > my_b.Add_Cards() and dealer_b.Add_Cards() <= 21:
                print(dealer_b.Add_Cards())
                print(f'The Dealer has more cards than you {dealer_hand}')
                break
            #This code below says that if the dealer has higher card value but over 21
            elif dealer_b.Add_Cards() > my_b.Add_Cards() and dealer_b.Add_Cards() > 21:
                print(f'The Dealer has {dealer_b.Add_Cards()}. They went over 21 and has LOST')
                player_win = True
                break
            #This code below says if the dealer has less card value than you
            elif dealer_b.Add_Cards() <= my_b.Add_Cards():
                dealer_b.hit(deck)
                print(f'The Dealer cards are: {dealer_hand}')
            elif dealer_b.Add_Cards() == my_b.Add_Cards() and dealer_b.Add_Cards() == 21:
                print("Wow. Both the player and the dealer have 21. Guess this is a tie. No one wins or loses.")
                break
        break


    if dealer_win == True:
        print("The house has won")
    elif player_win == True:
        print("The player has won")


    again = input("Would you like to play again? type 'y' or 'n'")
    if again == 'y':
        blackjack_game()

blackjack_game()
