from django.db import models

# Create your models here.

class Profile(models.Model):
   mobile = models.CharField(max_length=15)
   email = models.EmailField()
   password = models.CharField(max_length=50)
   year = models.CharField(max_length=100)
   logo = models.ImageField(upload_to='static/ad/images/')
   academy_name = models.CharField(max_length=300)
   address = models.TextField()
   facebook = models.CharField(max_length=500)
   linkdin = models.CharField(max_length=500)
   twitter = models.CharField(max_length=500)
   youtube = models.CharField(max_length=500)
   instagram = models.CharField(max_length=500)


class Academy_Statistic(models.Model):
   statistic_title = models.CharField(max_length=500)
   statistic_count = models.IntegerField(default=0)
   statistic_icon  = models.CharField(max_length=500)


class aboutdahanraj(models.Model):
   heading = models.CharField(max_length=700)
   paragraph = models.TextField()
   train_number = models.IntegerField()
   stu_num = models.IntegerField()
   expfac_num = models.IntegerField()
   course_num = models.IntegerField()

class CompetitionAbout(models.Model):

    main_heading = models.CharField(max_length=500)

    about_description = models.TextField()

    vision_description = models.TextField()

    year1 = models.CharField(max_length=20)
    timeline1 = models.TextField()

    year2 = models.CharField(max_length=20)
    timeline2 = models.TextField()

    year3 = models.CharField(max_length=20)
    timeline3 = models.TextField()

    year4 = models.CharField(max_length=20)
    timeline4 = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.main_heading
    



class WhyChooseUs(models.Model):
    icon = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    description = models.TextField()

    def __str__(self):
        return self.title
    

class StatsSection(models.Model):

    students_number = models.CharField(max_length=100)
    students_label = models.CharField(max_length=100)

    selection_number = models.CharField(max_length=100)
    selection_label = models.CharField(max_length=100)

    batch_number = models.CharField(max_length=100)
    batch_label = models.CharField(max_length=100)

    course_number = models.CharField(max_length=100)
    course_label = models.CharField(max_length=100)

    experience_number = models.CharField(max_length=100)
    experience_label = models.CharField(max_length=100)

    def __str__(self):
        return "Stats Section"


class mpsccourse(models.Model):
   department = models.CharField(max_length=500)
   course_name = models.CharField(max_length=500)
   duration = models.CharField(max_length=200)
   fees = models.CharField(max_length=300)
   timing = models.CharField(max_length=300)
   # mode = models.CharField(max_length=200)
   extra_label = models.CharField(max_length=100, null=True, blank=True)
   extra_value = models.CharField(max_length=200, null=True, blank=True)
# course info
   heading = models.CharField(max_length=1000, null=True, blank=True)
   title = models.CharField(max_length=1000, null=True, blank=True)
 
   eligibility = models.CharField(max_length=1000, null=True, blank=True)
   
   benefit1 = models.CharField(max_length=1000, null=True, blank=True)
   benefit2 =  models.CharField(max_length=1000, null=True, blank=True)
   benefit3 =  models.CharField(max_length=1000, null=True, blank=True)
   benefit4 =  models.CharField(max_length=1000, null=True, blank=True)
   benefit5 = models.CharField(max_length=1000, null=True, blank=True)
   admission_notice =models.TextField(null=True, blank=True)

  

   show_on_home = models.BooleanField(default=False)

# teacher profile start
class Teacher_Profilesdahanraj(models.Model):
   images = models.ImageField(upload_to='static/ad/images/')
   fullname = models.CharField(max_length=500)
   traner = models.CharField(max_length=500)
   experience = models.CharField(max_length=500)
   linkedin = models.CharField(max_length=500)
   instagram = models.CharField(max_length=500)
   twitter = models.CharField(max_length=500)

# demo session model start
class Demo_Sessionsdahanraj(models.Model):
   title = models.CharField(max_length=700)
   dec = models.CharField(max_length=2000)
   sub_btn = models.CharField(max_length=2000)
   sub_dec = models.CharField(max_length=2000)
   sub_video = models.FileField(upload_to='static/ad/videos')


# student review start

class Student_Reviewsdahanraj(models.Model):
   images = models.ImageField(upload_to='static/ad/images/')
   fullname = models.CharField(max_length=500)
   traner = models.CharField(max_length=500)
   icon = models.CharField(max_length=500)
   dec = models.CharField(max_length=500)

   # subject experts

class Subjectdahanraj(models.Model):
   title = models.CharField(max_length=700)
   dec = models.CharField(max_length=2000)



