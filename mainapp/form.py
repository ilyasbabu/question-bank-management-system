import json
from django import forms
from .models import *
from django.forms import NumberInput, TextInput,Select

class QForm(forms.ModelForm):
    ddepartments = {}
    ddeptid = {}
    list_departments = []
    list_deptid = []
    # for department in department.objects.all():
    #     if department.university.university_name in ddepartments:
    #         ddepartments[department.university.university_name].append(department.name)
    #     else:
    #         ddepartments[department.university.university_name]=[department.name]
    #     list_departments.append((department.name,department.name))
    #     if department.university.university_name in ddeptid:
    #         ddeptid[department.university.university_name].append(department.id)
    #     else:
    #         ddeptid[department.university.university_name]=[department.id]
    #     list_deptid.append((department.id,department.id))
    # universitys = [str(university) for university in university.objects.all()]
    # universitysid=[str(university.id) for university in university.objects.all()]
    department_select = forms.ChoiceField(widget=Select(attrs={'class':'block rounded border-slate-700 border px-2 w-full h-12','required':''}),choices=(list_departments))
    timesAsked=forms.CharField(required=False,widget=NumberInput(attrs={'class':'block rounded border-slate-700 border px-2 w-full h-12','placeholder':'no. of times the question has been asked'}))
    comment=forms.CharField(required=False,widget=TextInput(attrs={'class':'block rounded border-slate-700 border px-2 w-full h-12','placeholder':'Enter comments if any'}))
    # universitys = json.dumps(universitys)
    # departments = json.dumps(ddepartments)
    # deptid= json.dumps(ddeptid)
    class Meta:
        model=questionanswer
        fields=[
            'ques',
            'answer',
            'university_select',
            'department_select',
            'subject',
            'semester',
            'year',
            'timesAsked',
            'comment',
            'important',
        ]
        sem=(
        ('',"Select Semester"),
        ('s1',"1st Semester"),
        ('s2',"2nd Semester"),
        ('s3',"3rd Semester"),
        ('s4',"4th Semester"),
        ('s5',"5th Semester"),
        ('s6',"6th Semester"),
        ('s7',"7th Semester"),
        ('s8',"8th Semester"),
    )
        ddepartments = {}
        ddeptid = {}
        list_departments = []
        list_deptid = []
        for department in department.objects.all():
            if department.university.university_name in ddepartments:
                ddepartments[department.university.university_name].append(department.name)
            else:
                ddepartments[department.university.university_name]=[department.name]
            list_departments.append((department.name,department.name))

            if department.university.university_name in ddeptid:
                ddeptid[department.university.university_name].append(department.id)
            else:
                ddeptid[department.university.university_name]=[department.id]
            list_deptid.append((department.id,department.id))
        universitys = [str(university) for university in university.objects.all()]
        universitysid=[str(university.id) for university in university.objects.all()]
        widgets={
            'ques':
                TextInput(attrs={
                    'placeholder':'Enter the question here',
                    'class':'block rounded border-slate-700 border px-2 w-full h-12'
                    }),
            'answer':
                TextInput(attrs={
                    'placeholder':'Enter the answer here',
                    'class':'block rounded border-slate-700 border px-2 w-full h-12'
                    }),
            'university_select':
                Select(attrs={
                    'class':'block rounded border-slate-700 border px-2 w-full h-12'
                },choices=([(university, university) for university in universitys])),
            'department_select':
                Select(attrs={
                    'class':'block rounded border-slate-700 border px-2 w-full h-12'
                },choices=(list_departments)),
            'semester':
                Select(attrs={
                    'class':'block rounded border-slate-700 border px-2 w-full h-12'
                },choices=sem),
            'subject':
                Select(attrs={
                    'class':'block rounded border-slate-700 border px-2 w-full h-12'
                    }),
            'year':
                NumberInput(attrs={
                    'placeholder':'Enter the recent year of the question asked',
                    'class':'block rounded border-slate-700 border px-2 w-full h-12',
                    'min':'2000',
                    'max':'2030'
                    })
        }