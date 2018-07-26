# author: shikhasingh407
import math  # Public Library imported for calcs
import collections  # Public Lib imported for counting occurences in a list


class Evaluate:
    def __init__(self):
        # Initialize empty hand variables to be set later
        self.h1 = ""
        self.h2 = ""
        self.category = ""

    def handValue(self, hand):
        # Get a list of just ranks as integers
        ranks = self.convertFacesToInt([x[0] for x in hand])
        # Get a list of just suits
        suits = [x[1] for x in hand]
        # Get occurences of ranks for later comparison
        count = collections.Counter(ranks)

        # Return value of 9 for a straight flush
        if self.isStraightFlush(ranks, suits):
            self.category = "Straight flush"
            return 9
        # Return value of 8 if hand is 4 of a kind
        elif self.checkDupRanks(count, 4):
            self.category = "Four of a kind"
            return 8
        # Return value of 7 if hand is full house
        elif self.checkDupRanks(count, 3) and self.checkDupRanks(count, 2):
            self.category = "Full house"
            return 7
        # Return value of 6 if hand is a flush
        elif self.isFlush(suits):
            self.category = "Flush"
            return 6
        # Return value of 5 is hand is a straight
        elif self.isStraight(ranks):
            self.category = "Straight"
            return 5
        # Return value of 4 if hand is 3 of a kind
        elif self.checkDupRanks(count, 3):
            self.category = "Three of a kind"
            return 4
        # Return value of 3 if hand is two pairs
        elif self.isTwoPair(count):
            self.category = "Two pair"
            return 3
        # Return value of 2 if hand is a pair
        elif self.checkDupRanks(count, 2):
            self.category = "Pair"
            return 2
        # Default return value of 1 for high card
        else:
            self.category = "high card"
            return 1

    def isValidHand(hand):
        # Check if hand has 5 distinct cards
        if len(set(hand)) != 5:
            return False
        else:
            return True

    # Convert ranks list from strings to integers
    def convertFacesToInt(self, ranks):
        # Dict of face card values
        faceCardValues = {
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14
        }

        # For all ranks in list, if is a face card, convert to number value
        # else add number to list as int and return new list
        intRanks = []
        for card in ranks:
            if card in faceCardValues:
                intRanks.append(int(faceCardValues[card]))
            else:
                intRanks.append(int(card))
        return intRanks



    # Check if hand is a straight and a fluse
    # Return true if both checks are true
    def isStraightFlush(self, ranks, suits):
        if self.isFlush(suits) and self.isStraight(ranks):
            return True
        else:
            return False

    # Return true if all suits are the same
    def isFlush(self, suits):
        if len(set(suits)) == 1:
            return True
        else:
            return False

    # Check if hand is a straight
    def isStraight(self, ranks):
        # Sort ranks numerically
        ranks.sort()

        # if there are < 5 distinct ranks, it can't be a straight
        if len(set(ranks)) < 5:
            return False
        # if highest rank - lowest rank is 4, must be a straight
        elif ranks[4] - ranks[0] == 4:
            return True
        # if Above is false and there's an Ace in the hand, check for straight with Ace as a low card
        elif 14 in ranks:
            # iterate through list to replace any Ace(14) ranks with Ace(1)
            for i, d in enumerate(ranks):
                if d is 14:
                    ranks[i] = 1
            # Run check again with ace as low card
            return self.isStraight(ranks)
        else:
            return False

    # General function to check if hand has n number of duplicate ranks
    # Used to determine 4 of a kind, 3 of a kind, and a pair.
    # Takes in a dict that stores values of occurences of ranks
    def checkDupRanks(self, ranks, n):
        # Check if any ranks values equal n (ie. duplicates)
        if n in ranks.values():
            return True
        else:
            return False

    # Check if there are two pairs
    def isTwoPair(self, ranks):
        # Check if a counter of the counter passed in equals 2
        # meaning there are two pairs
        if 2 in collections.Counter(ranks.values()).values():
            return True
        else:
            return False

    # Check which hand has the highest card that isn't of a duplicate rank
    def highCard(self, h1, h2):
        # create list of keys that have a value of 1 (ie, card ranks that aren't duplicates)
        h1 = [k for k, v in collections.Counter(h1).items() if v == 1]
        h2 = [k for k, v in collections.Counter(h2).items() if v == 1]

        h1.sort()
        h2.sort()

        # Iterate through the list backwards (ie. highest to lowest)
        # comparing an list item to its counterpart in the other list
        # Return the hand that has the higher card
        for n in range(len(h1) - 1, -1, -1):
            if h1[n] > h2[n]:
                return self.h1
            elif h2[n] > h1[n]:
                return self.h2
            elif h1[n] == h2[n] and n <= 0:
                return "Draw"

    # Check what hand has the highest duplicate ranks
    def highestDup(self, h1, h2, n):
        # Reverse key and values in counter dict
        count1 = {v: k for k, v in collections.Counter(h1).items()}
        count2 = {v: k for k, v in collections.Counter(h2).items()}
        # Compare rank cards where n is the number of dups (ie. 3 of a kind)
        # Return the hand that has the higher rank
        if count1[n] > count2[n]:
            return self.h1
        elif count2[n] > count1[n]:
            return self.h2
        else:
            return "Draw"

    def highestPair(self, h1, h2, n):
        # create list of keys that have a value of 2 (ie, card ranks that are pairs)
        dups1 = [k for k, v in collections.Counter(h1).items() if v == 2]
        dups2 = [k for k, v in collections.Counter(h2).items() if v == 2]

        # If there are 2 pairs, check if highest pairs are not equal and return hand that has highest pair
        if n == 2:
            if dups1[-1] > dups2[-1]:
                return self.h1
            elif dups1[-1] < dups2[-1]:
                return self.h2
            # If highest pairs are equal, look at next highest pair
            else:
                if dups1[0] > dups2[0]:
                    return self.h1
                elif dups1[0] < dups2[0]:
                    return self.h2
                # If next highest pair are equal, check which side card is higher
                else:
                    return self.highCard(h1, h2)
        # If only 1 pair, return the hand of the pair which is higher
        elif n == 1:
            if dups1[0] > dups2[0]:
                return self.h1
            elif dups1[0] < dups2[0]:
                return self.h2
            # If both pairs are equal, return the hand with the highest side card
            else:
                return self.highCard(h1, h2)

    def tieBreaker(self, h1, h2, rank):
        self.h1 = h1
        self.h2 = h2
        # Player 1 card ranks
        r1 = self.convertFacesToInt([x[0] for x in h1])
        # Player 2 card ranks
        r2 = self.convertFacesToInt([x[0] for x in h2])

        if rank == 9 or rank == 6 or rank == 5 or rank == 1:
            # If straight flush, flush, or straight, look for highest card
            return self.highCard(r1, r2)
        elif rank == 8:
            # If 4 of a kind, determine which 4 of a kind is higher
            return self.highestDup(r1, r2, 4)
        elif rank == 7 or rank == 4:
            # If full house, or 3 of a kind, check which hand has the higher 3 of a kind
            return self.highestDup(r1, r2, 3)
        elif rank == 3:
            # If 2 pair, check which pair is higher
            return self.highestPair(r1, r2, 2)
        elif rank == 2:
            # If 1 pair, check which pair is higher
            return self.highestPair(r1, r2, 1)
        else:
            # If high card, check which hand has the higher card
            return self.highCard(r1, r2)

    def __hash__(self) -> int:
        return super().__hash__()
