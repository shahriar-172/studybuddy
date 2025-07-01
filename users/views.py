from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, UserProfileForm
from studygroups.models import StudyGroup


def welcome_view(request):
    return render(request, 'users/welcome.html')


@login_required
def home(request):
    joined_groups = StudyGroup.objects.filter(members=request.user)
    all_groups = StudyGroup.objects.all()
    return render(request, 'users/dashboard.html', {
        'joined_groups': joined_groups,
        'all_groups': all_groups
    })


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)
            return redirect('home')  
    else:
        user_form = UserRegistrationForm()
        profile_form = UserProfileForm()
    
    return render(request, 'users/register.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })
