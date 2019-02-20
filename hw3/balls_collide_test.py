from unittest import TestCase, main
from balls_collide import balls_collide


class Test_balls_collide(TestCase):
    def test_error(self):
        ball1 = (1.337, 5.71, 1, -3.12)
        ball2 = (1, -7, 2.0, 30.1)
        self.assertRaises(ValueError, balls_collide, ball1, ball2)
        ball1 = (544, 0, 1.0, 0.11)
        ball2 = (5, -4.8, 5.11, -1.012)
        self.assertRaises(ValueError, balls_collide, ball1, ball2)
        ball1 = (8.241, -78, 6.66, -37.1)
        ball2 = (4, 7.7, -5.19, -10)
        self.assertRaises(ValueError, balls_collide, ball1, ball2)

    def test_true(self):
        ball1 = (1, 2, 3, 0)
        ball2 = (1, 2, 3, 0)
        self.assertTrue(balls_collide(ball1, ball2))
        ball1 = (0, 0, 0, 4)
        ball2 = (0, 0, 0, 5)
        self.assertTrue(balls_collide(ball1, ball2))
        ball1 = (-3.1, 6, 13.3, 8)
        ball2 = (-8.7, 2, 4.8, 5)
        self.assertTrue(balls_collide(ball1, ball2))

    def test_false(self):
        ball1 = (4.0, -2.13, 5.12, 0)
        ball2 = (-59.1, 2.9, 3, 0)
        self.assertFalse(balls_collide(ball1, ball2))
        ball1 = (1, -1.1, -5.325, 3)
        ball2 = (6, 5.1, 3.11, 7)
        self.assertFalse(balls_collide(ball1, ball2))
        ball1 = (-7.8, 2, 6.13, 4.145)
        ball2 = (-4.71, 2, -1.01, 1.31)
        self.assertFalse(balls_collide(ball1, ball2))


main()
