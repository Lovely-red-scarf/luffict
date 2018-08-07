from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from django import views
from api import models
from rest_framework import serializers

from django.http import JsonResponse


#序列化类

class xuliehua(serializers.ModelSerializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField()
    # course_img = serializers.CharField()
    # course_type_choices = serializers.CharField(source="get_course_type_choices_display")
    # course_type = serializers.IntegerField()
    class Meta:
        model = models.Course  # 让你的表和这个类关联起来
        fields = '__all__'  # 这个是查找你的对应的表中的所有的字段

        depth = 1  # 查找你的关联的深度 因为可能你关联


class CourseDetial(APIView):
    '''
    课程详细 类
    '''
    def get(self,request,pk):
        ret = models.Course.objects.filter(id=pk).first()  # 得到你请求的这个课程的对象
        print(ret)
        ret = xuliehua(instance=ret,many=False)
        return Response(ret.data)
        # return HttpResponse("wqw")

    def post(self,pk):
        return HttpResponse('ok')

    def put(self,pk):
        return HttpResponse('ok')



class Xulie(serializers.ModelSerializer):
    #对学位课字段进行序列化
    class Meta:
        model = models.DegreeCourse
        fields = "__all__"
        depth = 1

class DegreeCourse(APIView):
    def get(self,request,pk):
        ret = models.DegreeCourse.objects.filter(pk = pk).first()
        ret = Xulie(ret)
        return Response(ret.data)

    def post(self,ok):
        return HttpResponse('ok')

    def put(self):

        return HttpResponse




class Course_all(APIView):
    def get(self,request):

        ret = models.Course.objects.all()
        # for i in ret:
        #     ret = xuliehua(i)
        ret = xuliehua(instance=ret,many=True)
        return Response(ret.data)
        # return JsonResponse(ret.data,safe=False)



