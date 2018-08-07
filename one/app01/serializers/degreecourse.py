from rest_framework import serializers

from api import models

class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()



class CourseModelSerializer(serializers.ModelSerializer):  # ModelSerializer  是多对多的时候需要用到的序列化

    level_name = serializers.CharField(source = "get_level_display")

    hours = serializers.CharField(source = 'coursedetail.hours')  # 对 CourseDetail 中的hours字段及逆行序列化

    course_slogan = serializers.CharField( source = 'coursedetail.course_slogan')

    recommend_courses  = serializers.SerializerMethodField()  # 上面的字段我们可以通过course就是

    class Meta:
        model = models.Course

        fields = ["id", "name", "level_name", "hours", "course_slogan", "recommend_courses"]


        def get_recommend_courses(self,obj):  # obj就是你的  Cours这个表对象

            recommend_list = obj.coursedetail.recommend_coures.all()


            return [{"id":item.id, "name":item.name} for item in recommend_list]   # 列表生成氏  返回一个字典  因为json数据类型的  就是应该是字典类型的



