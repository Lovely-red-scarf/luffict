from django.conf.urls import url

from app01.views import course,courses
urlpatterns = [

    url(r'course/$',course.CourseView.as_view()),   # 因为我们已经不是从views内导入了是从我们新建立的views内导入course
    # url(r'coursedetail/(?P<pk>\d+)/$',course.CourseDetail.as_view()),
    url(r"coo/$",courses.CourseViews.as_view()),

    url(r'coursedetail/(?P<pk>\d+)/',courses.CourseDetail.as_view()),

    url(r'degreecourse/$',courses.DegreeCourseTeacher.as_view()),

    # 2
    url(r'degreeschoolarship/',courses.DegreeCourseScholarship.as_view()),

    # 3
    url(r'courseall/$',courses.CourseAll.as_view()),

    # 4
    url(r'degreecourseall/(?P<pk>\d+)/$',courses.DegreeCourse.as_view()),

    # 5

    url(r'courseid/(?P<pk>\d+)/$',courses.Courseid.as_view()),
    # 6
    url(r'courseone/(?P<pk>\d+)/$',courses.Course_one.as_view()),

    # 7
    url(r'courseline/(?P<pk>\d+)/$',courses.CourseLine.as_view()),

    # 8
    url(r"coursechar/(?P<pk>\d+)", courses.Coursecharter.as_view()),








]