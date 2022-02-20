from django.shortcuts import redirect, render
from .models import *
from .form import QForm
from django.db.models import Q

# Create your views here.
def index(request):
    questions=questionanswer.objects.all()
    univ=university.objects.all()
    dept=department.objects.all()
    subj=subject.objects.all()
    return render(request, 'index.html',{'qu':questions,'un':univ,'de':dept,'su':subj})
def about(request):
    return render(request, 'about.html')
def feedback(request):
    return render(request, 'feedback.html')
def qverify(request):
    return render(request,'q_verify_prompt.html')
def addquestion(request):
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
        que=questionanswer(ques=ques,answer=answer,username=username,university_select_id=university,department_id=department_select,subject_id=subject,year=year,comment=comment,semester=semester,timesAsked=timesAsked,important=important)
        que.save()
        return redirect('/qverify')
    else:
        form=QForm()
    return render(request,'addQ.html',{'form':form})
def search(request):
    univ=university.objects.all()
    dep=department.objects.all()
    sub=subject.objects.all()
    query=None
    qustions=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        qustions=questionanswer.objects.all().filter(Q(ques__icontains=query)|Q(answer__icontains=query)|Q(subject__subject__icontains=query))
    return render(request, 'index.html',{'query':query,'qu':qustions,'un':univ,'de':dep,'su':sub})
#remove on production
def temp(request):
    return render(request, 'tempo.html')
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
        ques=questionanswer.objects.all().filter(Q(university_select_id=uni)&Q(department_id=dept)&Q(subject_id=subj)&Q(semester=sem))
    return render(request,'index.html',{'qu':ques,'un':univ,'de':dep,'su':sub})
def sort(request):
    univ=university.objects.all()
    dep=department.objects.all()
    sub=subject.objects.all()
    st=request.GET.get('sort')
    if st=='recent':
        ques=questionanswer.objects.all().order_by('-year')
    elif st=='asked':
        ques=questionanswer.objects.all().order_by('-timesAsked')
    elif st=='important':
        ques=questionanswer.objects.all().order_by('-important','-timesAsked')
    return render(request,'index.html',{'qu':ques,'un':univ,'de':dep,'su':sub})