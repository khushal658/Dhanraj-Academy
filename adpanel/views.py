from django.shortcuts import render,redirect,get_object_or_404
import csv
from django.http import HttpResponse
import os
from . import models 
from user import models as us
from django.contrib import messages


# Create your views here.

def login(req):
    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        admin = models.Profile.objects.filter(email = email, password = password).first()

        if admin:
            req.session['user_email'] = email
            req.session['is_login'] = True
            req.session.set_expiry(1800)

            response = redirect('/admin/')
            response.set_cookie('user_email', email, max_age=3600)
            return response
        else:
            return render(req,'admin/login.html',{"error":"Invalid User"})
    return render(req,"admin/login.html")

def logout(req):
    req.session.clear()
    req.session.flush() 
    return redirect('/login/')


def index(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    return render(req,"admin/index.html")


def enrollment(req):
    if not req.session.get('is_login'):
         return redirect('/login/')
    enroll_data = us.StudentEnroll.objects.all()
    return render(req,"admin/enrollment.html",{"enroll_data":enroll_data})

def view_enrollment(req,id):
    if not req.session.get('is_login'):
         return redirect('/login/')
    view_enroll = us.StudentEnroll.objects.get(id=id)
    return render(req,"admin/view_enrollment.html",{"view_enroll":view_enroll})

def delete_enrollment(req,id):
    enrollment = us.StudentEnroll.objects.get(id=id)
    enrollment.delete()
    messages.success(req, "Recorde  Delete Successfully!")

    return redirect('/admin/enrollment/')

def download_enroll_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="enrollments.csv"'

    writer = csv.writer(response)

    writer.writerow([
        'Name',
        'Mobile',
        'Email',
        'DOB',
        'Gender',
        'City',
        'District',
        'Qualification',
        'Course',
        'Batch'
    ])

    enrollments = us.StudentEnroll.objects.all()

    for enroll in enrollments:
        writer.writerow([
            enroll.name,
            enroll.mobile,
            enroll.email,
            enroll.dob,
            enroll.gender,
            enroll.city,
            enroll.district,
            enroll.qualification,
            enroll.course,
            enroll.batch
        ])

    return response



def profile(req):
    if not req.session.get('is_login'):
         return redirect('/login/')
    profile_data = models.Profile.objects.first()
    
    return render(req,"admin/profile.html",{"profile_data":profile_data})

def save_profile(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
       
        profile_data = models.Profile(

        mobile = req.POST.get('mobile'),
        email =req.POST.get('email'),
        password = req.POST.get('password'),
        year = req.POST.get('year'),
        logo =req.FILES.get('logo'),
        academy_name = req.POST.get('academy_name'),
        address = req.POST.get('address'),
        facebook =req.POST.get('facebook'),
        linkdin = req.POST.get('linkdin'),
        twitter = req.POST.get('twitter'),
        youtube = req.POST.get('youtube'),
        instagram = req.POST.get('instagram')
        )
        profile_data.save()

        return redirect('/admin/profile/')
    return render(req,"admin/profile.html")

def update_profile(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    upd_profile = models.Profile.objects.get(id=id)

    if req.method == "POST":
       upd_profile. mobile = req.POST.get('mobile')
       upd_profile.email =req.POST.get('email')
       upd_profile.password = req.POST.get('password')
       upd_profile.year = req.POST.get('year')
       if req.FILES.get('logo'):
            
            if upd_profile.logo:
                old_image = upd_profile.logo.path

                if os.path.exists(old_image):
                    os.remove(old_image)
            

            upd_profile.logo =req.FILES.get('logo')
       upd_profile.academy_name = req.POST.get('academy_name')
       upd_profile.address = req.POST.get('address')
       upd_profile.facebook =req.POST.get('facebook')
       upd_profile.linkdin = req.POST.get('linkdin')
       upd_profile.twitter = req.POST.get('twitter')
       upd_profile.youtube = req.POST.get('youtube')
       upd_profile.instagram = req.POST.get('instagram')
       
       upd_profile.save()
       messages.success(req, "Profile Updated Successfully!")

       return redirect('/admin/profile_list/')
    
    
    return render(req,"admin/update_profile.html",{"upd_profile":upd_profile})

def profile_list(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    profile_data = models.Profile.objects.first()

    return render(req, "admin/profile_list.html", {
        'profile_data': profile_data
    })
        

def academy_statistic(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    statistic = models.Academy_Statistic.objects.all()
    return render( req,"admin/academy_statistics.html",{"statistic":statistic})

def save_statistic(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    
    if req.method == "POST":
        statistic_data = models.Academy_Statistic(

            statistic_title = req.POST.get('statistic_title'),
            statistic_count  = req.POST.get('statistic_count'),
            statistic_icon  = req.POST.get('statistic_icon')
        )

        statistic_data.save()
    return redirect('/admin/academy_statistics/')

def delete_statistic(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_stat = models.Academy_Statistic.objects.get(id=id)
    delete_stat.delete()
    return redirect('/admin/academy_statistics/')

def update_statistic(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update_statistics = models.Academy_Statistic.objects.get(id=id)

    if req.method == "POST":
       

        update_statistics.statistic_title = req.POST.get('statistic_title')
        update_statistics.statistic_count  = req.POST.get('statistic_count')
        update_statistics.statistic_icon  = req.POST.get('statistic_icon')
        

        update_statistics.save()
        messages.success(req, "Statistics Updated Successfully!")
        
        return redirect('/admin/academy_statistics/')

    return render(req,"admin/update_academy_statis.html",{"update_statistics":update_statistics})




def about(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
   
    about_data = models.aboutdahanraj.objects.all()
    
    return render(req,"admin/about.html",{"about_data":about_data})

def about_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
       
        data = models.aboutdahanraj(
            heading = req.POST.get('heading'),
            paragraph = req.POST.get('paragraph'),
            train_number = req.POST.get('train_number'),
           
            stu_num = req.POST.get('selc_stud'),
          
            expfac_num = req.POST.get('expfac_num'),
            
            course_num =req.POST.get('course_num'),
           
        )
        data.save()
        

        return redirect('/admin/about/')
    
def update_about(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.aboutdahanraj.objects.get(id=id)

    if req.method == "POST":
        update.heading = req.POST.get('heading')
        update.paragraph = req.POST.get('paragraph')
        update.train_number = req.POST.get('train_number')
        update.stu_num = req.POST.get('selc_stud')
        update.expfac_num = req.POST.get('expfac_num')
        update.course_num = req.POST.get('course_num')

        update.save()

        return redirect('/admin/about/')
    return render(req,"admin/update_about.html",{"update":update})
    
def delete_about(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.aboutdahanraj.objects.get(id=id)

    delete_data.delete()
    return redirect('/admin/about/')


def maharashtra_compitation(request, id=None):
    if not request.session.get('is_login'):
        return redirect('/login/')

    data = models.CompetitionAbout.objects.first()
    edit_data = None

    if id:
        edit_data = models.CompetitionAbout.objects.get(id=id)

    return render( request, "admin/maharashtra_compitation.html",{'data': data,'edit_data': edit_data})

def delete_compitition(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    data = models.CompetitionAbout.objects.get(id=id)
    data.delete()
    return redirect('/maharashtra_compitation/')


def save_compitition(request):
    if not request.session.get('is_login'):
        return redirect('/login/')

    if request.method == "POST":

        obj = models.CompetitionAbout.objects.first()

        if obj:  # Data pehle se hai to update karo

            obj.main_heading = request.POST.get("main_heading")
            obj.about_description = request.POST.get("about_description")
            obj.vision_description = request.POST.get("vision_description")

            obj.year1 = request.POST.get("year1")
            obj.timeline1 = request.POST.get("timeline1")

            obj.year2 = request.POST.get("year2")
            obj.timeline2 = request.POST.get("timeline2")

            obj.year3 = request.POST.get("year3")
            obj.timeline3 = request.POST.get("timeline3")

            obj.year4 = request.POST.get("year4")
            obj.timeline4 = request.POST.get("timeline4")

            obj.save()

        else:  # Pehli baar save karo

            models.CompetitionAbout.objects.create(
                main_heading=request.POST.get("main_heading"),
                about_description=request.POST.get("about_description"),
                vision_description=request.POST.get("vision_description"),

                year1=request.POST.get("year1"),
                timeline1=request.POST.get("timeline1"),

                year2=request.POST.get("year2"),
                timeline2=request.POST.get("timeline2"),

                year3=request.POST.get("year3"),
                timeline3=request.POST.get("timeline3"),

                year4=request.POST.get("year4"),
                timeline4=request.POST.get("timeline4"),
            )

        return redirect("/admin/maharashtra_compitation/")

    return render(request, "admin/maharashtra_compitation.html")






def student_sucess(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    student_data = models.StatsSection.objects.first()

    edit_data = None

    return render( request,"admin/student_sucess.html",{"student_data": student_data,"edit_data": edit_data } )

def save_stats(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    if request.method == "POST":

        old_data = models.StatsSection.objects.first()

        if old_data:

            old_data.students_number = request.POST.get("students_number")
            old_data.students_label = request.POST.get("students_label")

            old_data.selection_number = request.POST.get("selection_number")
            old_data.selection_label = request.POST.get("selection_label")

            old_data.batch_number = request.POST.get("batch_number")
            old_data.batch_label = request.POST.get("batch_label")

            old_data.course_number = request.POST.get("course_number")
            old_data.course_label = request.POST.get("course_label")

            old_data.experience_number = request.POST.get("experience_number")
            old_data.experience_label = request.POST.get("experience_label")

            old_data.save()

        else:

            models.StatsSection.objects.create(

                students_number=request.POST.get("students_number"),
                students_label=request.POST.get("students_label"),

                selection_number=request.POST.get("selection_number"),
                selection_label=request.POST.get("selection_label"),

                batch_number=request.POST.get("batch_number"),
                batch_label=request.POST.get("batch_label"),

                course_number=request.POST.get("course_number"),
                course_label=request.POST.get("course_label"),

                experience_number=request.POST.get("experience_number"),
                experience_label=request.POST.get("experience_label"),
            )

        return redirect('/admin/student_sucess/')
    
def update_stats(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')

    stats_data = models.StatsSection.objects.first()
    edit_data = models.StatsSection.objects.get(id=id)

    return render(
        request,
        "admin/student_sucess.html",
        {
            "stats_data": stats_data,
            "edit_data": edit_data
        }
    )

def acadamy_speciality(request):
    if not request.session.get('is_login'):
        return redirect('/login/')

    data = models.WhyChooseUs.objects.all()

    return render(request,"admin/acadamy_speciality.html",{'data': data} )


def save_why_choose_us(request):
    if not request.session.get('is_login'):
        return redirect('/login/')

    if request.method == "POST":

        models.WhyChooseUs.objects.create(

            icon=request.POST.get("icon"),

            title=request.POST.get("title"),

            description=request.POST.get("description")

        )

    return redirect('/admin/acadamy_speciality/')


def delete_speciality(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')

    models.WhyChooseUs.objects.get(id=id).delete()

    return redirect('/admin/acadamy_speciality/')





# coursess start


def mpsc_course(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    mpsc = models.mpsccourse.objects.all() 
    return render(req,"admin/Mpsc_course.html",{"mpsc":mpsc})

def save_mpsc(req):
    if req.method == "POST":

        mpsc = models.mpsccourse(
            department = req.POST.get('department'),
            course_name = req.POST.get('course_name'),
            duration  = req.POST.get('duration'),
            fees = req.POST.get('fees'),
            timing = req.POST.get('timing'),
            # mode = req.POST.get('mode'),
            extra_label = req.POST.get('extra_label'),
            extra_value = req.POST.get('extra_value'),


            # course info
            heading = req.POST.get('heading'),
            title = req.POST.get('title'),
            eligibility = req.POST.get('eligibility'),
           
            benefit1 = req.POST.get('benefit1'),
            benefit2 = req.POST.get('benefit2'),
            benefit3 = req.POST.get('benefit3'),
            benefit4 = req.POST.get('benefit4'),
            benefit5 = req.POST.get('benefit5'),
            admission_notice = req.POST.get('admission_notice'),
           
        )
        mpsc.save()
        messages.success(req,"Course Save Successfully!")
    return redirect('mpsc_course')

def delete_mpsc(req,id):
    delete_mpsc = get_object_or_404(models.mpsccourse,id=id)
    delete_mpsc.delete()
    messages.success(req,"Course Delete Successfully!")
    return redirect('/admin/course_list/')

def update_mpsc_courses(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update_course = models.mpsccourse.objects.get(id=id)


    if req.method == "POST":

        update_course.department = req.POST.get('department')
        update_course.course_name = req.POST.get('course_name')
        update_course.duration  = req.POST.get('duration')
        update_course.fees = req.POST.get('fees')
        update_course.timing = req.POST.get('timing')
        # update_course.mode = req.POST.get('mode')
        update_course.extra_label = req.POST.get('extra_label')
        update_course.extra_value = req.POST.get('extra_value')
        update_course.heading = req.POST.get('heading')
        update_course.title = req.POST.get('title')
        update_course.eligibility = req.POST.get('eligibility')
        update_course.benefit1 = req.POST.get('benefit1')
        update_course.benefit2 = req.POST.get('benefit2')
        update_course.benefit3 = req.POST.get('benefit3')
        update_course.benefit4 = req.POST.get('benefit4')
        update_course.benefit5 = req.POST.get('benefit5')
        update_course.admission_notice = req.POST.get('admission_notice')



        update_course.save()
        messages.success(req,"Course Update Successfully!")

        return redirect('/admin/course_list/')

    return render(req,"admin/update_mpsc_course.html",{"update_course":update_course})

def course_list(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    mpsc = models.mpsccourse.objects.all()
   
    return render(req,"admin/course_list.html",{"mpsc":mpsc})

# teacher page start here 
def Teacher_Profiles(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    Teacher_Profiles_data = models.Teacher_Profilesdahanraj.objects.all()
    
    return render(req,"admin/Teacher_Profiles.html",{"Teacher_Profiles_data":Teacher_Profiles_data})

def Teacher_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Teacher_Profilesdahanraj(
            images = req.FILES.get('images'),
            fullname = req.POST.get('fullname'),
            traner = req.POST.get('traner'),
            experience = req.POST.get('experience'),
            linkedin = req.POST.get('linkedin'),
            instagram = req.POST.get('instagram'),
            twitter = req.POST.get('twitter'),
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Teacher_Profiles/')
    
def update_Teacher_Profiles(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Teacher_Profilesdahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        if req.FILES.get('images'):
            update.images = req.FILES.get('images')
        update.fullname = req.POST.get('fullname')
        update.traner = req.POST.get('traner')
        update.experience = req.POST.get('experience')
        update.linkedin = req.POST.get('linkedin')
        update.instagram = req.POST.get('instagram')
        update.twitter = req.POST.get('twitter')

        
        

        update.save()

        return redirect('/Teacher_Profiles/')
    return render(req,"admin/update_Teacher_Profiles.html",{"update":update})
    
def Delete_Teacher_Profiles(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.Teacher_Profilesdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Teacher_Profiles/')


# demo session page start

def Demo_Sessions(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    Demo_Sessions_data = models.Demo_Sessionsdahanraj.objects.all()
    return render(req,"admin/Demo_Sessions.html",{"Demo_Sessions_data":Demo_Sessions_data})


def Demo_Sessions_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Demo_Sessionsdahanraj(
            dec = req.POST.get('dec'),
            title = req.POST.get('title'),
            sub_btn = req.POST.get('sub_btn'),
            sub_dec = req.POST.get('sub_dec'),
            sub_video = req.FILES.get('sub_video'),
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Demo_Sessions/')
    
def update_Demo_Sessions(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Demo_Sessionsdahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        update.dec = req.POST.get('dec')
        update.title = req.POST.get('title')
        update.sub_btn = req.POST.get('sub_btn')
        update.sub_dec = req.POST.get('sub_dec')
        if req.FILES.get('sub_video'):
            update.sub_video = req.FILES.get('sub_video')
        update.save()

        return redirect('/Demo_Sessions/')
    return render(req,"admin/update_Demo_Sessions.html",{"update":update})
    
def Delete_Demo_Sessions(req,id):
    delete_data = models.Demo_Sessionsdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Demo_Sessions/')


# student review start

def Student_Reviews(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    Student_Reviews_data = models.Student_Reviewsdahanraj.objects.all()
    return render(req,"admin/Student_Reviews.html",{"Student_Reviews_data":Student_Reviews_data})

def Student_Reviews_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Student_Reviewsdahanraj(
            images = req.FILES.get('images'),
            fullname = req.POST.get('fullname'),
            traner = req.POST.get('traner'),
            icon = req.POST.get('icon'),
            dec = req.POST.get('dec'),
         
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Student_Reviews/')
    
def update_Student_Reviews(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Student_Reviewsdahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        if req.FILES.get('images'):
            update.images = req.FILES.get('images')
        update.fullname = req.POST.get('fullname')
        update.traner = req.POST.get('traner')
        update.icon = req.POST.get('icon')
        update.dec = req.POST.get('dec')

        
        

        update.save()

        return redirect('/Student_Reviews/')
    return render(req,"admin/update_Student_Reviews.html",{"update":update})
    
def Delete_Student_Reviews(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.Student_Reviewsdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Student_Reviews/')


# subject experties
def Subject(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
   
    Subject_data = models.Subjectdahanraj.objects.all()
    
    return render(req,"admin/Subject.html",{"Subject_data":Subject_data})

def Subject_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Subjectdahanraj(
          
           
            title = req.POST.get('title'),
            dec = req.POST.get('dec'),
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Subject/')
    
def update_Subject(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Subjectdahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        update.title = req.POST.get('title')
        update.dec = req.POST.get('dec')

        
        

        update.save()

        return redirect('/Subject/')
    return render(req,"admin/update_Subject.html",{"update":update})
    
def Delete_Subject(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.Subjectdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Subject/')


# Latest update file start

def latest_page(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    data = models.Latestpage.objects.all()
    return render(request, "admin/Latest_page.html", {'data': data})


def latestpage_upadate(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    if request.method == "POST":

        # Image Validation
        image = request.FILES.get("slider_image")

        if image:

            allowed = ["image/jpeg", "image/png", "image/webp"]

            if image.content_type not in allowed:
                messages.error(request, "Only image files are allowed.")
                return redirect("/latest_page/")

        print("POST DATA =", request.POST)
        print("FILES =", request.FILES)

        data = models.Latestpage(

            # Card Data
            category=request.POST.get('category'),
            heading=request.POST.get('heading'),
            heading_description=request.POST.get('heading_description'),
            dob=request.POST.get('dob'),
            slider_image=image,

            # Hero Section
            badge_text=request.POST.get('badge_text'),
            hero_heading=request.POST.get('hero_heading'),
            hero_description=request.POST.get('hero_description'),

            # Overview
            overview_title=request.POST.get('overview_title'),
            overview_description=request.POST.get('overview_description'),

            # Physical Test
            physical_title=request.POST.get('physical_title'),
            physical_point_1=request.POST.get('physical_point_1'),
            physical_point_2=request.POST.get('physical_point_2'),
            physical_point_3=request.POST.get('physical_point_3'),
            physical_point_4=request.POST.get('physical_point_4'),
            physical_point_5=request.POST.get('physical_point_5'),

            # Written Exam
            written_title=request.POST.get('written_title'),
            written_point_1=request.POST.get('written_point_1'),
            written_point_2=request.POST.get('written_point_2'),
            written_point_3=request.POST.get('written_point_3'),
            written_point_4=request.POST.get('written_point_4'),
            written_point_5=request.POST.get('written_point_5'),

            # Selection Process
            selection_title=request.POST.get('selection_title'),
            selection_description=request.POST.get('selection_description'),

            step1_title=request.POST.get('step1_title'),
            step1_description=request.POST.get('step1_description'),

            step2_title=request.POST.get('step2_title'),
            step2_description=request.POST.get('step2_description'),

            step3_title=request.POST.get('step3_title'),
            step3_description=request.POST.get('step3_description'),

            step4_title=request.POST.get('step4_title'),
            step4_description=request.POST.get('step4_description'),
        )

        data.save()

        messages.success(request, "Record Saved Successfully.")

        return redirect('/latest_page/')

    return redirect('/latest_page/')

    if not request.session.get('is_login'):
        return redirect('/login/')

    if request.method == "POST":

        print("POST DATA =", request.POST)
        print("FILES =", request.FILES)

        data = models.Latestpage(

            # Card Data
            category=request.POST.get('category'),
            heading=request.POST.get('heading'),
            heading_description=request.POST.get('heading_description'),
            dob=request.POST.get('dob'),
            slider_image=request.FILES.get('slider_image'),

            # Hero Section
            badge_text=request.POST.get('badge_text'),
            hero_heading=request.POST.get('hero_heading'),
            hero_description=request.POST.get('hero_description'),

            # Overview
            overview_title=request.POST.get('overview_title'),
            overview_description=request.POST.get('overview_description'),

            # Physical Test
            physical_title=request.POST.get('physical_title'),
            physical_point_1=request.POST.get('physical_point_1'),
            physical_point_2=request.POST.get('physical_point_2'),
            physical_point_3=request.POST.get('physical_point_3'),
            physical_point_4=request.POST.get('physical_point_4'),
            physical_point_5=request.POST.get('physical_point_5'),

            # Written Exam
            written_title=request.POST.get('written_title'),
            written_point_1=request.POST.get('written_point_1'),
            written_point_2=request.POST.get('written_point_2'),
            written_point_3=request.POST.get('written_point_3'),
            written_point_4=request.POST.get('written_point_4'),
            written_point_5=request.POST.get('written_point_5'),

            # Selection Process
            selection_title=request.POST.get('selection_title'),
            selection_description=request.POST.get('selection_description'),

            step1_title=request.POST.get('step1_title'),
            step1_description=request.POST.get('step1_description'),

            step2_title=request.POST.get('step2_title'),
            step2_description=request.POST.get('step2_description'),

            step3_title=request.POST.get('step3_title'),
            step3_description=request.POST.get('step3_description'),

            step4_title=request.POST.get('step4_title'),
            step4_description=request.POST.get('step4_description'),
        )

        data.save()
        messages.success(request, "Record Saved Successfully.")

        return redirect('/Latest_page/')

    return redirect('/Latest_page/')

# from django.shortcuts import redirect, get_object_or_404

def delete_latestpage(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')

    data = models.Latestpage.objects.get(id=id)

    if data.slider_image:
        data.slider_image.delete()

    data.delete()

    return redirect('/Latest_page/')





# result start
def result(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    
    police_results = models.Result.objects.filter(category='Police')
    gramsevak_results = models.Result.objects.filter(category='Gramsevak')
    vanrakshak_results = models.Result.objects.filter(category='Vanrakshak')
    mpsc_results = models.Result.objects.filter(category='MPSC')
    talathi_results = models.Result.objects.filter(category='Talathi')

    return render(
        request,
        'user/result.html',
        {
            'police_results': police_results,
            'gramsevak_results': gramsevak_results,
            "vanrakshak_results": vanrakshak_results,
            "mpsc_results": mpsc_results,
            "talathi_results": talathi_results
        }
    )





def save_result(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method== "POST":
       
        data = models.Result(
            
            category=req.POST.get('category'),
            image = req.FILES.get('image'),
            name = req.POST.get('name'),
            year = req.POST.get('year'),
            rank = req.POST.get('rank'),

            title= req.POST.get('title'),
            post=req.POST.get('post'),
            education=req.POST.get('education'),
            posting=req.POST.get('posting'),
            preparation=req.POST.get('preparation'),
            success_journey=req.POST.get('success_journey'),
            daily_routine=req.POST.get('daily_routine'),
            student_message=req.POST.get('student_message'),

        )
        data.save()
        messages.success(req,"Result Save Successfully!")
       

    return redirect('/admin/result/')

def success_story(request, id):
    # if not request.session.get('is_login'):
    #     return redirect('/login/')
    result = models.Result.objects.get(id=id)

    profile = models.Profile.objects.first()

    obj = {
        "result":result,
        "profile":profile,
    }


    return render(
        request,
        'user/success_story.html',obj)


def edit_result(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    result = models.Result.objects.get(id=id)
    return render(req,"admin/update_result.html" ,{"result":result})


def update_result(req, id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    result = models.Result.objects.get(id=id)

    if req.method == "POST":

        result.name = req.POST.get('name')
        result.year = req.POST.get('year')
        result.rank = req.POST.get('rank')
        result.category = req.POST.get('category')

        if req.FILES.get('image'):
            result.image = req.FILES.get('image')
        result.title = req.POST.get('title')
        # result.subtitle = req.POST.get('subtitle')
        result.post = req.POST.get('post')
        result.education = req.POST.get('education')
        result.posting = req.POST.get('posting')
        result.preparation = req.POST.get('preparation')
        result.success_journey = req.POST.get('success_journey')
        result.daily_routine = req.POST.get('daily_routine')
        result.student_message = req.POST.get('student_message')
        result.save()

        messages.success(req,"Update Result Successfully!")

        return redirect('/admin/result/')   

    return render(req, "admin/update_result.html", {"result": result})



def delete_result(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    result= models.Result.objects.get(id=id)
    if result.image:
        if os.path.isfile(result.image.path):
            os.remove(result.image.path)
    result.delete()
    messages.success(req,"Delete Data Successfully!")
    return redirect("/admin/result/")



def admin_result(request):
   if not request.session.get('is_login'):
        return redirect('/login/')
   result = models.Result.objects.all()
   return render(request,"admin/result.html",{"result":result})


# books and notes start here


def books(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    books_data = models.Books.objects.all()
    # print("ADMIN COUNT =", data.count())
    return render(
        req,
        "admin/books_notes.html",
        {"book_data": books_data}
    )


def books_save(req):

    if req.method == "POST":

        models.Books.objects.create(
            category=req.POST.get('category'),
            icon=req.POST.get('icon'),
            book_name=req.POST.get('book_name'),
            upload_book=req.FILES.get('upload_book')
        )

        messages.success(req, "Data Save Successfully!")


    return redirect('book')


def update_book(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    book = models.Books.objects.get(id=id)

    if request.method == "POST":

        book.category = request.POST.get('category')
        book.icon = request.POST.get('icon')
        book.name = request.POST.get('name')
        book.book_name = request.POST.get('book_name')

        if request.FILES.get('upload_book'):
            book.upload_book = request.FILES.get('upload_book')

        book.save()

        messages.success(request, "Data Updated Successfully!")

        return redirect('book')

    context = {
        'book': book
    }

    return render(request, 'admin/update_book.html', context)


def delete_book(req, id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    data = models.Books.objects.get(id=id)
    if data.upload_book:
        if os.path.isfile(data.upload_book.path):
            os.remove(data.upload_book.path)
    data.delete()
    messages.success(req, "Data Deleted Successfully!")
    return redirect('book')



# gallary page start

def photo_gallary(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    data = models.Gallery.objects.all().order_by('-id')
    return render(request, "admin/photo_gallary.html", {'data': data})
def save_gallary(request):

    if request.method == "POST":

        models.Gallery.objects.create(
            category=request.POST.get('category'),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            image=request.FILES.get('image')
        )

    return redirect('/admin/photo_gallary/')     


def edit_gallery(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    data = models.Gallery.objects.get(id=id)

    if request.method == "POST":
        data.category = request.POST.get('category')
        data.title = request.POST.get('title')
        data.description = request.POST.get('description')

        if request.FILES.get('image'):
            data.image = request.FILES.get('image')

        data.save()
        return redirect('photo_gallary')

    return render(request, "admin/photo_gallary.html", {'data': data})


def delete_gallery(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    data = models.Gallery.objects.get(id=id)
    data.delete()
    return redirect('photo_gallary')


def edit_gallery(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    data = models.Gallery.objects.get(id=id)

    if request.method == "POST":

        data.category = request.POST.get('category')
        data.title = request.POST.get('title')
        data.description = request.POST.get('description')

        if request.FILES.get('image'):
            data.image = request.FILES.get('image')

        data.save()

        return redirect('photo_gallary')

    return render(request, "admin/edit_gallery.html", {'data': data})


def video_gallary(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    data = models.Video.objects.all().order_by('-id')
    return render(request, "admin/video_gallary.html",{'data': data})


def add_video(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    if request.method == "POST":
        models.Video.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            video_url=request.POST.get('video_url')
        )
        return redirect('/add_video/')

    # data = models.Video.objects.all().order_by('-id')
    return render(request, "admin/video_gallary.html")


def delete_video(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    video = models.Video.objects.get(id=id)
    video.delete()
    return redirect('/add_video/')

def edit_video(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    video = models.Video.objects.get(id=id)

    if request.method == "POST":
        video.title = request.POST.get('title')
        video.description = request.POST.get('description')
        video.video_url = request.POST.get('video_url')
        video.save()

        return redirect('/admin/video_gallary/')

    return render(request, "admin/edit_video.html", {'video': video})



# blog page start here

 # blogs
def blog_card(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    blogs = models.Blog.objects.all()
    return render(request, 'admin/blog_card.html', {'blogs': blogs})

def save_blog(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    if request.method == "POST":
        models.Blog.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            image=request.FILES.get('image')
        )
    return redirect('blog_card')
    # edit ani delete
def delete_blog(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    blog =  models.Blog.objects.get(id=id)
    blog.delete()
    return redirect('blog_card')

    # 
def read_more1(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    all_data = models.ExamSchedule.objects.all().order_by('-id')
    return render(request, 'admin/read_more1.html', {'all_data': all_data})


def exam(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    if request.method == "POST":

        models.ExamSchedule.objects.create(
            exam_name=request.POST.get('exam_name'),
            exam_date=request.POST.get('exam_date')
        )

    return redirect('read_more1')

def delete_exam(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    data = models.ExamSchedule.objects.get(id=id)
    data.delete()
    return redirect('read_more1')


def read_more2(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    all_data = models.CurrentAffair.objects.all().order_by('-id')

    return render(
        request,
        'admin/read_more2.html',
        {'all_data': all_data}
    )
def question(request):
    if not request.session.get('is_login'):
        return redirect('/login/')
    if request.method == "POST":

        models.CurrentAffair.objects.create(
            date=request.POST.get('date'),
            title=request.POST.get('title'),
            description=request.POST.get('description')
        )

    return redirect('read_more2')

def delete_affair(request, id):
    if not request.session.get('is_login'):
        return redirect('/login/')
    data = models.CurrentAffair.objects.get(id=id)
    data.delete()

    return redirect('read_more2')




# contact page start

def Contact_us(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    Contact_us_data = models.Contact_usdahanraj.objects.all()
    return render(req,"admin/Contact_us.html",{"Contact_us_data":Contact_us_data})

def Contact_us_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Contact_usdahanraj(
            btn = req.POST.get('btn'),
            title = req.POST.get('title'),
            dec = req.POST.get('dec'),
            sub_btn = req.POST.get('sub_btn'),
            para = req.POST.get('para'),
            always = req.POST.get('always'),


         
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Contact_us/')
    
def Update_Contact_us(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Contact_usdahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        update.btn = req.POST.get('btn')
        update.title = req.POST.get('title')
        update.dec = req.POST.get('dec')
        update.sub_btn = req.POST.get('sub_btn')
        update.always = req.POST.get('always')
        update.para = req.POST.get('para')


        
        update.save()

        return redirect('/Contact_us/')
    return render(req,"admin/Update_Contact_us.html",{"update":update})
    
def Delete_Contact_us(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.Contact_usdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")


    delete_data.delete()
    return redirect('/Contact_us/')







def Contact_card(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    Contact_card_data = models.Contact_carddahanraj.objects.all()
    return render(req,"admin/Contact_card.html",{"Contact_card_data":Contact_card_data})

def Contact_card_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Contact_carddahanraj(
            icon = req.POST.get('icon'),
            title = req.POST.get('title'),
            dec = req.POST.get('dec'),
            para = req.POST.get('para'),


         
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Contact_card/')
    
def Update_Contact_card(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Contact_carddahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        update.icon = req.POST.get('icon')
        update.title = req.POST.get('title')
        update.dec = req.POST.get('dec')
        update.para = req.POST.get('para')


        
        update.save()

        return redirect('/Contact_card/')
    return render(req,"admin/Update_Contact_card.html",{"update":update})
    
def Delete_Contact_card(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.Contact_carddahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Contact_card/')


def Contact_about(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    Contact_about_data = models.Contact_aboutdahanraj.objects.all()
    return render(req,"admin/Contact_about.html",{"Contact_about_data":Contact_about_data})

def Contact_about_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Contact_aboutdahanraj(
            icon = req.POST.get('icon'),
            title = req.POST.get('title'),
            dec_1 = req.POST.get('dec_1'),
            dec_2 = req.POST.get('dec_2'),
            dec_3 = req.POST.get('dec_3'),
            para = req.POST.get('para'),


         
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Contact_about/')
    
def Update_Contact_about(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Contact_aboutdahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        update.icon = req.POST.get('icon')
        update.title = req.POST.get('title')
        update.dec_1 = req.POST.get('dec_1')
        update.dec_2 = req.POST.get('dec_2')
        update.dec_3 = req.POST.get('dec_3')

        update.para = req.POST.get('para')


        
        update.save()

        return redirect('/Contact_about/')
    return render(req,"admin/Update_Contact_about.html",{"update":update})
    
def Delete_Contact_about(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.Contact_aboutdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Contact_about/')

# contact form

def Contact_form_table(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    Contact_form_table_data = us.Contact_form_tabledahanraj.objects.all()
    return render(req,"admin/Contact_form_table.html",{"Contact_form_table_data":Contact_form_table_data})

# new changes
def update_contact_status(request, id):
    if request.method == "POST":
        obj = us.Contact_form_tabledahanraj.objects.get(id=id)
        obj.status = request.POST.get("status")
        obj.save()

    return redirect('/Contact_form_table/')
    
def Delete_Contact_form_table(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = us.Contact_form_tabledahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Contact_form_table/')


def Contact_callback(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    Contact_callback_data = us.Contact_callbackdahanraj.objects.all()
    return render(req,"admin/Contact_callback.html",{"Contact_callback_data":Contact_callback_data})


    
def update_callback_status(request, id):
    if request.method == "POST":
        obj = us.Contact_callbackdahanraj.objects.get(id=id)
        obj.status = request.POST.get("status")
        obj.save()
    return redirect('/Contact_callback/')
    
def Delete_Contact_callback(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = us.Contact_callbackdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Contact_callback/')

# contact faq

def Contact_faq(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
   
    Contact_faq_data = models.Contact_faqdahanraj.objects.all()
    
    return render(req,"admin/Contact_faq.html",{"Contact_faq_data":Contact_faq_data})

def Contact_faq_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Contact_faqdahanraj(
          
           
            title = req.POST.get('title'),
            dec = req.POST.get('dec'),
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Contact_faq/')
    
def Update_Contact_faq(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Contact_faqdahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        update.title = req.POST.get('title')
        update.dec = req.POST.get('dec')

        
        

        update.save()

        return redirect('/Contact_faq/')
    return render(req,"admin/Update_Contact_faq.html",{"update":update})
    
def Delete_Contact_faq(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.Contact_faqdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Contact_faq/')


# questions faq

def Contact_AskedQ(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
   
    Contact_AskedQ_data = models.Contact_AskedQdahanraj.objects.all()
    
    return render(req,"admin/Contact_AskedQ.html",{"Contact_AskedQ_data":Contact_AskedQ_data})

def Contact_AskedQ_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Contact_AskedQdahanraj(
          
           
            que = req.POST.get('que'),
            ans = req.POST.get('ans'),
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Contact_AskedQ/')
    
def Update_Contact_AskedQ(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Contact_AskedQdahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        update.que = req.POST.get('que')
        update.ans = req.POST.get('ans')

        
        

        update.save()

        return redirect('/Contact_AskedQ/')
    return render(req,"admin/Update_Contact_AskedQ.html",{"update":update})
    
def Delete_Contact_AskedQ(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.Contact_AskedQdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Contact_AskedQ/')


def Contact_Locations(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    Contact_Locations_data = models.Contact_Locationsdahanraj.objects.all()
    return render(req,"admin/Contact_Locations.html",{"Contact_Locations_data":Contact_Locations_data})

def Contact_Locations_save(req):
    if not req.session.get('is_login'):
        return redirect('/login/')
    if req.method == "POST":
        print(req.POST)
        data = models.Contact_Locationsdahanraj(
            title = req.POST.get('title'),
            dec = req.POST.get('dec'),
            academy_name = req.POST.get('academy_name'),
            address = req.POST.get('address'),
            mobile = req.POST.get('mobile'),
            email = req.POST.get('email'),
            time = req.POST.get('time'),
            add = req.POST.get('add'),
           


         
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Contact_Locations/')
    
def Update_Contact_Locations(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    update = models.Contact_Locationsdahanraj.objects.get(id=id)
    messages.success(req, "Record Updated Successfully")

    if req.method == "POST":
        update.title = req.POST.get('title')
        update.dec = req.POST.get('dec')
        update.academy_name = req.POST.get('academy_name')
        update.address = req.POST.get('address')
        update.mobile = req.POST.get('mobile')
        update.email = req.POST.get('email')
        update.email = req.POST.get('email')
        update.time = req.POST.get('time')
        update.add = req.POST.get('add')



        update.para = req.POST.get('para')


        
        update.save()

        return redirect('/Contact_Locations/')
    return render(req,"admin/Update_Contact_Locations.html",{"update":update})
    
def Delete_Contact_Locations(req,id):
    if not req.session.get('is_login'):
        return redirect('/login/')
    delete_data = models.Contact_Locationsdahanraj.objects.get(id=id)
    messages.success(req, "Record Deleted Successfully")

    delete_data.delete()
    return redirect('/Contact_Locations/')







def Contact_form_cources(req):
    Contact_form_cources_data = models.Course.objects.all()
    return render(req,"admin/Contact_form_cources.html",{"Contact_form_cources_data":Contact_form_cources_data})

def Contact_form_cources_save(req):
    if req.method == "POST":
        print(req.POST)
        data = models.Course(
            course_name = req.POST.get('course_name'), 
        )
        data.save()
        print("Saved Successfully!")

        return redirect('/Contact_form_cources/')
    
def update_contact_form_course(req,id):
    update = models.Course.objects.get(id=id)


    if req.method == "POST":
        update.course_name = req.POST.get('course_name')
        update.save()
        messages.success(req, "Course Updated Successfully!")

        return redirect('/Contact_form_cources/')
        
    return render(req,"admin/update_contact_form_course.html",{"update":update})
    
def Delete_Contact_form_cources(req,id):
    messages.success(req, "Record Deleted Successfully")

    delete_data = models.Course.objects.get(id=id)

    delete_data.delete()
    return redirect('/Contact_form_cources/')



