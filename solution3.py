# author: shikhasingh407

import itertools
from handeval import Evaluate  # Module I created to calculate a rank for a given hand


def getBestHand(cards):
    """
    Returns the best hand of five cards, from a larger list of cards.
    If ranks are alphabetical (e.g., A for ace), it will convert the rank to a number,
    using the method: convertFacesToInt
    ex.
    getBestHand(['7C', '7S', '2H', '3C', 'AC', 'AD', '5S'])
    returns
    Best Hand: ['5S', '7C', '7S', '14C', '14D']
    """
    # All combinations of 5 cards from the larger list
    allHandCombos = itertools.combinations(cards, 5)
    maxValue = 0
    bestHand = []
    e = Evaluate()
    # Iterating through all the handRanks
    bestHands = {x: [] for x in range(9)}
    for combo in allHandCombos:
        hand = list(combo)
        handValue = e.handValue(hand)
        if handValue >= maxValue:
            # Stronger or equal hand has been found
            maxValue = handValue
            bestHands[handValue].append(hand)# Store hand in dictionary
    maxHandIdx = max(k for k, v in bestHands.items() if len(bestHands[k])>0)
    rankSum, maxSum = 0, 0
    # The strongest hand type out of the combinations has been found
    for hand in bestHands[maxHandIdx]:
        # Iterate through hands of this strongest type
        ranks = e.convertFacesToInt([x[0] for x in hand])
        rankSum = sum(ranks)
        if rankSum > maxSum:
            maxSum = rankSum
            # Choose hand with highest ranking cards
            bestHand = hand
    return bestHand


if __name__ == '__main__':
    print("Best hand: ", getBestHand(["3H", "6S", "3S", "3D", "5S", "8D", "2H"]))
