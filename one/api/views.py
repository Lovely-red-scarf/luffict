from django.shortcuts import render,HttpResponse

# Create your views here.


from api import models

def inquire(request):

    '''
    #1 查看所有学位课并打印学位课名称以及授课老师

    degreecourse = models.DegreeCourse.objects.all()
    for i in degreecourse:
        print(i.teachers.all(), i.name)
    '''

    # 2 查看所有学位课并打印学位课名称以及学位课的奖学金
    # degreecourse = models.DegreeCourse.objects.all().values('name','scholarship__value')   # 就是简单的跨表查询
    # print(degreecourse)

    # 3 展示所有的专题课
    # models.Course.objects.filter(degree_course__isnull=True)


    # 4 查看id=1的学位课对应的所有模块名称

    ret =  models.DegreeCourse.objects.filter(pk = 1,course__degree_course__isnull = False).values('course__name')   # 前面是查的是满足条件的 这个时候你还是在你的DegreeCourse中  你需要到course表中去查询满足的名字
    print(ret)


    # 5 :获取id=1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses

    # ret = models.Course.objects.filter(id = 1).first()
    # print(ret.get_level_display(),ret.name)   # get_列_display() 是查找带choices的列中的中文名


    # 6 获取id=1的专题课，并打印该课程相关的所有常见问题

    # ret = models.Course.objects.filter(id = 1,degree_course__isnull = True).first()
    # ret =ret.asked_question.all()
    # for i in ret:
    #     print(i.question)
        # 先通过cententType提供的反向查询 查到 这个id等于1和问题表进行的关联 然后再进行的 这个queryset进行循环 得到它的评论

    # g.获取id = 1 的专题课，并打印该课程相关的课程大纲

    # ret = models.Course.objects.filter(id = 1,degree_course__isnull = True).values('coursedetail__courseoutline__title')   # 因为取到了id为1 的内容 然后进行反向查询  得到coursedetail__这个是进入了coursedetail表内再进行反向查询就得到了内容
    # print(ret)

    # h.获取id = 1 的专题课，并打印该课程相关的所有章节

    # ret = models.Course.objects.filter(id=1,degree_course__isnull = True).values('coursechapters__name')
    # print(ret)



    # 获取id=1的专题课，并打印该课程相关的所有课时
    # ret = models.Course.objects.filter(id = 1,degree_course__isnull = True).values('coursechapters__coursesections__pub_date')
    # print(ret)



    # 获取id=1的专题课，并打印该课程相关的所有的价格策略


    # ret = models.Course.objects.filter(id= 1).first()
    # ret = ret.price_policy.all()
    # print(ret)
    return HttpResponse('ok')


