from django.contrib import admin
from fuw.models import Student, ClassName, Evaluation


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'matric_number', 'get_score')

    @admin.display(description='Score')
    def get_score(self, obj):
        return obj.classname.evaluation.score


@admin.register(ClassName)
class ClassNameAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'get_score')

    @admin.display(description='Score')
    def get_score(self, obj):
        return obj.evaluation.score


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('name', 'score')

