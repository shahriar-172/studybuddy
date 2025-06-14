from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StudySessionForm
from .models import StudySession
from studygroups.models import StudyGroup

@login_required
def create_session(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)

    if request.method == 'POST':
        form = StudySessionForm(request.POST)
        if form.is_valid():
            session = form.save(commit=False)
            session.group = group
            session.created_by = request.user
            session.save()
            return redirect('group_details', group_id=group.id)
    else:
        form = StudySessionForm()

    return render(request, 'schedule/create_session.html', {'form': form, 'group': group})

@login_required
def session_list(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    sessions = StudySession.objects.filter(group=group).order_by('scheduled_time')
    return render(request, 'schedule/session_list.html', {'group': group, 'sessions': sessions})




