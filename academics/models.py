from django.db import models
from django.conf import settings

#create your models here

class AcademicSession(models.Model):
    session = models.CharField(max_length=20)
    is_current = models.BooleanField(default=False)

    def __str__(self):
        return self.session

class Classroom(models.Model):
    name = models.CharField(max_length=20)
    class_Teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'TEACHER'}, related_name='assigned_classes')
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)
    teacher = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, limit_choices_to={'role': 'TEACHER'}, related_name='subject_taught')

    def __str__(self):
        return f'{self.name} ({self.code})'

class Grade(models.Model):
    student = models.ForeignKey('accounts.StudentProfile', on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    exam_score = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    session = models.ForeignKey(AcademicSession, on_delete=models.CASCADE, related_name='grades')
    continuous_assessment = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    class Meta:
        unique_together = ('student', 'subject', 'session')

    @property
    def total_score(self):
        return self.continuous_assessment + self.exam_score

    def __str__(self):
        return f'{self.student} - {self.subject}: {self.total_score}'
