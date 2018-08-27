import json
import redis

from one.settings import LUFFY_SHOPPING_CAR
from api.utils.auth import Auth
from luffy import models

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.shortcuts import render,redirect,HttpResponse

from django_redis import get_redis_connection  # 会创建一个连接池 然后在连接池子中找到你的redis信息如果settings中配置之后没有指定信心那么就会在本地进行创建 或者查找

# CONN = get_redis_connection("default")

CONN = redis.Redis(host='192.168.11.61',port=6379)
class Payment(ViewSetMixin,APIView):
    '''
    订单界面你也需要构造你的redis的结构，其实就是和你的购物车的差不多
    '''
    parser_classes = [JSONParser]  #导入解析器
    authentication_classes = [Auth]  #实例化认证类


    def create(self,request,*args,**kwargs):
        '''
        创建你的订单界面
        :param request:
        :param args:
        :param kwargs:
        :return:
        '''

        # 这是一个成成订单的界面 这个界面是从你的购物车中先把你的存放的信息给取出来 然后再添加到订单界面然后结算
        user_id = request.user.id  #从你的认证信息中取当前登陆用户的id
        course_list = request.data.get("courselist")
        for course_id in course_list:
            shop_car_key = LUFFY_SHOPPING_CAR %(request.user.id,course_id)
            if not shop_car_key:
                #不存在
                return Response({"errors":"课程不存在"})

            # 课程存在就取出对应的信息

            id = CONN.hget(shop_car_key,"id").decode("utf8")
            name = CONN.hget(shop_car_key,"name").decode("utf8")
            price_policy_dict = json.loads(CONN.hget(shop_car_key,"price_policy_dict").decode("utf8"))


        #然后根据用户的id来获取这个用户的拥有的优惠券
        import datetime
        today = datetime.date.today()
        coupon_list = models.CouponRecord.objects.filter(account_id = user_id,
                                           status = 0,
                                           coupon__valid_begin_date_lte=today,
                                           coupon__valid_end_date_gte=today,
                                           coupon__content_type__models="course", #优惠券的类型是专题课的
        )



        global_coupon_list = models.CouponRecord.objects.filter(course_id = user_id,
                                                                status=0,
                                                                coupon__valid_begin_date_lte=today,
                                                                coupon__valid_end_date_gte=today,
                                                                coupon__content_type__isnull=True  #没有绑定课程就是所有的优惠券



        )

