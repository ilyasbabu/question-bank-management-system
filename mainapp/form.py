from django import forms
from .models import questionanswer
from django.forms import NumberInput, TextInput,Select

class QForm(forms.ModelForm):
    class Meta:
        model=questionanswer
        fields=[
            'ques',
            'answer',
            'university',
            'department',
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
            'university':
                Select(attrs={
                    'class':'block rounded border-slate-700 border px-2 w-full h-12'
                    }),
            'department':
                Select(attrs={
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
