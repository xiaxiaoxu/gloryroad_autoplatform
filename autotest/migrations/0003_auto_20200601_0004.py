# Generated by Django 2.2.1 on 2020-05-31 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autotest', '0002_caseexecuteresult_executerecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='executerecord',
            old_name='id',
            new_name='execute_id',
        ),
    ]