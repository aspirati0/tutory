from django.contrib import admin
from .models import AddProject, Profile, Project, Result, Feedback, CourseProject

# Register your models here.

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(AddProject)
admin.site.register(Result)
admin.site.register(Feedback)
admin.site.register(CourseProject)
