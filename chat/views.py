from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Message
from studygroups.models import StudyGroup

@login_required
def group_chat(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(group=group, user=request.user, content=content)
            return redirect('group_chat', group_id=group.id)

    messages = Message.objects.filter(group=group).order_by('timestamp')
    return render(request, 'chat/group_chat.html', {'group': group, 'messages': messages})
