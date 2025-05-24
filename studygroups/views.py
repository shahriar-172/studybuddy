from django.shortcuts import render, redirect
from .forms import StudyGroupForm
from .models import StudyGroup
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

@login_required
def group_details(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    return render(request, 'studygroups/group_details.html', {'group': group})


@login_required
def create_study_group(request):
    if request.method == 'POST':
        form = StudyGroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.created_by = request.user
            group.save()
            group.members.add(request.user)  # creator auto join kore
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
    group = StudyGroup.objects.get(id=group_id)
    group.members.add(request.user)
    return redirect('group_list')
    from django.shortcuts import get_object_or_404
from .models import StudyGroup

@login_required
def group_details(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    members = group.members.all()
    return render(request, 'studygroups/group_details.html', {
        'group': group,
        'members': members
    })
@login_required
def create_group(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        if name and description:
            group = StudyGroup.objects.create(name=name, description=description)
            group.members.add(request.user)
            return redirect('group_list')
    return render(request, 'studygroups/create_group.html')


