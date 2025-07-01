from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import FileResponse
from .forms import ResourceForm
from .models import Resource
from studygroups.models import StudyGroup

import os


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



@login_required
def download_resource(request, resource_id):
    resource = get_object_or_404(Resource, id=resource_id)
    resource.download_count += 1
    resource.save()

    file_path = resource.file.path
    return FileResponse(open(file_path, 'rb'), as_attachment=True)



@login_required
def group_resources(request, group_id):
    group = get_object_or_404(StudyGroup, id=group_id)
    shared_resources = Resource.objects.filter(group=group)
    popular_resources = shared_resources.order_by('-download_count')[:3]  

    return render(request, 'resources/group_resources.html', {
        'group': group,
        'resources': shared_resources,
        'popular_resources': popular_resources
    })
