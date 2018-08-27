from django.shortcuts import render,HttpResponse


from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
# Create your views here.
from luffy import models

# def course(request):
#
#     # 1.	查看所有学位课并打印学位课名称以及授课老师
#     obj = models.DegreeCourse.objects.all().values("name","teachers__name")
#     print(obj)
#
#
#     return HttpResponse("ok")

class Course(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        # 1.	查看所有学位课并打印学位课名称以及授课老师
        #     obj = models.DegreeCourse.objects.all().values("name","teachers__name")
        #     print(obj)

        #2.	查看所有学位课并打印学位课名称以及学位课的奖学金
        # obj = models.DegreeCourse.objects.all()
        # for data in obj:
        #     print(data.degreecourse_price_policy.all(),data.name)  # 反向查询需要用到对象.z字段.all()


        # 3.	展示所有的专题课
        # obj = models.Course.objects.filter(degree_course__isnull=True).values("name")

        pk = request.query_params.get("pk")


        # 5.	获取id=1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
        # obj = models.Course.objects.filter(pk = pk,degree_course__i
        obj = models.Course.objects.filter(pk=3,degree_course__isnull=True).first()


        print(obj.name,
              obj.get_level_display(),
              obj.coursedetail.why_study,
              obj.coursedetail.what_to_study_brief,
              # obj.coursedetail.recommend_courses.all()
                obj.recommend_by.all())
        # )  # 因为设置了别名 需要用别名reletename 来查找  因为还有一个一对一的字段 也就是多了一种写法 也可以通过表名反向查询




        # 6.	获取id=1的专题课，并打印该课程相关的所有常见问题
        # obj = models.Course.objects.filter(pk = 1,degree_course__isnull=True).first()
        # print(obj.asked_question.all())
        # print(obj)

        # 获取id=1的专题课，并打印该课程相关的课程大纲

        # obj = models.Course.objects.filter(pk = 2,degree_course__isnull=True).first()
        #
        # print(obj.coursedetail.courseoutline_set.all().values('content'))  # 对象查询反向一对多的必须用_set.all()然后取其中的额值再values() 如果是
        # # 对象查询一对多反向查询要用set

        # 8.	获取id=1的专题课，并打印该课程相关的所有章节
        #id
        # obj = models.Course.objects.filter( id = 1).values("xxxxx__name")  # 因为设置了reletename 那么就要通过这个别名来查找




        # 9.	获取id=1的专题课，并打印该课程相关的所有的价格策略
        # obj = models.Course.objects.filter(id = 1).first()
        # print(obj.price_policy.all())  # 因为价格策略使用了contentType 所以可以通过course表中设置的GenericRelation 的字段反向查找  必须是对象.字段.all()


        # 10.	获取id=1的专题课，并打印该课程相关的所有课时
        obj = models.Course.objects.filter(id =1).values("xxxxx__coursesections__name")  # 通过别名来反向查询 如果都有别名必须用别名来查找
        print(obj)









        return HttpResponse("ok")


    def create(self,request,pk,*args,**kwargs):


        # 4.	查看id=1的学位课对应的所有模块名称
        obj = models.DegreeCourse.objects.filter(pk = pk).values("course__name")



        print(obj)

        return HttpResponse("ok")