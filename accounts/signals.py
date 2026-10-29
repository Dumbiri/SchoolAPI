from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, TeacherProfile, StudentProfile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs): 
    ##kwargs = additional keyword arguments that may be passed to the signal handler. In this case, it can include information about the save operation, such as whether the instance was created or updated.
    if created:
        # Create a new profile for the user
        if instance.role == User.Role.TEACHER:
            TeacherProfile.objects.create(user=instance)
        elif instance.role == User.Role.STUDENT:
            StudentProfile.objects.create(user=instance)