class Latestpage(models.Model):

    CATEGORY_CHOICES = [('Notification', 'Notification'),('Result', 'Result'),('New Batch', 'New Batch'),('Admission', 'Admission'),('Event', 'Event'),
    ]

    # Card Data

    category = models.CharField(max_length=50,choices=CATEGORY_CHOICES,blank=True,null=True
    )

    heading = models.CharField(max_length=500)

    heading_description = models.CharField(max_length=500)

    dob = models.CharField(max_length=200)

    slider_image = models.ImageField(upload_to='static/ad/images/' )

    # Hero Section

    badge_text = models.CharField(max_length=300,blank=True, null=True )

    hero_heading = models.CharField(max_length=500,blank=True,null=True
    )

    hero_description = models.TextField(blank=True,null=True
    )

    # Overview

    overview_title = models.CharField(max_length=500,blank=True,null=True
    )

    overview_description = models.TextField(blank=True,null=True
    )

    # Physical Test

    physical_title = models.CharField(max_length=500,blank=True,null=True
    )

    physical_point_1 = models.CharField(max_length=500, blank=True, null=True)
    physical_point_2 = models.CharField(max_length=500, blank=True, null=True)
    physical_point_3 = models.CharField(max_length=500, blank=True, null=True)
    physical_point_4 = models.CharField(max_length=500, blank=True, null=True)
    physical_point_5 = models.CharField(max_length=500, blank=True, null=True)

    # Written Exam

    written_title = models.CharField(max_length=500,blank=True,null=True
    )

    written_point_1 = models.CharField(max_length=500, blank=True, null=True)
    written_point_2 = models.CharField(max_length=500, blank=True, null=True)
    written_point_3 = models.CharField(max_length=500, blank=True, null=True)
    written_point_4 = models.CharField(max_length=500, blank=True, null=True)
    written_point_5 = models.CharField(max_length=500, blank=True, null=True)

    # Selection Process

    selection_title = models.CharField(max_length=500,blank=True,null=True
    )

    selection_description = models.TextField(blank=True,null=True
    )

    step1_title = models.CharField(max_length=500, blank=True, null=True)
    step1_description = models.TextField(blank=True, null=True)

    step2_title = models.CharField(max_length=500, blank=True, null=True)
    step2_description = models.TextField(blank=True, null=True)

    step3_title = models.CharField(max_length=500, blank=True, null=True)
    step3_description = models.TextField(blank=True, null=True)

    step4_title = models.CharField(max_length=500, blank=True, null=True)
    step4_description = models.TextField(blank=True, null=True)

    def __str__(self):return self.heading




class Result(models.Model):
    CATEGORY_CHOICES = (
        ('Police', 'Police'),
        ('Gramsevak', 'Gramsevak'),
        ('Vanrakshak', 'Vanrakshak'),
        ('MPSC', 'MPSC'),
        ('Talathi', 'Talathi'),
    )

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES ,null=True,
    blank=True)
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/ad/images/')
    # success story 
    
    title = models.CharField(max_length=255 ,null=True, blank=True)
    post = models.CharField(max_length=255,null=True, blank=True)
    education = models.CharField(max_length=255,null=True, blank=True)
    posting = models.CharField(max_length=255,default="Not Specified")
    preparation = models.CharField(max_length=255,null=True, blank=True)
    success_journey = models.TextField(null=True, blank=True)
    daily_routine = models.TextField(null=True, blank=True)
    student_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
        return self.title
    

class Books(models.Model):

    CATEGORY_CHOICES = (
        ('POLICE', 'Police Bharti'),
        ('MPSC', 'MPSC'),
        ('GRAMSEVAK', 'Gramsevak'),
        ('TALATHI', 'Talathi'),
        ('VANRAKSHAK', 'Vanrakshak'),
    )

    category = models.CharField(max_length=20,  null=True, blank=True)
    icon = models.CharField(max_length=100)
    # name = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    upload_book = models.FileField(upload_to='static/ad/images/')


   # gallary page start

class Gallery(models.Model):

    CATEGORY_CHOICES = [
        ('Police Bharti', 'Police Bharti'),
        ('Talathi', 'Talathi'),
        ('Gramsevak', 'Gramsevak'),
        ('Vanrakshak', 'Vanrakshak'),
        ('MPSC', 'MPSC'),
    ]

    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/ad/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# video gallary
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField()

    def __str__(self):
        return self.title



# blogs page start
class Blog(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='static/ad/images/', blank=True, null=True)

    def __str__(self):
        return self.title

class ExamSchedule(models.Model):
    exam_name = models.CharField(max_length=255)
    exam_date = models.CharField(max_length=100)

    def __str__(self):
        return self.exam_name

class CurrentAffair(models.Model):
    date = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title



# contact page start

class Contact_usdahanraj(models.Model):
   btn = models.CharField(max_length=500)
   title = models.CharField(max_length=500)
   dec = models.CharField(max_length=500)
   sub_btn = models.CharField(max_length=500)
   always = models.CharField(max_length=500)
   para = models.CharField(max_length=500)



class Contact_carddahanraj(models.Model):
   icon = models.CharField(max_length=500)
   title = models.CharField(max_length=500)
   dec = models.CharField(max_length=500)
   para = models.CharField(max_length=500)

class Contact_aboutdahanraj(models.Model):
   icon = models.CharField(max_length=500)
   title = models.CharField(max_length=500)
   dec_1 = models.CharField(max_length=500)
   dec_2 = models.CharField(max_length=500)
   dec_3 = models.CharField(max_length=500)

   para = models.CharField(max_length=500)

class Contact_faqdahanraj(models.Model):
   title = models.CharField(max_length=700)
   dec = models.CharField(max_length=2000)


class Contact_AskedQdahanraj(models.Model):
   que = models.CharField(max_length=700)
   ans = models.CharField(max_length=2000)

class Contact_Locationsdahanraj(models.Model):
   title = models.CharField(max_length=500)
   dec = models.CharField(max_length=500)
   academy_name = models.CharField(max_length=500)
   address = models.CharField(max_length=500)
   mobile = models.CharField(max_length=500)
   email = models.CharField(max_length=500)
   time = models.CharField(max_length=500)
   add = models.CharField(max_length=500)

class Course(models.Model):
    course_name = models.CharField(max_length=200)

    def _str_(self):
        return self.course_name