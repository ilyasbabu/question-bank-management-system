from django.shortcuts import redirect, render
from .models import *
from .form import QForm


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def feedback(request):
    return render(request, 'feedback.html')
def qverify(request):
    return render(request,'q_verify_prompt.html')
def addquestion(request):
    form=QForm(request.POST)
    if request.method=='POST':
        ques=request.POST.get('ques')
        answer=request.POST.get('answer')
        university=request.POST.get('university')
        department=request.POST.get('department')
        subject=request.POST.get('subject')
        year=request.POST.get('year')
        que=questionanswer(ques=ques,answer=answer,university_id=university,department_id=department,subject_id=subject,year=year)
        que.save()
        return redirect('/qverify')
    return render(request, 'addQ.html',{"form":form})
#remove on production
def temp(request):
    return render(request, 'tempo.html')