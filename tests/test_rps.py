import unittest
import sys
import os

# Add src directory to path so we can import from chanwookim_rps
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from chanwookim_rps import get_result, score

class TestRPS(unittest.TestCase):

    def setUp(self):
        """Reset the global score before each test."""
        import chanwookim_rps
        chanwookim_rps.score = 0

    def test_get_result_draw(self):
        """Test cases where the game results in a draw."""
        # Rock vs Rock
        self.assertEqual(get_result('rock', 'rock'), 'Draw')

        # Scissors vs Scissors
        self.assertEqual(get_result('scissors', 'scissors'), 'Draw')

        # Paper vs Paper
        self.assertEqual(get_result('paper', 'paper'), 'Draw')

    def test_get_result_user_win(self):
        """Test cases where the user wins the round."""
        import chanwookim_rps

        # User Rock vs Computer Scissors
        self.assertEqual(get_result('rock', 'scissors'), 'You win!')
        self.assertEqual(chanwookim_rps.score, 1)

        # User Scissors vs Computer Paper
        self.setUp()
        self.assertEqual(get_result('scissors', 'paper'), 'You win!')
        self.assertEqual(chanwookim_rps.score, 1)

        # User Paper vs Computer Rock
        self.setUp()
        self.assertEqual(get_result('paper', 'rock'), 'You win!')
        self.assertEqual(chanwookim_rps.score, 1)

    def test_get_result_user_lose(self):
        """Test cases where the user loses the round."""
        import chanwookim_rps

        # User Rock vs Computer Paper
        self.assertEqual(get_result('rock', 'paper'), 'You lose')
        self.assertEqual(chanwookim_rps.score, 0)

        # User Scissors vs Computer Rock
        self.setUp()
        self.assertEqual(get_result('scissors', 'rock'), 'You lose')
        self.assertEqual(chanwookim_rps.score, 0)

        # User Paper vs Computer Scissors
        self.setUp()
        self.assertEqual(get_result('paper', 'scissors'), 'You lose')
        self.assertEqual(chanwookim_rps.score, 0)

if __name__ == '__main__':
    unittest.main()

