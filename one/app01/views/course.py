from django.shortcuts import render,HttpResponse

from api.models import Course,DegreeCourse
import json
from app01.serializers import course


from rest_framework.views import APIView
from rest_framework.response import Response




class CourseView(APIView):

    def get(self,request):

        # 版本一：
        # course_list = Course.objects.all().values('id','name')
        # course_list = list(course_list)   # 对你的到的queryset进行转化为list
        # return HttpResponse(json.dumps(course_list,ensure_ascii=False))   # 转化为json字符串

        # 版本二
        courst_list = Course.objects.all()
        ret = course.CourseSerializer(instance=courst_list,many=True)   # 通过你在外部写的serialize序列化  文件进行其表的序列化


        return Response(ret.data)





class CourseDetail(APIView):
    def get(self,request,pk,*args,**kwargs):

        response = {"code":1000, "data":None,"errors":None}
        try:
            degreecourse_list = DegreeCourse.objects.filter(pk = pk).first()

            ret = course.CourseSerializer(instance = degreecourse_list)
            response["data"] = ret.data
        except Exception as e:
            response["code"] = 500
            response["errors"] = "查找失败"

        return Response(response)

