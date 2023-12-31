from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    ########### Program Master ###########
    path('program-master', views.program_master, name='program_master'),
    path('insert-program', views.insert_program, name='insert_program'),
    path('edit-program/<str:id>',views.edit_program, name='edit_program'),
    path('update-program/<str:id>',views.update_program,name='update_program'),

    ########### Scheme ###########
    path('scheme/<str:id>', views.scheme, name='scheme'),
    

    ########### Course Master ###########
    path('course-master', views.course_master, name='course_master'),
    path('insert-course', views.insert_course, name='insert_course'),
    path('edit-course/<str:id>',views.edit_course, name='edit_course'),
    path('update-course/<str:id>',views.update_course,name='update_course'),
    path('search-course',views.search_course,name='search_course'),
    # path('delete-course/<str:id>',views.delete_course,name='delete_course'),

    ########### Faculty Master ###########
    path('faculty-master', views.faculty_master, name='faculty_master'),
    path('insert-faculty', views.insert_faculty, name='insert_faculty'),
    path('edit-faculty/<str:id>',views.edit_faculty, name='edit_faculty'),
    path('update-faculty/<str:id>',views.update_faculty,name='update_faculty'),
    # path('available-faculty-autumn1', views.available_faculty_autumn1, name='available_faculty_autumn1'),
    # path('available-faculty-autumn2', views.available_faculty_autumn2, name='available_faculty_autumn2'),
    # path('available-faculty-winter1', views.available_faculty_winter1, name='available_faculty_winter1'),

    ########### Course Offering ###########
    path('course-offered', views.course_offered, name='course_offered'),
    path('insert-course-offered', views.insert_course_offered, name='insert_course_offered'),
    path('search-program',views.search_program,name='search_program'),

    ########### Semester ###########
    path('course-faculty', views.course_faculty, name='course_faculty'),
    path('insert-course-faculty', views.insert_course_faculty, name='insert_course_faculty'),
    # path('edit-course-faculty/<str:id>',views.edit_course_faculty, name='edit_course_faculty'),
    # path('update-course-faculty/<str:id>',views.update_course_faculty,name='update_course_faculty'),
    path('search-faculty',views.search_faculty,name='search_faculty'),

    ########### Elective Details ###########
    path('electives', views.electives, name='electives'),
    path('search-elective',views.search_elective,name='search_elective'),


    ########### Slot Assignment ###########
    path('slots', views.slots, name='slots'),
    path('insert-slot', views.insert_slot, name='insert_slot'),
    path('edit-slot/<str:id>',views.edit_slot, name='edit_slot'),
    path('update-slot/<str:id>',views.update_slot,name='update_slot'),
    path('search-slot',views.search_slot,name='search_slot'),

    ########### Generate Timetable ###########
    path('timetable', views.timetable, name='timetable'),
    path('export', views.export_csv, name='export_csv'),


    ########### Autumn 1 ###########
    path('autumn1', views.autumn1, name='autumn1'),
    path('insert-autumn1', views.insert_autumn1, name='insert_autumn1'),
    path('edit-autumn1/<str:id>',views.edit_autumn1, name='edit_autumn1'),
    path('update-autumn1/<str:id>',views.update_autumn1,name='update_autumn1'),
    path('search-content',views.search_content,name='search_content'),
    path('not-autumn1', views.not_autumn1, name='not_autumn1'),

    ########### Autumn 2 ###########
    path('autumn2', views.autumn2, name='autumn2'),
    path('insert-autumn2', views.insert_autumn2, name='insert_autumn2'),
    path('edit-autumn2/<str:id>',views.edit_autumn2, name='edit_autumn2'),
    path('update-autumn2/<str:id>',views.update_autumn2,name='update_autumn2'),
    path('search-content2',views.search_content2,name='search_content2'),
    path('not-autumn2', views.not_autumn2, name='not_autumn2'),

    ########### Winter 1 ###########
    path('winter1', views.winter1, name='winter1'),
    path('insert-winter1', views.insert_winter1, name='insert_winter1'),
    path('edit-winter1/<str:id>',views.edit_winter1, name='edit_winter1'),
    path('update-winter1/<str:id>',views.update_winter1,name='update_winter1'),
    path('search-content3',views.search_content3,name='search_content3'),
    path('not-winter1', views.not_winter1, name='not_winter1'),
]