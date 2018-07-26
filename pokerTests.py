import unittest  # unittest library
import collections  # Lib imported for counting occurences in a list
from handeval import Evaluate  # Module I made for calculating hand ranks


class PokerTests(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(PokerTests, self).__init__(*args, **kwargs)
        self.e = Evaluate()

    def testHandValueReturnsValue(self):
        # Ensure that handValue does return a value (ie. a 2 for a pair)
        hand = '5C 8H QC JS 8D'
        self.assertEqual(self.e.handValue(hand.split()), 2)

    def testStraightFlush(self):
        # Ensure the isStraightFlush function calcs the hand correctly
        hand = '5H 6H 9H 8H 7H'.split()
        ranks = self.e.convertFacesToInt([x[0] for x in hand])
        suits = [x[1] for x in hand]
        # Should return true as this hand is a straight flush
        self.assertTrue(self.e.isStraightFlush(ranks, suits))

        # Remove straight possibility from hand
        ranks[1] = 2
        # Should return false as this isn't a straight flush any longer
        self.assertFalse(self.e.isStraightFlush(ranks, suits))

    def testFlush(self):
        suits = [x[1] for x in '5H 6H 9H 8H 7H'.split()]
        # Should return true as this hand is a flush
        self.assertTrue(self.e.isFlush(suits))

        # Remove flush possibility
        suits[0] = 'C'
        # Should return false as this isn't a flush any longer
        self.assertFalse(self.e.isFlush(suits))

    def testStraight(self):
        ranks = self.e.convertFacesToInt([x[0] for x in '5H 6C 9S 8D 7H'.split()])
        # Should return true as this hand is a straight
        self.assertTrue(self.e.isStraight(ranks))

        # Remove Straight possibility
        ranks[0] = 12
        # hand isn't a straight any longer so this should return false
        self.assertFalse(self.e.isStraight(ranks))

    def testCheckDupRanks(self):
        ranks = self.e.convertFacesToInt([x[0] for x in '5H QC 9S 9D 6H'.split()])
        count = collections.Counter(ranks)

        # Check if there is a pair, should return true
        self.assertTrue(self.e.checkDupRanks(count, 2))

        ranks[2] = 7
        count = collections.Counter(ranks)
        # Should return false as there is no longer a pair
        self.assertFalse(self.e.checkDupRanks(count, 2))

    def testTwoPair(self):
        ranks = self.e.convertFacesToInt([x[0] for x in '5H 6C 9S 9D 6H'.split()])
        count = collections.Counter(ranks)

        # Check if there's 2 pairs, should return true
        self.assertTrue(self.e.isTwoPair(count))

        ranks[2] = 7
        count = collections.Counter(ranks)
        # Should return false as now there's only 1 pair
        self.assertFalse(self.e.isTwoPair(count))

    def testHighCard(self):
        # This checks which hand has the highest card
        self.assertEquals(self.e.tieBreaker('5H TC QS 9D 6H'.split(), '5S AC QH 4C TD'.split(), 1),
                          '5S AC QH 4C TD'.split())

    def testHighestDup(self):
        # This tests which hand has the highest 3 of a kind
        self.assertEquals(self.e.tieBreaker('5H TC TS 9D TH'.split(), 'QS AC QH QC TD'.split(), 4),
                          'QS AC QH QC TD'.split())

    def testHighestPair(self):
        # This tests which hand has the highest 2 pair, but goes deeper as both hands have the same 2 pairs,
        # so it resorts to the high card
        self.assertEquals(self.e.tieBreaker('AH QC QS AD 9H'.split(), 'AS AC QH QC TD'.split(), 2),
                          'AS AC QH QC TD'.split())

        # This should return a Draw
        self.assertEquals(self.e.tieBreaker('AH QC QS AD TH'.split(), 'AS AC QH QC TD'.split(), 2), 'Draw')


if __name__ == '__main__':
    unittest.main()
