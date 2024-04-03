from django.db import models

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
    title = models.CharField(max_length=255, help_text='Lesson title')
    lesson = models.FileField(upload_to='videos/', help_text='Video')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'


class Gift(models.Model):
    title = models.CharField(max_length=255, help_text='Gift title')
    gift = models.FileField(upload_to='gifts/', help_text='Gift file')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Created at', blank=True, null=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Gift'
        verbose_name_plural = 'Gifts'

