from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResourceForm
from studygroups.models import StudyGroup
from .models import Resource
from django.contrib.auth.decorators import login_required

@login_required
def upload_resource(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.group = group
            resource.uploaded_by = request.user
            resource.save()
            return redirect('group_details', group_id=group.id)
    else:
        form = ResourceForm()
    return render(request, 'resources/upload_resource.html', {'form': form, 'group': group})



  
    

