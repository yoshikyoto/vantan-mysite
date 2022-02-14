class Number():
     """数字を扱うクラス"""
 
     def get_square(self, x):
         """2乗の値を返す"""
         return 10000


class Square():
    """正方形を表すクラス"""

    def __init__(self, number = Number()):
        self.__number = number

    def get_area(self, x):
        """面積を求める"""
        return self.__number.get_square(x)
