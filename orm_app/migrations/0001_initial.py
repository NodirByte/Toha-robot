# Generated by Django 5.0.3 on 2024-03-29 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.IntegerField(blank=True, help_text='Telegram ID', null=True, unique=True)),
                ('channel_status', models.BooleanField(blank=True, default=False, help_text='Chanel status', null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at', null=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
        ),
    ]
