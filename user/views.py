from django.shortcuts import render,redirect
from adpanel import models as ad
from . import models 
from django.contrib import messages


# Create your views here.
def index(req):
    
    home_courses = ad.mpsccourse.objects.all()[:3]
    profile = ad.Profile.objects.first()
    statistis = ad.Academy_Statistic.objects.all()
    student_data = ad.aboutdahanraj.objects.first()
    data = ad.CompetitionAbout.objects.first()
    why_data = ad.WhyChooseUs.objects.all()
    stats_data = ad.StatsSection.objects.first()
    latest = ad.Latestpage.objects.all()[:3]
    result = ad.Result.objects.all()[:2]
    teacher = ad.Teacher_Profilesdahanraj.objects.all()[:3]
   

    obj = {
        "home_courses":home_courses,
        "profile":profile,
        "statistis":statistis,
        "student_data":student_data,
        "data":data,
        "why_data":why_data,
        "stats_data":stats_data,
        "latest":latest,
        "result":result,
        "teacher":teacher,
    }
    
    return render(req,"user/index.html",obj)


def enroll(req):
    profile = ad.Profile.objects.first()
    Contact_form_cources_data = ad.Course.objects.all()

    obj = {
        "profile":profile,
        "Contact_form_cources_data":Contact_form_cources_data,
    }
   
    return render(req,"user/enroll.html",obj)

def save_enroll(req):
    if req.method == "POST":
        save_enroll = models.StudentEnroll(
            name = req.POST.get('name'),
            dob  = req.POST.get('dob'),
            gender  = req.POST.get('gender'),
            mobile  = req.POST.get('mobile'),
            email  = req.POST.get('email'),
            city  = req.POST.get('city'),
            district  = req.POST.get('district'),
            occupation  = req.POST.get('occupation'),
            qualification  = req.POST.get('qualification'),
            course  = req.POST.get('course'),
            batch  = req.POST.get('batch')

        )
        save_enroll.save()
        messages.success(req, "Form Submit Save Successfully!")
    return redirect('/enroll/')


def about(req):
    profile = ad.Profile.objects.first()
    data = ad.CompetitionAbout.objects.first()
    why_data = ad.WhyChooseUs.objects.all()
    student_data = ad.aboutdahanraj.objects.first()
    stats_data = ad.StatsSection.objects.first()
    obj = {
         "profile":profile,
         "data":data,
         "why_data":why_data,
         "student_data":student_data,
         "stats_data":stats_data,
    }
    return render(req,"user/about.html",obj)

def course(req):
    profile = ad.Profile.objects.first()
    course = ad.mpsccourse.objects.all()
    obj = {
        "course":course,
        "profile":profile,
    }
    return render(req,"user/course.html" ,obj)

def course_mpsc(req,id):
    profile = ad.Profile.objects.first()
    course = ad.mpsccourse.objects.get(id=id)
    obj = {
        "profile":profile,
        "course":course,

    }
    return render(req,"user/course_mpsc.html",obj)

def course_police(req):

    return render(req,"user/course_police.html")

def course_talathi(req):
   
    return render(req,"user/course_talathi.html")
    

def course_vanrakshak(req):
    return render(req,"user/course_vanrakshak.html")


def course_gramsevak(req):
    return render(req,"user/course_gramsevak.html")


def course_allexams(req):
    return render(req,"user/course_allexams.html")


def latest_update(req):
    profile = ad.Profile.objects.first()
    notifications = ad.Latestpage.objects.filter(category='Notification')

    results = ad.Latestpage.objects.filter(category='Result')

    batches = ad.Latestpage.objects.filter( category='New Batch')

    admissions = ad.Latestpage.objects.filter( category='Admission' )

    events = ad.Latestpage.objects.filter( category='Event')
    obj = {
        "profile":profile,
        "notifications":notifications,
        "results":results,
        "batches":batches,
        "admissions":admissions,
        "events":events,
    }
    return render(req,"user/latest_update.html",obj)

def update_detail(request, id):
    profile = ad.Profile.objects.first()
    
    data = ad.Latestpage.objects.get(id=id)

    obj = {
        "profile":profile,
        "data":data,
    }

    return render(
        request,'user/upd1.html',obj)

def upd1(req):
    return render(req,"user/upd1.html")

def upd2(req):
    return render(req,"user/upd2.html")

def upd3(req):
    return render(req,"user/upd3.html")

