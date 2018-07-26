# author: shikhasingh407
from handeval import Evaluate  # Module I created to calculate a rank for a given hand


# Checks if the hand is valid or not
def isValidHand(hand):
    # Check if hand has 5 distinct cards
    if len(set(hand)) != 5:
        return False
    else:
        return True


def compareTwoHands(hand1, hand2):
    e = Evaluate()

    # .split(',')
    hand1Rank = e.handValue(hand1)
    hand2Rank = e.handValue(hand2)

    # Determine which hand has a higher rank
    if hand2Rank > hand1Rank:
        return -1
    elif hand1Rank > hand2Rank:
        return 1
    # if handRanks are equal, return -1, 0, 1 values to help sorting
    elif hand1Rank == hand2Rank:
        if (e.tieBreaker(hand1, hand2, hand1Rank)) != 'Draw':
            hand = e.tieBreaker(hand1, hand2, hand1Rank)
            if hand == hand1:
                return 1
            else:
                return -1
        return 0


def cmp_to_key(compareTwoHands):
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj

        def __lt__(self, other):
            return compareTwoHands(self.obj, other.obj) < 0

        def __gt__(self, other):
            return compareTwoHands(self.obj, other.obj) > 0

        def __eq__(self, other):
            return compareTwoHands(self.obj, other.obj) == 0

        def __le__(self, other):
            return compareTwoHands(self.obj, other.obj) <= 0

        def __ge__(self, other):
            return compareTwoHands(self.obj, other.obj) >= 0

        def __ne__(self, other):
            return compareTwoHands(self.obj, other.obj) != 0

    return K


def findWinner(listOfHands):
    # Turn hand strings into lists
    # h1 = hand1.split(',')
    # h2 = hand2.split(',')
    e = Evaluate()
    for hand in listOfHands:
        if not isValidHand(hand):
            return "ERROR: %s is not a valid hand" % hand

    x = (sorted(listOfHands, key=cmp_to_key(compareTwoHands), reverse=True))
    return x[0]


if __name__ == '__main__':
    # Assuming valid cases only.
    print("The winner of the game is with cards: ", findWinner([('3H', '3S', 'QD', '3D', '4S'),
                                                                ('3H', '8S', 'QD', 'AH', '4D'),
                                                                ('JH', 'JS', 'QD', 'QH', 'JD')]))
