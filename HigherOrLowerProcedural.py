import random

# constants
SUIT_TUPLE =  ('Spades','Hearts','Clubs','Diamonds')
RANK_TUPLE = ('Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King')

NCARDS = 8

# pass deck as a parameter and return a random card

def get_card(deckListIn):
    thisCard = deckListIn.pop()
    return thisCard

# pass in a deck and this function returns a shuffled copy of the deck
def shuffle(deckListIn):
    deckListOut = deckListIn.copy()
    random.shuffle(deckListOut)
    return deckListOut

def main():
    pass

if __name__ == main:
    main()