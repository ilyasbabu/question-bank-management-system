import json
from django import forms
from .models import *
from django.forms import NumberInput, TextInput,Select

class QForm(forms.ModelForm):
    ddepartments = {}
    list_departments = []
    for department in department.objects.all():
        if department.university.university_name in ddepartments:
            ddepartments[department.university.university_name].append(department.name)
        else:
            ddepartments[department.university.university_name]=[department.name]
        list_departments.append((department.name,department.name))

    universitys = [str(university) for university in university.objects.all()]

    university_select = forms.ChoiceField(widget=Select(attrs={'class':'block rounded border-slate-700 border px-2 w-full h-12'}),choices=([(university, university) for university in universitys]))
    department_select = forms.ChoiceField(widget=Select(attrs={'class':'block rounded border-slate-700 border px-2 w-full h-12'}),choices=(list_departments))

    universitys = json.dumps(universitys)
    departments = json.dumps(ddepartments)
    class Meta:
        model=questionanswer
        fields=[
            'ques',
            'answer',
            'university_select',
            'department_select',
            'subject',
            'year',
        ]
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
