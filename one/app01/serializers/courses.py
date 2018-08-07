from rest_framework import serializers

from api import models

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()



class CourseModelSerializer(serializers.ModelSerializer):  # ModelSerializer  是多对多的时候需要用到的序列化

    level_name = serializers.CharField(source = "get_level_display")

    hours = serializers.CharField(source = 'coursedetail.hours')  # 对 CourseDetail 中的hours字段及逆行序列化

    course_slogan = serializers.CharField( source = 'coursedetail.course_slogan')

    recommend_courses  = serializers.SerializerMethodField()  # 上面的字段我们可以通过course获取但是manytomany不可以
    class Meta:
        model = models.Course

        fields = ["id", "name", "level_name", "hours", "course_slogan", "recommend_courses"]


        def get_recommend_courses(self,obj):  # obj就是你的  Cours这个表对象

            recommend_list = obj.coursedetail.recommend_coures.all()   # 因为是反向查询所以需要加一个表名然后再加上你的关联字段


            return [{"id":item.id, "name":item.name} for item in recommend_list]   # 列表生成氏  返回一个字典  因为json数据类型的  就是应该是字典类型的




class DegreeCourseSerializers(serializers.ModelSerializer):
    name = serializers.CharField()

    teacher_name  = serializers.SerializerMethodField()

    class Meta:
        model = models.DegreeCourse

        fields = ['name',"teacher_name"]

        def get_teacher_name(self,obj):
            teacher_list = obj.teachers.all()
            return [{"id":item.id, "name":item.name} for item in teacher_list]


# b.查看所有学位课并打印学位课名称以及学位课的奖学金
class DegreeCourseScholarshipSerializers(serializers.ModelSerializer):
    name = serializers.CharField()

    school_name = serializers.CharField(source = "schoolarship.name")

    class Meta:
        model = models.DegreeCourse

        fields = ["name", "school_name"]



# c.展示所有的专题课


class CourseALLSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ["id","name"]



# d. 查看id=1的学位课对应的所有模块名称
class DegreeCourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    brief = serializers.CharField()

    degree_course = serializers.SerializerMethodField()  # 奖学金

    course = serializers.SerializerMethodField()   # 这个SerializerMethodField可以定义获取的方法
    def get_degree_course(self,obj):
        li = []
        scholarship_list = obj.scholarship_set.all()
        print(scholarship_list)
        for item in scholarship_list:
            li.append(item.value)
        return li

    def get_course(self,obj):
        ll =[]
        course_list = obj.course_set.all()
        print(course_list)

        for i in course_list:
            ll.append(i.name)
        return ll




# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses

class Courseid(serializers.ModelSerializer):
    level = serializers.CharField(source = "get_level_display")
    why_study = serializers.CharField(source = "coursedetail.why_study")
    what_to_study_brief = serializers.CharField(source= "coursedetail.what_to_study_brief")
    recommend_courses = serializers.SerializerMethodField()   # 对你的要查找的recommend_courses 是manytomany的所以需要进行设置函数来定义查找

    class Meta:
        model = models.DegreeCourse
        fields = ["id", "name", "level","why_study","what_to_study_brief","recommend_courses"]

        def get_recommend_courses(self,obj):
            recommend_list =  obj.coursedetail.recommend_coures.all()
            return [{"id": item.id, "name":item.name} for item in recommend_list]



# f.获取id = 1的专题课，并打印该课程相关的所有常见问题


class CourseQues(serializers.Serializer):

    id = serializers.IntegerField()

    name = serializers.CharField()

    # question = serializers.CharField(source = "oftenaskedquestion.question")
    question = serializers.CharField(source = "asked_question.all")   # 因为是用cententType关联的  我们直接就用 他们关联的属性来查找   GenericRelation是在course中的asked_question中的字段属性 我们就按照反向查询  来查找



# g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CourseLine(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    line_name = serializers.SerializerMethodField()
    def get_line_name(self,obj):
        course_list = obj.coursedetail.courseoutline_set.all()
        return [{"id": item.id, "name": item.name} for item in course_list ]




# h.获取id = 1的专题课，并打印该课程相关的所有章节

class Coursecharter(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    chapter_name = serializers.CharField(source = "coursechapters.all")






















