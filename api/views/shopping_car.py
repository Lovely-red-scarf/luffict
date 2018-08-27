from django.shortcuts import render,redirect,HttpResponse

import json
import redis
from api.utils.auth import Auth
from api.utils import response
from luffy import models
from one.settings import LUFFY_SHOPPING_CAR

from rest_framework.viewsets import ViewSetMixin
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response


# Create your views here.


USER_id = 1
CONN = redis.Redis(host="118.25.234.102",port=6379)

class ShoppingCar(ViewSetMixin,APIView):

    parser_classes = [JSONParser]  # 配置这个JSONParser可以从你的请求体中解析数据然后把数据进行反序列化 然后放器request.data中
    authentication_classes = [Auth] #导入你的认证信息 然后可以进行你登陆后的信息的取值

    def list(self,request,*args,**kwargs):

        pattern = LUFFY_SHOPPING_CAR %(USER_id ,"*")
        key =CONN.keys(pattern)  #获取所有的key
        print(key)

        message = []
        # 因为你的redis是个大字典有很多的 对应的values 所以要把你取到的值都放到一个容器中然后再返回出去
        for data in key:
            temp ={
                "id":CONN.hget(data,"id").decode("utf8"),
                "name":CONN.hget(data,"name").decode("utf8"),
                "img":CONN.hget(data,"img").decode("utf8"),
                "default_price_id":CONN.hget(data,"default_price_id").decode("utf8"),
                "price_policy_dict":json.loads(CONN.hget(data,"price_policy_dict").decode("utf8"))  #存进去是字符串必须反序列化
            }
            message.append(temp)

        return Response(message)




    def create(self,request,*args,**kwargs):

        reg = response.Response()
        '''
        加入购物车 创建购物车的信息
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''
        # 从requst.data中取到你解析后的请求体中的数据
        courseid = request.data.get("courseid")
        policyid = request.data.get("policyid")


        obj = models.Course.objects.filter(pk = courseid).first() # 取到课程id
        if not obj:  #如果课程不存在
            reg.code = 88
            reg.errors = "老哥课程错误啦"
            return reg.dict
        # 课程存在
        # 找到课程相关的所有的价格策略 然后判断这个在不在里面
        policy_set = obj.price_policy.all() #所有的价格
        price_policy_dict = {}
        for data in policy_set:
            temp = {
                "id":data.id,
                "price":data.price,
                "valid_period":data.valid_period,
                "valid_period_display":data.get_valid_period_display(),
            }  #获取价格的所有内容
            price_policy_dict[data.id] = temp #用这个价格策略的id== 价格策略所有的内容

        if policyid not in price_policy_dict:
            reg.errors = "傻X 别乱改价格"
            reg.code = 88
            # return reg.dict
        #如果存在就添加信息  首先我们要根据我们设置的key来进行添加信息
            return Response({"code": 88, "errors": "乱改"})


        # 我们还要判断如果购物车的信息大于100个就先让他取结算
        parrent = LUFFY_SHOPPING_CAR %(USER_id ,"*")
        keys = CONN.keys(parrent)  # 获取你的redis中的key是parrent的信息然后把这些key都加入一个列表中
        if len(keys) > 100:
            return ({"code":88,"errors":"购物车信息过多先去结算"})
        key = LUFFY_SHOPPING_CAR %(USER_id ,courseid) #把你的购物车的key先拼接出来
        CONN.hset(key,"id",courseid)
        CONN.hset(key,"name",obj.name)
        CONN.hset(key,"img",obj.course_img)
        CONN.hset(key,"default_price_id",policyid)
        CONN.hset(key,"price_policy_dict",json.dumps(price_policy_dict))  #redis的第三层必须是字符串所以序列化成字符串


        CONN.expire(key,60*60*24)  #设置24小时清空购物车

        return Response({"code":666,"data":"购买成功"})



    def update(self,request):
        reg = response.Response()
        '''
        修改价格策略
        :return:
        '''

        # 我们要知道修改的是第三层  用户对应的课程的价格策略

        course_id = request.data.get("courseid")
        policy_id = str(request.data.get("policyid")) if request.data.get("policyid") else None  # 虽然发送的的是int但是序列化之后就是str的了

        key = LUFFY_SHOPPING_CAR%(USER_id,course_id)

        if not CONN.exists(key):
            reg.code = 88
            reg.errors = "课程不存在"

            return Response(reg.dict)
        # 课程存在判断价格策略
        price_policy_dict = json.loads(CONN.hget(key,"price_policy_dict").decode("utf8"))  #取出这个课程的价格策略
        if policy_id not in price_policy_dict: # 不存在
            reg.code = 88
            reg.errors = "价格策略不存在"

            return Response(reg.dict)

        # 存在

        CONN.hset(key,"price_policy_dict",policy_id)
        CONN.expire(key,24*60*60)# 清空购物车

        return Response({"meg":"修改成功"})




    def dd(self,request):
        '''
        删除购物车信息
        :param request:
        :return:
        '''
        # 我们找到课程构建的key删除即可
        course_id = request.data.get("courseid")
        # key = CONN.keys(course_id)
        key = LUFFY_SHOPPING_CAR%(USER_id,course_id)
        CONN.delete(key)

        return Response({"errors":"删除完成"})











