from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(university)
admin.site.register(department)
admin.site.register(subject)
admin.site.register(questionanswer)