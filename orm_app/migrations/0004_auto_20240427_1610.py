# Generated by Django 3.2.25 on 2024-04-27 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orm_app', '0003_auto_20240425_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeLessonText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(help_text='Free Lesson Text', verbose_name='Text')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at', null=True)),
            ],
            options={
                'verbose_name': 'Free Lesson Text',
                'verbose_name_plural': 'Free Lesson Texts',
            },
        ),
        migrations.AlterModelOptions(
            name='admininfo',
            options={'verbose_name': 'Admin Info', 'verbose_name_plural': 'Admin Info'},
        ),
        migrations.AlterModelOptions(
            name='resultexam',
            options={'verbose_name': 'Exam Result', 'verbose_name_plural': 'Exams Result'},
        ),
        migrations.AddField(
            model_name='admininfo',
            name='image',
            field=models.ImageField(default=1, help_text='Admin rasmi', upload_to='', verbose_name='Image'),
            preserve_default=False,
        ),
    ]