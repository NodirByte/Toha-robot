import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm.settings")
from django import setup
setup()
from asgiref.sync import sync_to_async

from orm_app import models

@sync_to_async
def get_or_create_user(telegram_id: int):
    user, created = models.User.objects.get_or_create(telegram_id=telegram_id)
    return user, created

@sync_to_async
def get_all_courses():
    courses = models.Course.objects.all()
    return courses

@sync_to_async
def get_course_lessons(course_id: int):
    course = models.Course.objects.get(id=course_id)
    lessons = course.lessons.all()
    return lessons

@sync_to_async
def get_lessons():
    lessons = models.Lesson.objects.all()
    return lessons

@sync_to_async
def get_lesson_by_id(lesson_id: int):
    lesson = models.Lesson.objects.get(id=lesson_id)
    return lesson

@sync_to_async
def get_course_by_id(course_id: int):
    course = models.Course.objects.get(id=course_id)
    return course