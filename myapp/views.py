from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from myapp.models import AddHostel, AddMess, RegisterHostel, StudentFeedback


# Create your views here.



def index(request):
    return render(request, 'pages/index.html')


def adminlogin(request):
    return render(request, 'pages/adminlogin.html')


def studentlogin(request):
    return render(request, 'pages/studentlogin.html')


def studentregister(request):
    return render(request, 'pages/studentregister.html')


def adminhome(request):
    return render(request, 'pages/adminhome.html')


def studentdetails(request):
    studentdata = RegisterHostel.objects.all()
    return render(request, 'pages/studentdetails.html', {'student':studentdata})


def addhostel(request):
    return redirect('/myapp/showhostels')


def addmess(request):
    return redirect('/myapp/showmesses')


def studentfeedback(request):
    feedbacks = StudentFeedback.objects.all()
    return render(request, 'pages/studentfeedback.html', {'feedbacks':feedbacks})


def studenthome(request):
    hostel = AddHostel.objects.all()
    mess = AddMess.objects.all()
    return render(request, 'studentpages/studenthome.html',{'hostel':hostel, 'mess':mess})


def hosteldetails(request):
    print(User.first_name)
    return render(request, 'studentpages/hosteldetails.html')


def messdetails(request):
    return render(request, 'studentpages/messdetails.html')


def feedetails(request):
    return render(request, 'studentpages/feedetails.html')


def addfeedback(request):
    return render(request, 'studentpages/addfeedback.html')


# student register & login functions
def StudentSignup(request):
    if request.method == "POST":
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        username = request.POST.get('uname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmpassword = request.POST.get('cpassword')
        if password == confirmpassword:
            if User.objects.filter(email=email).exists():
                mes = "email already exists"
                return render(request, 'pages/studentregister.html', {'mes': mes})
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username,
                                                email=email, password=password)
                user.save()
                alert = "successfullyy registered"
                return render(request, 'pages/studentregister.html', {'alert': alert})
        else:
            perror = "passwords are not same"
            return render(request, 'pages/studentregister.html', {'perror': perror})
    else:
        pass


def StudentSignin(request):
    if request.method == "POST":
        usersname = request.POST.get('uname')
        passsword = request.POST.get('password')
        if usersname == "puadministrator":
            invalid = "invalid username or password"
            return render(request, 'pages/studentlogin.html', {'invalid': invalid})
        else:
            user = auth.authenticate(username=usersname, password=passsword)
            if user is not None:
                auth.login(request, user)
                return redirect('/myapp/studenthome')
            else:
                wrong = "invalid username or password"
                return render(request, 'pages/studentlogin.html', {'wrong':wrong})
    else:
        return render(request, 'pages/studentlogin.html')


def StudentLogout(request):
    auth.logout(request)
    return redirect('/')


def AdminSignin(request):
    if request.method == "POST":
        usersname = request.POST.get('uname')
        passsword = request.POST.get('password')
        if usersname == "puadministrator":
            user = auth.authenticate(username=usersname, password=passsword)
            if user is not None:
                auth.login(request, user)
                return render(request, 'pages/adminhome.html', {'user': user})
            else:
                invalid = "invalid username or password"
                return render(request, 'pages/adminlogin.html', {'invalid': invalid})
        else:
            admin = "invalid username or password"
            return render(request, 'pages/adminlogin.html', {'admin': admin})
    else:
        return render(request, 'pages/adminlogin.html')


def AdminLogout(request):
    auth.logout(request)
    return redirect('/')


def AddHostels(request):
    if request.method == "POST":
        hostelname = request.POST.get('addhostels')
        try:
            hosteldata = AddHostel(Hostel_name=hostelname)
            hosteldata.save()
            mes = "hostel name added..!"
            return redirect('/myapp/showhostels',)
        except:
            return render(request, 'pages/addhostel.html')

    else:
        return render(request, 'pages/addhostel.html')

def AddMesses(request):
    if request.method == "POST":
        messname = request.POST.get('addmess')
        try:
            messdata = AddMess(Mess_name=messname)
            messdata.save()
            mes = "mess name added..!"
            return redirect('/myapp/showmesses')
        except:
            return render(request, 'pages/addmess.html')
    else:
        return render(request, 'pages/addmess.html')

