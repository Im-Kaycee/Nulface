from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'inputbox'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'inputbox'}))
    last_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'inputbox'}))
    username = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'inputbox'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name',  'last_name', 'password')
class PasswordChangedForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'inputbox', 'type': 'password'}))
    new_password1 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'inputbox', 'type': 'password'}))
    new_password2 = forms.CharField(max_length=255, widget=forms.PasswordInput(attrs={'class': 'inputbox', 'type': 'password'}))
    
    class Meta:
        model = User
        fields = ('old_password', 'new_password1',  'new_password2')

        