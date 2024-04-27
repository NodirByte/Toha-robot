from django.contrib import admin
from orm_app import models

admin.site.register(models.Course)
admin.site.register(models.Lesson)
admin.site.register(models.Gift)
admin.site.register(models.AdminInfo)
admin.site.register(models.ResultExam)
admin.site.register(models.FreeLessonText)

# Path: orm_app/models.py