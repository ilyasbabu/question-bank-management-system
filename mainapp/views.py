from django.shortcuts import redirect, render
from .models import *
from .form import QForm

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
#remove on production
def temp(request):
    return render(request, 'tempo.html')