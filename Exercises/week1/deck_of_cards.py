import numpy.random as rn


deck = [(i,letter) for i in range(1,14) for letter in ['H','C','D','S']]


rn.shuffle(deck)
s_deck = deck[:13]



Clubs = [card for card in s_deck if card[1] == 'C']
Clubs.sort()

Hearts = [card for card in s_deck if card[1] == 'H']
Hearts.sort()

Diamonds = [card for card in s_deck if card[1] == 'D']
Diamonds.sort()

Spades = [card for card in s_deck if card[1] == 'S']
Spades.sort()


hand = Clubs + Hearts + Diamonds + Spades

print(hand)
