from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

    def save(self, commit = True):
        user = super(RegistrationForm, self).save(commit = False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'username',
            'email',
        )
