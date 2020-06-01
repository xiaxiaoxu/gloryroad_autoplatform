from django.contrib import admin

# Register your models here.
from autotest.models import ProjectInfo, ModuleInfo, TestCaseInfo, CaseStepInfo

admin.site.site_title = 'GloryroadPlatform'
admin.site.site_header = 'GloryroadPlatform'

@admin.register(ProjectInfo) # 把项目信息注册到Django admin后台并显示
class SetAdmin(admin.ModelAdmin):
    list_display = ['project_name', 'responsible_name', 'test_user', 'dev_user', 'simple_desc', 'other_desc']


@admin.register(ModuleInfo) # 把模块管理注册到Django admin后台并显示
class ModelAdmin(admin.ModelAdmin):
    list_display = ['module_name', 'belong_project', 'test_user', 'test_user', 'simple_desc', 'other_desc']


@admin.register(CaseStepInfo) # 把步骤信息注册到Django admin后台并显示
class CaseStepInfoAdmin(admin.ModelAdmin):
    list_display = [ 'case', 'teststep', 'testobjname', 'optmethod', 'findmethod', 'evelement', 'testdata',  'create_time']


@admin.register(TestCaseInfo) # 把用例信息注册到Django admin后台并显示
class TestCaseInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'belong_project', 'belong_module', 'author', 'create_time', 'update_time']
