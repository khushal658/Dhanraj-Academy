"""
URL configuration for Dnynraj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user import views as us
from adpanel import views as ad

urlpatterns = [
    path('',us.index),
    path('enroll/',us.enroll),
    path('save_enroll/',us.save_enroll),
    path('about/',us.about),
    path('course/',us.course),
    path('course_mpsc/<int:id>/',us.course_mpsc , name="course_mpsc"),
    path('course_police/',us.course_police),
    path('course_talathi/',us.course_talathi),
    path('course_vanrakshak/',us.course_vanrakshak),
    path('course_gramsevak/',us.course_gramsevak),   
    path('course_allexams/',us.course_allexams),
    path('latest_update/',us.latest_update),
    path('upd1/',us.upd1),
    path('upd2/',us.upd2),
    path('upd3/',us.upd3),
    path('upd4/',us.upd4),
    path('upd5/',us.upd5),
    path('upd6/',us.upd6),
    path('upd7/',us.upd7),
    path('upd8/',us.upd8),
    path('upd9/',us.upd9),
    path('upd10/',us.upd10),
    path('upd11/',us.upd11),
    path('upd12/',us.upd12),
    path('upd13/',us.upd13),
    path('upd14/',us.upd14),
    path('upd15/',us.upd15),
    path('books_notes/',us.book_notes),
    path('test_series/',us.test_series),
    # path('result/',us.result),
    path('success-story1/',us.success_story1),
    path('success-story2/',us.success_story2),
    path('success-story3/',us.success_story3),
    path('success-story4/',us.success_story4),
    path('success-story5/',us.success_story5),
    path('success-story6/',us.success_story6),
    path('success-story7/',us.success_story7),
    path('success-story8/',us.success_story8),
    path('success-story9/',us.success_story9),
    path('success-story10/',us.success_story10),
    path('success-story11/',us.success_story11),
    path('success-story12/',us.success_story12),
    path('books_notes/',us.book_notes),
    path('test_series/',us.test_series),
    path('result/',us.result),
    path('scholarship/',us.scholarship),
    path('faculty/',us.faculty),
    path('gallary/',us.gallary),
    path('blog/',us.blog),
    path('curruntaffires/',us.curruntaffires),
    path('strategyblogs/',us.strategyblogs),
    path('preprationblogs/',us.preprationblogs),
    path('timetableblogs/',us.timetableblogs),

    path('contact/',us.contact),
    

    # path('admin/', admin.site.urls),

    # admin urls
    path('login/',ad.login),
    path('logout/',ad.logout, name="logout"),
    path('admin/',ad.index),
    # enroll urls
    path('admin/enrollment/',ad.enrollment),
    path('download-enroll-csv/', ad.download_enroll_csv,name='download_enroll_csv'),
    path('delete_enrollment/<int:id>/',ad.delete_enrollment, name = "delete_enrollment"),
    path('admin/view_enrollment/<int:id>/',ad.view_enrollment , name ="view_enrollment"),
    



    # home profile urls
    path('admin/profile/',ad.profile),
    path('save_profile/',ad.save_profile),
    path('update_profile/<int:id>/',ad.update_profile, name= "update_profile"),
    path('admin/profile_list/', ad.profile_list, name='profile_list'),
    # academy statistic
    path('admin/academy_statistics/',ad.academy_statistic),
    path('save_academy_statistic/',ad.save_statistic),
    path('delete_statistic/<int:id>/',ad.delete_statistic, name ="delete_statistic" ),
    path('update_statistic/<int:id>/',ad.update_statistic , name ="update_statistic"),

    # about urls
   
    path('admin/about/',ad.about),
    path('save_train/',ad.about_save, name="save_train"),
    path('delete_about/<int:id>/',ad.delete_about, name="delete_about"),
    path('update_about/<int:id>/',ad.update_about, name = "update_about"),

    
    path('admin/maharashtra_compitation/',ad.maharashtra_compitation,name="maharashtra_compitation"),
    path('admin/student_sucess/',ad.student_sucess,name="student_sucess"),
    path('save_stats/',ad.save_stats, name='save_stats'),
    path('update_stats/<int:id>/', ad.update_stats,name='update_stats'),
    path('admin/acadamy_speciality/',ad.acadamy_speciality,name="acadamy_speciality"),
    path('save_why_choose_us/',ad.save_why_choose_us,name='save_why_choose_us'),
    path('delete_speciality/<int:id>/',ad.delete_speciality,name='delete_speciality'),
    path('save_compitition/',ad.save_compitition,name="save_compitition"),
    path('update_compitition/<int:id>/',ad.maharashtra_compitation,name='update_compitition'),
    path('delete_compitition/<int:id>/',ad.delete_compitition,name='delete_compitition' ),


    # course page url
    path('admin/Mpsc_course/',ad.mpsc_course ,  name='mpsc_course'),
    path('save_mpsc/',ad.save_mpsc , name="save_mpsc"),
    path('delete_mpsc/<int:id>/',ad.delete_mpsc, name="delete_mpsc"),
    path('update_course/<int:id>/',ad.update_mpsc_courses , name = "update_mpsc_courses"),
    path('admin/course_list/',ad.course_list),

    # teacher profile start here 
    path('Teacher_Profiles/',ad.Teacher_Profiles, name="Teacher_Profiles"),
    path('save_Teacher/',ad.Teacher_save, name="save_Teacher"),
    path('Delete_Teacher_Profiles/<int:id>/',ad.Delete_Teacher_Profiles, name="Delete_Teacher_Profiles"),
    path('update_Teacher_Profiles/<int:id>/',ad.update_Teacher_Profiles, name = "update_Teacher_Profiles"),

    # demo session
    path('Demo_Sessions/',ad.Demo_Sessions, name="Demo_Sessions"),
    path('save_Demo_Sessions/',ad.Demo_Sessions_save, name="save_Demo_Sessions"),
    path('Delete_Demo_Sessions/<int:id>/',ad.Delete_Demo_Sessions, name="Delete_Demo_Sessions"),
    path('update_Demo_Sessions/<int:id>/',ad.update_Demo_Sessions, name = "update_Demo_Sessions"),

    # student review 
    path('Student_Reviews/',ad.Student_Reviews, name="Student_Reviews"),
    path('save_Student_Reviews/',ad.Student_Reviews_save, name="save_Student_Reviews"),
    path('Delete_Student_Reviews/<int:id>/',ad.Delete_Student_Reviews, name="Delete_Student_Reviews"),
    path('update_Student_Reviews/<int:id>/',ad.update_Student_Reviews, name = "update_Student_Reviews"),
   
    # subject experties 

    path('Subject/',ad.Subject, name="Subject"),
    path('save_Subject/',ad.Subject_save, name="save_Subject"),
    path('Delete_Subject/<int:id>/',ad.Delete_Subject, name="Delete_Subject"),
    path('update_Subject/<int:id>/',ad.update_Subject, name = "update_Subject"),


    # lagest update 
    path('latest_page/', ad.latest_page, name="latest_page"),
    path('latestpage_upadate/', ad.latestpage_upadate, name="latestpage_upadate"),
    path('delete_latestpage/<int:id>/',ad.delete_latestpage,name='delete_latestpage'),

    path('update_detail/<int:id>/', us.update_detail, name='update_detail'),



     # Result page
    path('admin/result/', ad.admin_result, name='admin_result'),
    path('save_result/', ad.save_result, name='save_result'),
    path('edit_result/<int:id>/', ad.edit_result, name='edit_result'),
    path('update_result/<int:id>/', ad.update_result, name='update_result'),
    path('delete_result/<int:id>/', ad.delete_result, name='delete_result'),
    path('success_story/<int:id>/', ad.success_story, name='success_story'),    
    # User Result Page
    path('result/', us.result, name='user_result'),

# books page start
    path('admin/book/', ad.books, name='book'),
    path('save_books/', ad.books_save, name='save_books'),
    path('delete_book/<int:id>/', ad.delete_book, name='delete_book'),
    path('update-book/<int:id>/', ad.update_book, name='update_book'),

    # User Book page
    path('books_notes/', us.book_notes, name='books_notes'),

# gallary page url

    path('admin/photo_gallary/', ad.photo_gallary, name="photo_gallary"),
    path('save_gallary/',ad.save_gallary,name="save_gallary"),
    path('gallery-update/<int:id>/', ad.edit_gallery, name='gallery_update'),
    path('gallery-delete/<int:id>/', ad.delete_gallery, name='gallery_delete'),
    path('admin/video_gallary/',ad.video_gallary,name="video_gallary"),
    path('add_video/', ad.add_video, name='add_video'),
    path('delete_video/<int:id>/', ad.delete_video, name='delete_video'),
    path('edit_video/<int:id>/', ad.edit_video, name='edit_video'),


# blog page url
    
    path('admin/blog_card/',ad.blog_card,name="blog_card"),
    path('save_blog/', ad.save_blog, name='save_blog'),
    path('delete_blog/<int:id>/', ad.delete_blog, name='delete_blog'),
    path('admin/read_more1/',ad.read_more1,name="read_more1"),
    path('exam/', ad.exam, name='exam'),
    path('admin/delete_exam/<int:id>/', ad.delete_exam, name='delete_exam'),
    path('admin/read_more2/',ad.read_more2,name="read_more2"),
    path('question/', ad.question, name='question'),
    path( 'admin/delete_affair/<int:id>/',ad.delete_affair,name='delete_affair'),
    path('blogs_detail/', us.blog_detail, name='blogs_detail'),
    # new
    path('timetable-blog/', us.blog_timetable, name='timetable_blog'),
    path('tips-blog/', us.blog_tips, name='tips_blog'),
    path('preparation-blog/', us.blog_preparation, name='preparation_blog'),
    path('current-affairs-blog/', us.blog_current_affairs, name='current_affairs_blog'),
    

    # contact page start

    path('Contact_us/',ad.Contact_us, name="Contact_us"),
    path('save_Contact_us/',ad.Contact_us_save, name="save_Contact_us"),
    path('Delete_Contact_us/<int:id>/',ad.Delete_Contact_us, name="Delete_Contact_us"),
    path('Update_Contact_us/<int:id>/',ad.Update_Contact_us, name = "Update_Contact_us"),

    # contact card 

    path('Contact_card/',ad.Contact_card, name="Contact_card"),
    path('save_Contact_card/',ad.Contact_card_save, name="save_Contact_card"),
    path('Delete_Contact_card/<int:id>/',ad.Delete_Contact_card, name="Delete_Contact_card"),
    path('Update_Contact_card/<int:id>/',ad.Update_Contact_card, name = "Update_Contact_card"),


# contact about
   path('Contact_about/',ad.Contact_about, name="Contact_about"),
   path('save_Contact_about/',ad.Contact_about_save, name="save_Contact_about"),
   path('Delete_Contact_about/<int:id>/',ad.Delete_Contact_about, name="Delete_Contact_about"),
   path('Update_Contact_about/<int:id>/',ad.Update_Contact_about, name = "Update_Contact_about"),


# contact form
   path('Contact_form_table/',ad.Contact_form_table, name="Contact_form_table"),
   path('Delete_Contact_form_table/<int:id>/',ad.Delete_Contact_form_table, name="Delete_Contact_form_table"),
   path('update-contact-status/<int:id>/',ad.update_contact_status,name='update_contact_status'),
   path('save_Contact_form_table/',us.Contact_form_table_save, name="save_Contact_form_table"),

#   contact callback
    path('Contact_callback/',ad.Contact_callback, name="Contact_callback"),
    path('Delete_Contact_callback/<int:id>/',ad.Delete_Contact_callback, name="Delete_Contact_callback"),
    path('update_callback_status/<int:id>/', ad.update_callback_status, name='update_callback_status'),
    path('save_Contact_callback/',us.Contact_callback_save, name="save_Contact_callback"),

    path('Contact_faq/',ad.Contact_faq, name="Contact_faq"),
    path('save_Contact_faq/',ad.Contact_faq_save, name="save_Contact_faq"),
    path('Delete_Contact_faq/<int:id>/',ad.Delete_Contact_faq, name="Delete_Contact_faq"),
    path('Update_Contact_faq/<int:id>/',ad.Update_Contact_faq, name = "Update_Contact_faq"),

    path('Contact_AskedQ/',ad.Contact_AskedQ, name="Contact_AskedQ"),
    path('save_Contact_AskedQ/',ad.Contact_AskedQ_save, name="save_Contact_AskedQ"),
    path('Delete_Contact_AskedQ/<int:id>/',ad.Delete_Contact_AskedQ, name="Delete_Contact_AskedQ"),
    path('Update_Contact_AskedQ/<int:id>/',ad.Update_Contact_AskedQ, name = "Update_Contact_AskedQ"),
 

    path('Contact_Locations/',ad.Contact_Locations, name="Contact_Locations"),
    path('save_Contact_Locations/',ad.Contact_Locations_save, name="save_Contact_Locations"),
    path('Delete_Contact_Locations/<int:id>/',ad.Delete_Contact_Locations, name="Delete_Contact_Locations"),
    path('Update_Contact_Locations/<int:id>/',ad.Update_Contact_Locations, name = "Update_Contact_Locations"),

    path('Contact_form_cources/', ad.Contact_form_cources, name='Contact_form_cources'),
    path('save_Contact_form_cources/', ad.Contact_form_cources_save, name='Contact_form_cources_save'),
    path('update_contact_form_course/<int:id>/', ad.update_contact_form_course, name='update_contact_form_course'),
    path('Delete_Contact_form_cources/<int:id>/', ad.Delete_Contact_form_cources, name='Delete_Contact_form_cources'),

]
