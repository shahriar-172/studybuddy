from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    institution = models.CharField(max_length=100)
    student_class = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username
