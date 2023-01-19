import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):

    def setUp(self):
        self.scores = [5,2,6,10]
        self.scores_tied = [2,3,3,4]

    # Test latest score (the last thing in the list)
    def test_return_latest_score(self):
        self.assertEqual(10, latest(self.scores))

    # Test personal best (the highest score in the list)
    def test_high_score_is_10(self):
        self.assertEqual(10, personal_best(self.scores))

    # Test top three from list of scores
    def test_top_three_scores(self):
        self.assertEqual([5,6,10], personal_top_three(self.scores))

    # Test ordered from highest tp lowest
    def test_ordered_highest_to_lowest(self):
        self.assertEqual([10,6,5,2], (sort_high_to_low(self.scores)))

    # Test top three when there is a tie
    def test_return_top_three_when_there_is_a_tie(self):
        pass

    # Test top three when there are less than three

    # Test top three when there is only one
    
