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
    # Use Django ORM to fetch all Course objects asynchronously
    courses = list(models.Course.objects.all())
    return courses

@sync_to_async
def get_course_lessons(course_title: str):
    try:
        course_id = models.Course.objects.get(title=course_title).id
        lessons = list(models.Lesson.objects.filter(course_id=course_id))
        return lessons
    except models.Course.DoesNotExist:
        return None
    

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

@sync_to_async
def get_lesson_by_title(title: str):
    lesson = models.Lesson.objects.get(title=title)
    return lesson

@sync_to_async
def get_gift():
    gift = models.Gift.objects.first()
    return gift

@sync_to_async
def get_exam_results():
    exam_results = list(models.ResultExam.objects.all())
    return exam_results

@sync_to_async
def get_channel_link():
    channel_link = models.AdminInfo.objects.first().channel_link
    return channel_link

@sync_to_async
def get_admin1():
    admin1 = models.AdminInfo.objects.first().admin1_telegram_link
    return admin1

@sync_to_async
def get_admin2():
    admin2 = models.AdminInfo.objects.first().admin2_telegram_link
    return admin2

@sync_to_async
def get_admin_description():
    admin_description = models.AdminInfo.objects.first().admin_description
    return admin_description    

@sync_to_async
def get_admin_image():
    admin_image = models.AdminInfo.objects.first().image
    return admin_image

@sync_to_async
def get_all_users():
    users = list(models.User.objects.all())
    return users

@sync_to_async
def get_free_lessons_text():
    free_lessons_text = models.FreeLessonText.objects.first().text
    return free_lessons_text

