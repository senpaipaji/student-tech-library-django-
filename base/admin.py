from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Course)
admin.site.register(Subject)
admin.site.register(Semester)
admin.site.register(BookLink)
admin.site.register(PyqLink)
admin.site.register(Pyq)
admin.site.register(Topic)
admin.site.register(Video)
admin.site.register(Comment)



