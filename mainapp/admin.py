from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(university)
admin.site.register(department)
admin.site.register(subject)
class quesAdmin(admin.ModelAdmin):
    list_display=['__str__','subject','username','show']
    list_editable=['show']
admin.site.register(questionanswer,quesAdmin)