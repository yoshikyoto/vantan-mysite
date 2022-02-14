from django.test import TestCase
from django.utils import timezone
from polls.models import Question


class RequestTest(TestCase):
    """実際に HTTP リクエストを送ると、どういう結果が帰ってくるかテスト"""

    def test_no_questions(self):
        """アンケートが無いときの index ページのテスト"""
        # self.client というのがある
        # 実際に GET リクエスト送って、responseを取得する
        response = self.client.get('/polls/')

        # レスポンスのステータスコードが 200 OK であることを確認する
        self.assertEqual(response.status_code, 200)

        # ページに表示される文字列をテストしている
        self.assertContains(response, "No polls are available.")

    def test_questions_exists(self):
        """アンケートがすでに投稿されている場合のテスト"""
        # 質問を作成する
        question = Question(
            question_text="Todays lunch?",
            pub_date=timezone.now()
        )
        question.save()

        response = self.client.get('/polls/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Todays lunch?")




from unittest.mock import MagicMock
from polls.square import Square


class SquareTest(TestCase):

    def test_get_area(self):
        number_mock = MagicMock()
        number_mock.get_square.return_value = 1

        square = Square(number = number_mock)

        x = 1
        expected = 1
        actual = square.get_area(x)
        self.assertEqual(actual, expected)