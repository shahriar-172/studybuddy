from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import StudyGroupForm
from .models import StudyGroup
from users.models import UserProfile  




@login_required
def group_details(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    members = group.members.all()
    creator_profile = UserProfile.objects.get(user=group.created_by)

    return render(request, 'studygroups/group_details.html', {
        'group': group,
        'members': members,
        'creator_profile': creator_profile
    })



@login_required
def create_study_group(request):
    if request.method == 'POST':
        form = StudyGroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()
            group.members.add(request.user)
            return redirect('group_list')
    else:
        form = StudyGroupForm()
    return render(request, 'studygroups/create_group.html', {'form': form})




@login_required
def group_list(request):
    groups = StudyGroup.objects.all()
    return render(request, 'studygroups/group_list.html', {'groups': groups})



@login_required
def join_group(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    group.members.add(request.user)
    return redirect('group_list')



@login_required
def leave_group(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    if request.user in group.members.all():
        group.members.remove(request.user)
    return redirect('group_list')