def upd4(req):
    return render(req,"user/upd4.html")

def upd5(req):
    return render(req,"user/upd5.html")

def upd6(req):
    return render(req,"user/upd6.html")

def upd7(req):
    return render(req,"user/upd7.html")

def upd8(req):
    return render(req,"user/upd8.html")

def upd9(req):
    return render(req,"user/upd9.html")

def upd10(req):
    return render(req,"user/upd10.html")

def upd11(req):
    return render(req,"user/upd11.html")

def upd12(req):
    return render(req,"user/upd12.html")

def upd13(req):
    return render(req,"user/upd13.html")

def upd14(req):
    return render(req,"user/upd14.html")

def upd15(req):
    return render(req,"user/upd15.html")


def book_notes(req):
    profile = ad.Profile.objects.first()
    books_data = ad.Books.objects.all()
    obj = {
        "profile":profile,
        "books_data":books_data,
    }
    return render(req,"user/books_notes.html",obj)

def test_series(req):
    profile = ad.Profile.objects.first()
    obj = {
        "profile":profile,
    }
    return render(req,"user/test_series.html",obj)

def scholarship(req):
    return render(req,"user/scholarship.html")

def result(req):
    profile = ad.Profile.objects.first()
    police_results = ad.Result.objects.filter(category='Police')
    gramsevak_results = ad.Result.objects.filter(category='Gramsevak')
    vanrakshak_results = ad.Result.objects.filter(category='Vanrakshak')
    mpsc_results = ad.Result.objects.filter(category="MPSC")
    talathi_results=ad.Result.objects.filter(category="Talathi")
    obj = {
        "profile":profile,
        "police_results": police_results,
        "gramsevak_results":gramsevak_results,
        "vanrakshak_results":vanrakshak_results,
        "mpsc_results":mpsc_results,
        "talathi_results":talathi_results,


    }
    return render(req,"user/result.html",obj)


def success_story1(req,id):
    profile = ad.Profile.objects.first()
    police_results = ad.Result.objects.filter(category='Police')
    gramsevak_results = ad.Result.objects.filter(category='Gramsevak')
    vanrakshak_results = ad.Result.objects.filter(category='Vanrakshak')
    mpsc_results = ad.Result.objects.filter(category="MPSC")
    talathi_results=ad.Result.objects.filter(category="Talathi")
    obj = {
        "profile":profile,
        "police_results":police_results,
        "gramsevak_results":gramsevak_results,
        "vanrakshak_results":vanrakshak_results,
        "mpsc_results":mpsc_results,
        "talathi_results":talathi_results,
    }
    return render(req,"user/success-story1.html",obj)

def success_story2(req):
    
    return render(req,"user/success-story2.html")

def success_story3(req):
    return render(req,"user/success-story3.html")

def success_story4(req):
    return render(req,"user/success-story4.html")

def success_story5(req):
    return render(req,"user/success-story5.html")

def success_story6(req):
    return render(req,"user/success-story6.html")

def success_story7(req):
    return render(req,"user/success-story7.html")

def success_story8(req):
    return render(req,"user/success-story8.html")

def success_story9(req):
    return render(req,"user/success-story9.html")

def success_story10(req):
    return render(req,"user/success-story10.html")

def success_story11(req):
    return render(req,"user/success-story11.html")

def success_story12(req):
    return render(req,"user/success-story12.html")

def faculty(req):
    profile = ad.Profile.objects.first()
    Teacher_Profiles_data = ad.Teacher_Profilesdahanraj.objects.all()
    Demo_Sessions_data = ad.Demo_Sessionsdahanraj.objects.all()
    Student_Reviews_data = ad.Student_Reviewsdahanraj.objects.all()
    Subject_data = ad.Subjectdahanraj.objects.all()
    obj = {
        "profile":profile,
        "Teacher_Profiles_data":Teacher_Profiles_data,
        "Demo_Sessions_data":Demo_Sessions_data,
        "Student_Reviews_data":Student_Reviews_data,
        "Subject_data":Subject_data,
    }
    return render(req,"user/faculty.html",obj)

