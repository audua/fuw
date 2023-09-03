from django.db import models


class Evaluation(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    score = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    picture = models.ImageField(upload_to="evaluations/", blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.score}'


class ClassName(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    code = models.CharField(max_length=10, blank=True, null=True)
    evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.code} {self.evaluation.score}'


class Student(models.Model):
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    matric_number = models.CharField(max_length=20, blank=True, null=True)
    classname = models.ForeignKey(ClassName, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}":" {self.matric_number}'