def showhostels(request):
    hostels = AddHostel.objects.all()
    return render(request, 'pages/addhostel.html', {'hostels':hostels})

def showmesses(request):
    messes = AddMess.objects.all()
    return render(request, 'pages/addmess.html', {'messes':messes})

def deletehostel(request,Hostel_id):
    a = AddHostel.objects.get(Hostel_id=Hostel_id)
    a.delete()
    return redirect('/myapp/showhostels')

def deletemess(request,Mess_id):
    a = AddMess.objects.get(Mess_id=Mess_id)
    a.delete()
    return redirect('/myapp/showmesses')

def registerhostel(request):
    if request.method == "POST":
        s_id = request.POST.get('studentid')
        s_name = request.POST.get('studentname')
        s_semester = request.POST.get('semester')
        s_email = request.POST.get('email')
        s_contact = request.POST.get('contact')
        s_hostel = request.POST.get('choosehostel')
        s_mess = request.POST.get('choosemess')
        if RegisterHostel.objects.filter(studentId=s_id).exists():
            msg = "student already registered"
            return render(request, 'studentpages/alreadyregisteredid.html',{'msg':msg})
        else:
            try:
                reghostel = RegisterHostel(studentId=s_id, studentName=s_name, semester=s_semester, email=s_email, contact=s_contact, HostelName=s_hostel, MessName=s_mess)
                reghostel.save()
                return redirect('/myapp/hosteldetails')
            except:
                return redirect('/myapp/studenthome')
    else:
        return redirect('/myapp/studenthome')

def alreadyregisteredid(request):
    return render(request, 'studentpages/alreadyregisteredid.html')
def searcheddetails(request):
    return render(request, 'studentpages/searched.html')
def messsearched(request):
    return render(request, 'studentpages/messserached.html')

def search(request):
    if request.method == "POST":
        searched = request.POST.get('search')
        if RegisterHostel.objects.filter(studentId=searched).exists():
            item = RegisterHostel.objects.get(studentId=searched)
            hostel = item.HostelName
            name = item.studentName
            mess = item.MessName
            email = item.email
            semester = item.semester
            contact = item.contact
            return render(request, 'studentpages/searched.html', {'item':item, 'searched':searched, 'hostel':hostel,'name':name,'email':email,'semester':semester,'contact':contact})
        else:
            incorrect = "incorrect id"
            return render(request, 'studentpages/searched.html', {'incorrect':incorrect})
    else:
        return render(request, 'studentpages/searched.html')
def searchmess(request):
    if request.method == "POST":
        searched = request.POST.get('search')
        if RegisterHostel.objects.filter(studentId=searched).exists():
            item = RegisterHostel.objects.get(studentId=searched)
            hostel = item.HostelName
            name = item.studentName
            mess = item.MessName
            email = item.email
            semester = item.semester
            contact = item.contact
            return render(request, 'studentpages/messserached.html', {'item':item, 'searched':searched,'name':name,'email':email,'mess':mess,'semester':semester,'contact':contact})
        else:
            incorrect = "incorrect id"
            return render(request, 'studentpages/messserached.html', {'incorrect':incorrect})
    else:
        return render(request, 'studentpages/messserached.html')
def addfeedback(request):
    if request.method == "POST":
        student_id = request.POST.get('sid')
        feedback = request.POST.get('feedback')
        if RegisterHostel.objects.filter(studentId=student_id).exists():
            try:
                a = StudentFeedback(studentid=student_id, feedback=feedback)
                a.save()
                msg = "feedback added"
                return render(request, 'studentpages/addfeedback.html',{'msg':msg})
            except:
                alert = "incorrect id"
                return render(request, 'studentpages/addfeedback.html', {'alert': alert})
        else:
            alert2 = "incorrect id"
            return render(request, 'studentpages/addfeedback.html',{'alert2': alert2})
    else:
        return render(request, 'studentpages/addfeedback.html')

def aboutpage(request):
    return render(request,'pages/about.html')