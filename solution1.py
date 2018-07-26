# author: shikhasingh407
from handeval import Evaluate  # Module created to calculate a rank for a given hand


# Checks if the hand is valid or not
def isValidHand(hand):
    # Check if hand has 5 distinct cards
    if len(set(hand)) != 5:
        return False
    else:
        return True


# returns the category of a hand
def handCategory(hand):
    e = Evaluate()
    if not isValidHand(hand):
        return "ERROR: %s is not a valid hand" % hand

    e.handValue(hand)
    return e.category


if __name__ == '__main__':
    print(handCategory(["4H", "4K", "4S", "9C", "9H"]))
