from django.shortcuts import  render,redirect,HttpResponse


import uuid

from luffy import models
from api.utils import response

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from rest_framework.parsers import JSONParser  #解析器

from django.core.handlers.wsgi import WSGIRequest
class AuthView(ViewSetMixin,APIView):
    parser_classes = [JSONParser]


    def login(self,request,*args,**kwargs):
        reg = response.Response()

        user = request.data.get("user")
        pwd = request.data.get('pwd')

        user_obj = models.Account.objects.filter(username= user,password=pwd).first()

        token = request.data.get("token")

        token_obj = models.UserToken.objects.filter(token = token).first()
        if not user_obj:# 不存在
            reg.code = 88
            reg.errors = "用户名或密码错误"
            return Response(reg.dict)


        # 登陆成功
        # 生成一个随机字符串用来当作token然后给用户
        uid = str(uuid.uuid4())

        models.UserToken.objects.update_or_create(user = user_obj,defaults={"token":uid})  #对你的user_obj这个对象有就跟新没有就创建一个uid的token随机字符串

        reg.data = uid
        reg.code = 66
        return Response(reg.dict)








