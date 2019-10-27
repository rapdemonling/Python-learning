__author__ = "George Ling"


class LingError(Exception):
    def __init__(self, msg):
        self.message = msg
    # def __str__(self):
    #     return 'sdfsf'
try:
    raise LingError('数据库连不上')
except LingError as e:
    print(e)