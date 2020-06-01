# Generated by Django 2.2.1 on 2020-06-01 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autotest', '0010_auto_20200601_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='caseexecuteresult',
            name='capture_screen',
        ),
        migrations.RemoveField(
            model_name='caseexecuteresult',
            name='exception_info',
        ),
        migrations.RemoveField(
            model_name='caseexecuteresult',
            name='execute_end_time',
        ),
        migrations.RemoveField(
            model_name='caseexecuteresult',
            name='execute_start_time',
        ),
        migrations.AddField(
            model_name='executerecord',
            name='capture_screen',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='executerecord',
            name='exception_info',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='executerecord',
            name='execute_end_time',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='执行结束时间'),
        ),
        migrations.AddField(
            model_name='executerecord',
            name='execute_start_time',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='执行开始时间'),
        ),
    ]