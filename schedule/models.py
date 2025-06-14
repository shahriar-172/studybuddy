from django.db import models
from django.contrib.auth.models import User
from studygroups.models import StudyGroup

class StudySession(models.Model):
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE, related_name='sessions')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    scheduled_time = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.group.name}"
