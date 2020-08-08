import unittest
from .Card_Game import Game

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.card = Game(4)

    def test_Condition1_WHEN_ALL_SAME(self):
        self.card.players = [['A', '7', 'J'], ['2', 'K', '6'],
                        ['6', '9', 'A'], ['5', '5', '5']]
        self.assertEqual(self.card.winner()+1, 4, "Should be Player 4")

    def test_Condition2_WHEN_SEQUENCE_IS_THERE(self):
        self.card.players = [['A', '3', '2'], ['2', 'K', '6'],
                        ['6', '9', 'A'], ['5', '5', '6']]
        self.assertEqual(self.card.winner()+1, 1, "Should be Player 1")


    def test_Condition3_WHEN_PAIRS_EQUAL(self):
        self.card.players = [['A', '4', '2'], ['K', 'K', '6'],
                        ['6', '9', 'A'], ['5', '9', '6']]
        self.assertEqual(self.card.winner()+1, 2, "Should be Player 2")


    def test_Condition4_MAXIMUM_SUM_CARDS(self):
        self.card.players = [['A', '4', '2'], ['K', '2', '6'],
                        ['6', '9', 'J'], ['5', '9', '6']]
        self.assertEqual(self.card.winner()+1, 3, "Should be Player 3")

    def test_Condition1_POSITIVE(self):
        player = ['A', 'A', 'A']
        self.assertTrue(self.card.condition1(player))

    def test_Condition1_NEGATIVE(self):
        player = ['A', '4', '2']
        self.assertFalse(self.card.condition1(player))

    def test_Condition2_POSITIVE(self):
        player = ['A', '2', '3']
        self.assertTrue(self.card.condition2(player))

    def test_Condition2_NEGATIVE(self):
        player = ['A', '4', '2']
        self.assertFalse(self.card.condition2(player))

    def test_Condition3_POSITIVE(self):
        player = ['A', 'A', '2']
        self.assertTrue(self.card.condition3(player))

    def test_Condition3_NEGATIVE(self):
        player = ['A', '3', '2']
        self.assertFalse(self.card.condition3(player))

if __name__ == '__main__':
    unittest.main()