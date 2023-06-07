from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    ########### Program Master ###########
    path('program-master', views.program_master, name='program_master'),
    path('insert-program', views.insert_program, name='insert_program'),
    path('edit-program/<str:id>',views.edit_program, name='edit_program'),
    path('update-program/<str:id>',views.update_program,name='update_program'),

    ########### Course Master ###########
    path('course-master', views.course_master, name='course_master'),
    path('insert-course', views.insert_course, name='insert_course'),
    path('edit-course/<str:id>',views.edit_course, name='edit_course'),
    path('update-course/<str:id>',views.update_course,name='update_course'),
    # path('delete-course/<str:id>',views.delete_course,name='delete_course'),

    ########### Faculty Master ###########
    path('faculty-master', views.faculty_master, name='faculty_master'),
    path('insert-faculty', views.insert_faculty, name='insert_faculty'),
    path('edit-faculty/<str:id>',views.edit_faculty, name='edit_faculty'),
    path('update-faculty/<str:id>',views.update_faculty,name='update_faculty'),
]