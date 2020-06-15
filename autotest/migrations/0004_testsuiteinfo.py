# Generated by Django 2.2.13 on 2020-06-14 08:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autotest', '0003_auto_20200614_1111'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestSuiteInfo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('suite_name', models.CharField(max_length=200, verbose_name='测试集名称')),
                ('include_cases', models.CharField(max_length=200, verbose_name='包含用例id列表')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='编写人员')),
                ('belong_module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autotest.ModuleInfo', verbose_name='所属模块')),
                ('belong_project', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='autotest.ProjectInfo', verbose_name='所属项目')),
            ],
            options={
                'verbose_name': '用例集表',
                'verbose_name_plural': '用例集表',
            },
        ),
    ]