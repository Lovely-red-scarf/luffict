
class BaseResponse(object):

    def __inie__(self):
        self.code = 1000
        self.data = None
        self.errors = None
    @property
    def __dict__(self):  # __dict__把你的内容以字典的形式返回出去
        return self.__dict__