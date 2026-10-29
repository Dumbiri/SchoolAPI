from rest_framework import serializers
from accounts.models import User, StudentProfile, TeacherProfile
from academics.models import Subject, Classroom, Grade, AcademicSession


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role', 'phone_number']

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class_name = serializers.CharField(source = 'current_class.name', read_only=True)

    class Meta:
        model = StudentProfile
        fields = ['id', 'user', 'admission_number', 'date_of_birth', 'class_name']

class SubjectSerializer(serializers.ModelSerializer):
    teacher_name = serializers.CharField(source = 'teacher.get_full_name', read_only=True)
    
    class Meta:
        model = Subject
        fields = ['id', 'name', 'code', 'teacher', 'teacher_name']


class GradeSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source = 'subject_name', read_only=True)
    student_name = serializers.CharField(source = 'student.user.get_full_name', read_only = True)

    class Meta:
        model = Grade
        fields = ['id', 'student', 'student_name', 'subject', 'subject_name', 'session', 'continuous_assessment', 'exam_score', 'total_score']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=6)
    admission_number = serializers.CharField(write_only=True, required=False, allow_blank=True)
    employee_id = serializers.CharField(write_only=True, required=False, allow_blank=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role', 'phone_number', 'admission_number', 'employee_id']

