from django.test import TestCase
from polls.square import Square


class SquareTest(TestCase):

    def test_get_area(self):
        square = Square()

        x = 1
        expected = 1
        actual = square.get_area(x)
        self.assertEqual(actual, expected)
        
        x = 2
        expected = 4
        actual = square.get_area(x)
        self.assertEqual(actual, expected)
