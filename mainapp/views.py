from http.client import HTTPResponse
from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q



# Create your views here.
def home(request):
    questions=questionanswer.objects.all().filter(show=True)
    univ=university.objects.all()
    dept=department.objects.all()
    subj=subject.objects.all()
    return render(request, 'index.html',{
        'qu':questions,
        'un':univ,
        'de':dept,
        'su':subj
        })


def about(request):
    return render(request, 'about.html')

def feedback(request):
    return render(request, 'feedback.html')

def qverify(request):
    return render(request,'q_verify_prompt.html')



def addquestion(request):
    from .form import QForm
    form=QForm(request.POST)
    if request.method=='POST':
        usr=request.user.username
        ques=request.POST.get('ques')
        answer=request.POST.get('answer')
        username=usr
        university=request.POST.get('university_select')
        department_select=request.POST.get('department_select')
        subject=request.POST.get('subject')
        semester=request.POST.get('semester')
        year=request.POST.get('year')
        timesAsked=request.POST.get('timesAsked')
        comment=request.POST.get('comment')
        imp=request.POST.get('important')
        if imp=='on':
            important=True
        else:
            important=False
        que=questionanswer(
            ques=ques,
            answer=answer,
            username=username,
            university_select_id=university,
            department_id=department_select,
            subject_id=subject,
            year=year,
            comment=comment,
            semester=semester,
            timesAsked=timesAsked,
            important=important
            )
        que.save()
        return redirect('/qverify')
    else:
        form=QForm()
    return render(request,'addQ.html',{
        'form':form
        })

def search(request):
    univ=university.objects.all()
    dep=department.objects.all()
    sub=subject.objects.all()
    query=None
    qustions=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        valid=True
        qustions=questionanswer.objects.all().filter(
            # Q(show__contains=valid)&
            Q(ques__icontains=query,show=True)|
            # Q(show__contains=valid)&
            Q(answer__icontains=query,show=True)|
            # Q(show__contains=valid)&
            Q(subject__subject__icontains=query,show=True)
            )
    return render(request, 'index.html',{
        'query':query,
        'qu':qustions,
        'un':univ,
        'de':dep,
        'su':sub
        })
#remove on production

def detail(request,id):
    question=questionanswer.objects.get(id=id)
    return render(request,'details.html',{'qu':question})

def qfeedback(request,id):
    question=questionanswer.objects.get(id=id)
    return render(request,'feedback.html',{'qu':question})

def feedget(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        feed=feedback_m(name=name,email=email,message=message)
        feed.save()
        return redirect('/')
    return render(request,'feedback.html')

def category(request):
    univ=university.objects.all()
    dep=department.objects.all()
    sub=subject.objects.all()
    if request.method=='GET':
        uni=request.GET.get('university')
        dept=request.GET.get('department')
        subj=request.GET.get('subject')
        sem=request.GET.get('semester')
        if uni!='' and dept!='' and subj!='' and sem!='':
            ques=questionanswer.objects.all().filter(Q(university_select_id=uni,show=True)&Q(department_id=dept,show=True)&Q(subject_id=subj,show=True)&Q(semester=sem,show=True))
        elif uni!='' and dept!='' and subj!='':
            ques=questionanswer.objects.all().filter(Q(university_select_id=uni,show=True)&Q(department_id=dept,show=True)&Q(subject_id=subj,show=True))
        elif uni!='' and dept!='' and sem!='':
            ques=questionanswer.objects.all().filter(Q(university_select_id=uni,show=True)&Q(department_id=dept,show=True)&Q(semester=sem,show=True))
        elif uni!='' and subj!='' and sem!='':
            ques=questionanswer.objects.all().filter(Q(university_select_id=uni,show=True)&Q(subject_id=subj,show=True)&Q(semester=sem,show=True))
        elif dept!='' and subj!='' and sem!='':
            ques=questionanswer.objects.all().filter(Q(department_id=dept,show=True)&Q(subject_id=subj,show=True)&Q(semester=sem,show=True))
        elif uni!='' and dept!='':
            ques=questionanswer.objects.all().filter(Q(university_select_id=uni,show=True)&Q(department_id=dept,show=True))
        elif uni!='' and sem!='':
            ques=questionanswer.objects.all().filter(Q(university_select_id=uni,show=True)&Q(semester=sem,show=True))
        elif uni!='' and subj!='':
            ques=questionanswer.objects.all().filter(Q(university_select_id=uni,show=True)&Q(subject_id=subj,show=True))
        elif subj!='' and sem!='':
            ques=questionanswer.objects.all().filter(Q(subject_id=subj,show=True)&Q(semester=sem,show=True))
        elif uni!='':
            ques=questionanswer.objects.all().filter(Q(university_select_id=uni,show=True))
        elif dept!='' and sem!='':
            ques=questionanswer.objects.all().filter(Q(department_id=dept,show=True)&Q(semester=sem,show=True))
        elif dept!='' and subj!='':
            ques=questionanswer.objects.all().filter(Q(department_id=dept,show=True)&Q(subject_id=subj,show=True))
        elif dept!='':
            ques=questionanswer.objects.all().filter(Q(department_id=dept,show=True))
        elif sem!='':
            ques=questionanswer.objects.all().filter(Q(semester=sem,show=True))
        elif subj!='':
            ques=questionanswer.objects.all().filter(Q(subject_id=subj,show=True))
        elif uni=='' and dept=='' and sem=='' and subj=='':
            ques=questionanswer.objects.all().filter(show=True)
    return render(request,'index.html',{
        'qu':ques,
        'un':univ,
        'de':dep,
        'su':sub
        })

def sort(request):
    univ=university.objects.all()
    dep=department.objects.all()
    sub=subject.objects.all()
    st=request.GET.get('sort')
    if st=='recent':
        ques=questionanswer.objects.all().filter(show=True).order_by('-year')
    elif st=='asked':
        ques=questionanswer.objects.all().filter(show=True).order_by('-timesAsked')
    elif st=='important':
        ques=questionanswer.objects.all().filter(show=True).order_by('-important','-timesAsked')
    return render(request,'index.html',{'qu':ques,'un':univ,'de':dep,'su':sub})


# def create_acc(request):
#     if request.method=='POST':
#         fname=request.POST['fname']
#         laname=request.POST['laname']
#         username=request.POST['username']
#         email=request.POST['email']
#         designation=request.POST['designation']
#         university=request.POST['university']
#         college=request.POST['college']
#         phone=request.POST['phone']
#         password=request.POST['password']
#         password1=request.POST['password1']
#         if password==password1:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'Username Taken')
#                 return redirect('/create_acc')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'email already registered')
#                 return redirect('/create_acc')
#             else:
#                 user=User.objects.create_user(username=username,first_name=fname,last_name=laname,email=email,password=password)
#                 user.save()
#                 prof=Profile(username=username,designation=designation,university=university,college=college,phone=phone)
#                 prof.save()
#                 messages.info(request,'User Created')
#         else:
#             print('error in password')
#             messages.info(request,'Password not matching')
#             return redirect('/create_acc')
#     else:
#         return render(request,'signup.html')
#     return render(request,'signup.html')

# def login(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password=request.POST['password']
#         user=auth.authenticate(username=username,password=password)
#         if user is not None:
#             auth.login(request,user)
#             return redirect('/')
#         else:
#             messages.info(request,'Invalid username or password!')
#             return redirect('/login')
#     else:
#         return render(request,'login.html')

# def logout(request):
#     auth.logout(request)
#     return redirect('/')