# Generated by Django 2.2.13 on 2020-06-20 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autotest', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testsuiteinfo',
            name='cases',
        ),
        migrations.AddField(
            model_name='testsuiteinfo',
            name='include_cases',
            field=models.CharField(default=None, max_length=500, verbose_name='包含用例列表'),
        ),
    ]