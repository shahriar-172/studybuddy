from django import forms
from .models import StudySession

class StudySessionForm(forms.ModelForm):
    class Meta:
        model = StudySession
        fields = ['title', 'description', 'scheduled_time']
        widgets = {
            'scheduled_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
