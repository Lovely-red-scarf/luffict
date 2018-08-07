class BaseResponse(object):

    def __init__(self):
        self.code = 1000
        self.data = None
        self.errors = None
    @property
    def dict(self):   # 设置一个dict的函数让它返回的是你的__dict__这个方法
        return self.__dict__