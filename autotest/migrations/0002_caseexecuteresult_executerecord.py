# Generated by Django 2.2.1 on 2020-05-31 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autotest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseExecuteResult',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('execute_id', models.CharField(max_length=100)),
                ('step_id', models.CharField(max_length=100)),
                ('step_desc', models.CharField(max_length=300)),
                ('result', models.CharField(max_length=100, null=True)),
                ('capture_screen', models.CharField(max_length=500)),
                ('execute_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用例结果表',
                'verbose_name_plural': '用例结果表',
            },
        ),
        migrations.CreateModel(
            name='ExecuteRecord',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('case_id', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100, null=True)),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '运行记录表',
                'verbose_name_plural': '运行记录表',
            },
        ),
    ]