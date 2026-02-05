import unittest
import rps

class TestRPS(unittest.TestCase):

    def setUp(self):
        """Reset the global score before each test."""
        rps.score = 0

    def test_get_result_draw(self):
        """Test cases where the game results in a draw."""
        # Rock vs Rock
        self.assertEqual(rps.get_result('바위', '바위'), '비겼다...')
        self.assertEqual(rps.score, 0) # Score should not change on a draw

        # Scissors vs Scissors
        self.assertEqual(rps.get_result('가위', '가위'), '비겼다...')
        self.assertEqual(rps.score, 0) # Score should still be 0

        # Paper vs Paper
        self.assertEqual(rps.get_result('보', '보'), '비겼다...')
        self.assertEqual(rps.score, 0) # Score should still be 0

    def test_get_result_user_win(self):
        """Test cases where the user wins the round."""
        # User Rock vs Computer Scissors
        self.assertEqual(rps.get_result('바위', '가위'), '이겼다!')
        self.assertEqual(rps.score, 1) # Score should increase by 1

        # User Scissors vs Computer Paper
        self.setUp() # Reset score for next test case
        self.assertEqual(rps.get_result('가위', '보'), '이겼다!')
        self.assertEqual(rps.score, 1)

        # User Paper vs Computer Rock
        self.setUp() # Reset score
        self.assertEqual(rps.get_result('보', '바위'), '이겼다!')
        self.assertEqual(rps.score, 1)

    def test_get_result_user_lose(self):
        """Test cases where the user loses the round."""
        # User Rock vs Computer Paper
        self.assertEqual(rps.get_result('바위', '보'), '졌다ㅠㅠ')
        self.assertEqual(rps.score, 0) # Score should not change on a loss

        # User Scissors vs Computer Rock
        self.setUp() # Reset score
        self.assertEqual(rps.get_result('가위', '바위'), '졌다ㅠㅠ')
        self.assertEqual(rps.score, 0)

        # User Paper vs Computer Scissors
        self.setUp() # Reset score
        self.assertEqual(rps.get_result('보', '가위'), '졌다ㅠㅠ')
        self.assertEqual(rps.score, 0)

if __name__ == '__main__':
    unittest.main()
