from django.contrib import admin
from .models import AcademicSession, Classroom, Subject, Grade

# Register your models here.
admin.site.register(AcademicSession)
admin.site.register(Classroom)
admin.site.register(Subject)

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'exam_score', 'continuous_assessment', 'total_score', 'session')
    list_filter = ('subject', 'session')
    # search_fields = ('student__user__username', 'subject__name')
