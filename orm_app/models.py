from django.db import models
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(models.Model):
    telegram_id = models.IntegerField(unique=True, null=True, blank=True, help_text='Telegram ID')
    channel_status = models.BooleanField(default=False, help_text='Chanel status', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at', blank=True, null=True)

    def __str__(self):
        return f'{self.telegram_id}'
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Course(models.Model):
    title = models.CharField(max_length=255, help_text='Course title')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons', help_text='Course')
    title = models.TextField(_("Title"), help_text=_("Mazvu nomi yoki text uchun joy!"))
    lesson = models.FileField(upload_to='videos/', help_text='Sizning darsingiz')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Gift(models.Model):
    title = models.TextField(_("Title"), help_text=_("Gift uchun nomi yoki text uchun joy!"))
    gift = models.FileField(upload_to='gifts/', help_text='Gift file')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Gift'
        verbose_name_plural = 'Gifts'


class AdminInfo(models.Model):
    image = models.ImageField(_("Image"), upload_to="user_image/", help_text=_("Admin rasmi"))
    admin_description = models.TextField(_("Admin description"), help_text=_("Admin haqida ma'lumot"))
    admin1_telegram_link = models.TextField(_("Admin 1 telegram link"), help_text=_("Birinchi Admin telegram link"))
    admin2_telegram_link = models.TextField(_("Admin 2 telegram link"), help_text=_("Ikkinchi Admin telegram link"))
    channel_link = models.TextField(_("Channel link"), help_text=_("Kanal link, Bepul Darslar uchun"))
    
    def __str__(self):
        return f'{self.admin_description}'
    
    class Meta:
        verbose_name = 'Admin Info'
        verbose_name_plural = 'Admin Info'
        
class ResultExam(models.Model):
    text = models.TextField(_("Text"), help_text=_("Natija Matni"))
    exam_file = models.FileField(upload_to='exams/', help_text='Exam file')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at', blank=True, null=True)
    
    def __str__(self):
        return f'{self.text}'
    
    
    class Meta:
        verbose_name = 'Exam Result'
        verbose_name_plural = 'Exams Result'
        
class FreeLessonText(models.Model):
    text = models.TextField(_("Text"), help_text=_("Free Lesson Text"))
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at', blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, help_text='Updated at', blank=True, null=True)
    
    def __str__(self):
        return f'{self.text}'
    
    class Meta:
        verbose_name = 'Free Lesson Text'
        verbose_name_plural = 'Free Lesson Texts'
