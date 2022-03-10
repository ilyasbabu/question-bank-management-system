from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(university)
admin.site.register(department)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('__str__','department')
admin.site.register(subject,SubjectAdmin)

class quesAdmin(admin.ModelAdmin):
    list_display=['__str__','subject','username','show']
    list_editable=['show']
    list_filter=['subject','username']
    search_fields=['ques','answer','subject__subject']
admin.site.register(questionanswer,quesAdmin)

class feedbackAdmin(admin.ModelAdmin):
    list_display=['__str__','name','email']
admin.site.register(feedback_m,feedbackAdmin)



admin.site.site_header = 'QUESTION BANK'
admin.site.site_title = 'ADMIN PANEL'
admin.site.index_title= 'Welcome to Question Bank Admin'