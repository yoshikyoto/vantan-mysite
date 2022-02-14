from django.test import TestCase
from unittest.mock import MagicMock
from polls.square import Square
from django.urls import reverse

class SquareTest(TestCase):

    def test_get_area(self):
        number_mock = MagicMock()
        number_mock.get_square.return_value = 1

        square = Square(number = number_mock)

        x = 1
        expected = 1
        actual = square.get_area(x)
        self.assertEqual(actual, expected)
