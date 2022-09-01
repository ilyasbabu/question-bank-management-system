from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt



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

@csrf_exempt
def print_f(request):
    ids = request.POST.getlist('printQ')
    res = {}
    res['heading'] = "QuestionBank"
    res['data'] = {}
    for counter,i in enumerate(ids,1):
        qa = questionanswer.objects.get(id=i)
        res['data'][counter] = f"""
                                <p>{qa.ques}</p><br>
                                <p>{qa.answer}</p><br>
                                """
    return HttpResponse(res['data'][1])