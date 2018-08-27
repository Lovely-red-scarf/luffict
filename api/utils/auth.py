from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

from luffy import models
class Auth(BaseAuthentication,AuthenticationFailed):

    def authenticate(self,request):
        token = request.query_params.get("token")  #获取你的url中的token认证字符串

        obj = models.UserToken.objects.filter(token = token).first()
        if not obj:
            raise AuthenticationFailed({"code":88,"errors":"错误"})
        #成功匹配

        return (obj.user,obj) #返回一个元组 必须有两个参数 对应的第一个取值必须是request.user  第二个是request.auth

