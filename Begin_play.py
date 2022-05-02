import random


class blackjack:
    def __init__(self, hand):
        self.hand = hand

    def hit(self, deck):
        x=random.randint(0,3)
        y=random.randint(0,len(deck[x]))
        z = (deck[x][y - 1])
        self.hand.append(z)
        deck[x].pop(y-1)


    def Add_Cards (self):
        total = 0
        for i in range (len(self.hand)):
            total += self.hand[i]
        return(total)


