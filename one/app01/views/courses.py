from django.shortcuts import render,HttpResponse

from api import models
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from app01.utils import one
from app01.serializers import courses
class CourseViews(APIView):

    def get(self,request, *args, **kwargs):
        # response = {"code":1000,"data":None,"errors":None}
        res = one.BaseResponse()  # 实例化你定义的类
        try:
            print(request.version)   # 打印你的版本信息
            course_list =  models.Course.objects.all()  # 取数据

            # 分页

            pag = PageNumberPagination()

            course_list = pag.paginate_queryset(course_list,request,self)   # 对你取到的内容进行分页

            ret = courses.CourseSerializer(instance = course_list,many=True)
            res.data = ret.data
        except Exception as e:
            # response["code"] = 500
            # response["errors"] = "查找失败"
            res.code = 500
            res.errors = "查找失败"
        return Response(res.dict)


class CourseDetail(APIView):

    def get(self,request,pk,*args,**kwargs):

        # respone = {"code":1000,"data":None, "errors":None}
        res = one.BaseResponse()

        try:
            course_obj = models.Course.objects.filter(pk = pk).first()
            ret = courses.CourseSerializer(instance=course_obj)
            res.data = ret.data
        except Exception as e:
            res.code = 500

            res.errors = "查询失败"
        return Response(res.dict)



# a.查看所有学位课并打印学位课名称以及授课老师

class DegreeCourseTeacher(APIView):
    def get(self,request,*args,**kwargs):
        res = one.BaseResponse()
        try:
            degree_list = models.DegreeCourse.objects.all()
            ret = courses.DegreeCourseSerializers(instance=degree_list,many=True)
            res.data = ret.data
        except Exception as e:
            res.errors = "查询失败"
            res.code =500
        return Response(res.dict)




# b.查看所有学位课并打印学位课名称以及学位课的奖学金


class DegreeCourseScholarship(APIView):

    def get(self,request):
        res = one.BaseResponse()
        try:
            degree_list = models.DegreeCourse.objects.all()

            # 分页
            page = PageNumberPagination()
            degree_list = page.paginate_queryset(degree_list,request,self)

            ret = courses.DegreeCourseScholarshipSerializers(instance = degree_list,many=True)
            res.data = ret.data

        except Exception as e:

            res.code = 500

            res.errors = "查询失败"

        return Response(res.dict)


class CourseAll(APIView):

    def get(self,request):
        try:
            res = one.BaseResponse()

            course_list = models.Course.objects.all()
            print(course_list)
            # page = PageNumberPagination()
            # course_list = page.paginate_queryset(course_list,request,self)

            ret = courses.CourseALLSerializers(instance=course_list, many = True)

            res.dat = ret.data

        except Exception as e:

            res.code = 500
            res.errors = "查询失败"


        return Response(res.dict)


# d. 查看id=1的学位课对应的所有模块名称

class DegreeCourse(APIView):
    def get(self,request,pk,*args,**kwargs):
        res = one.BaseResponse()
        try:
            degree = models.DegreeCourse.objects.filter(pk = pk).first()
            ret = courses.DegreeCourseSerializer(instance = degree)
            res.data = ret.data
        except Exception as e:
            res.code = 500

            res.errors = "查询失败"

        return Response(res.dict)



# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses


class Courseid(APIView):

    def get(self,request,pk,*args,**kwargs):
        res = one.BaseResponse()
        try:
           course_obj =  models.Course.objects.filter(pk = pk).first()  # 求出对象
           ret = courses.Courseid(instance=course_obj)
           res.data = ret.data
        except Exception as e:

            res.code = 500

            res.errors = "查询失败"
        return Response(res.dict)



# f.获取id = 1的专题课，并打印该课程相关的所有常见问题

class Course_one(APIView):

    def get(self,request,pk,*args,**kwargs):
        res = one.BaseResponse()
        obj = models.Course.objects.filter(pk = pk).first()
        ret = courses.CourseQues(instance=obj)
        res.data = ret.data

        return Response(res.dict)

class CourseLine(APIView):

    def get(self,request,pk,*args,**kwargs):
        res = one.BaseResponse()
        obj = models.Course.objects.filter(pk=pk).first()
        ret = courses.CourseQues(instance=obj)
        res.data = ret.data
        return Response(res.dict)

# h.获取id = 1的专题课，并打印该课程相关的所有章节


class Coursecharter(APIView):
    def get(self,pk,*args,**kwargs):
        print(1111111111)
        res = one.BaseResponse()
        obj = models.Course.objects.filter(pk=pk).first()
        ret = courses.Coursecharter(instance=obj)
        res.data = ret.data
        return Response(res.dict)

