def gallary(req):
    profile = ad.Profile.objects.first()
    police = ad.Gallery.objects.filter(category="Police Bharti")
    talathi = ad.Gallery.objects.filter(category="Talathi")
    gramsevak = ad.Gallery.objects.filter(category="Gramsevak")
    vanrakshak = ad.Gallery.objects.filter(category="Vanrakshak")
    mpsc = ad.Gallery.objects.filter(category="MPSC")

    videos = ad.Video.objects.all().order_by('-id')
    obj = {
        "profile":profile,
        'police': police,
        'talathi': talathi,
        'gramsevak': gramsevak,
        'vanrakshak': vanrakshak,
        'mpsc': mpsc,
        'videos': videos,
    }
    return render(req,"user/gallary.html",obj)

def blog(request):
    profile = ad.Profile.objects.first()
    blogs = ad.Blog.objects.all().order_by('-id')

    obj = {
        "profile":profile,
        "blogs":blogs,
    }

    return render(request, 'user/blog.html',obj)


def blog_detail(request):

    exams = ad.ExamSchedule.objects.all().order_by('-id')
    affairs = ad.CurrentAffair.objects.all().order_by('-id')

    return render(request, "user/blog_detail.html", {
        'exams': exams,
        'affairs': affairs
    })

def curruntaffires(req):
    profile = ad.Profile.objects.first()
    # affairs = ad.CurrentAffair.objects.all().order_by('-id')
    obj = {
        "profile":profile,
        # "affairs":affairs,
    }
    return render(req,"user/curruntaffires.html",obj)

def strategyblogs(req):
    profile = ad.Profile.objects.first()
    obj = {
        "profile":profile,
    }
    return render(req,"user/strategyblogs.html",obj)

def preprationblogs(req):
    profile = ad.Profile.objects.first()
    obj = {
        "profile":profile,
    }
    return render(req,"user/preprationblogs.html",obj)

def timetableblogs(req):
    exams = ad.ExamSchedule.objects.all().order_by('-id')
    profile = ad.Profile.objects.first()
    obj = {
        "profile":profile,
        "exams":exams,
    }
    return render(req,"user/timetableblogs.html",obj)

def contact(req):
    profile = ad.Profile.objects.first()
    Contact_us_data = ad.Contact_usdahanraj.objects.all()
    Contact_card_data = ad.Contact_carddahanraj.objects.all()
    Contact_about_data = ad.Contact_aboutdahanraj.objects.all()
    Contact_faq_data = ad.Contact_faqdahanraj.objects.all()
    Contact_AskedQ_data = ad.Contact_AskedQdahanraj.objects.all()
    Contact_Locations_data = ad.Contact_Locationsdahanraj.objects.all()
    Contact_form_cources_data = ad.Course.objects.all()

    obj = {
        "profile":profile,
        "Contact_us_data": Contact_us_data ,
        "Contact_card_data":Contact_card_data,
        "Contact_about_data":Contact_about_data,
        "Contact_faq_data":Contact_faq_data,
        "Contact_AskedQ_data":Contact_AskedQ_data,
        "Contact_Locations_data":Contact_Locations_data,
        "Contact_form_cources_data":Contact_form_cources_data,
    }
    return render(req,"user/contact.html",obj)

def Contact_form_table_save(req):
    if req.method == "POST":
        print(req.POST)
        data = models.Contact_form_tabledahanraj(
            fullname = req.POST.get('fullname'),
            mobile = req.POST.get('mobile'),
            email = req.POST.get('email'),
            mess = req.POST.get('mess'),
            course = req.POST.get('course'),

         
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/contact/')


def Contact_callback_save(req):
    if req.method == "POST":
        data = models.Contact_callbackdahanraj(
            cb_name = req.POST.get('cb_name'),
            cb_mobile = req.POST.get('cb_mobile'),
            cb_time = req.POST.get('cb_time'),
         

         
        )
        data.save()

        return redirect('/contact/')



# blogs 
def blog_timetable(request):
    exams = ad.ExamSchedule.objects.all().order_by('-id')
    profile = ad.Profile.objects.first()

    obj = {
        "exams":exams,
        "profile":profile,

    }

    return render(request, "user/timetable_blogs.html",obj)


def blog_tips(request):
    profile = ad.Profile.objects.first()

    return render(request, "user/tips_blogs.html",{"profile":profile})

def blog_preparation(request):
    profile = ad.Profile.objects.first()

    return render(request, "user/prepration_blog.html",{"profile":profile})

def blog_current_affairs(request):
    affairs = ad.CurrentAffair.objects.all().order_by('-id')
    profile = ad.Profile.objects.first()

    obj = {
        "affairs":affairs,
        "profile":profile,
        
    }

    return render( request,"user/current_affairs_blog.html", obj)