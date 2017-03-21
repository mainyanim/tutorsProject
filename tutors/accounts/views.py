from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404

from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    UserProfileForm,
)
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from .models import UserProfile, Subject
from django.views import generic
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:login'))
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)


@login_required
def view_profile(request, pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user}
    return render(request, 'accounts/profile.html', args)

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def edit_user(request):
    user = request.user
    user_form = UserProfileForm(instance=user)

    ProfileInlineFormset = inlineformset_factory(User, UserProfile, fields=('title', 'first_name', 'last_name', 'area', 'charge', 'description', 'language', 'subject'))
    formset = ProfileInlineFormset(instance=user)

    if request.user.is_authenticated() and request.user.id == user.id:
        if request.method == "POST":
            user_form = UserProfileForm(request.POST, request.FILES, instance=user)
            formset = ProfileInlineFormset(request.POST, request.FILES, instance=user)

            if user_form.is_valid():
                created_user = user_form.save(commit=False)
                formset = ProfileInlineFormset(request.POST, request.FILES, instance=created_user)

                if formset.is_valid():
                    created_user.save()
                    formset.save()
                    return redirect(reverse('accounts:view_profile'))

        return render(request, "accounts/account_update.html", {
            "noodle_form": user_form,
            "formset": formset,
        })
    else:
        raise PermissionDenied


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('accounts:view_profile'))
        else:
            return redirect(reverse('accounts:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'accounts/change_password.html', args)


class SubjectDetailView(generic.DetailView):
    """
    Generic class-based detail view for a tutor.
    """
    model = Subject

class SubjectListView(generic.ListView):
    """
    Generic class-based list view for a list of authors.
    """
    model = Subject
    paginate_by = 10

#show all subjects and by click on subject show tutors associated with subject
