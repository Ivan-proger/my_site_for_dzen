from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):

    username = forms.CharField(required=True, max_length=15, label='email',  min_length=2)
    first_name = forms.CharField(required=True, max_length=25, label='логин', )    
    password1 = forms.CharField(required=True, max_length=30, label='Пароль', min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, max_length=30, label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        if User.objects.filter(username=cleaned_data.get('username')).exists():
            self.add_error('username', "Эта почта уже зарегестрированна")

        if User.objects.filter(first_name=cleaned_data.get('first_name')).exists():
        	self.add_error('first_name', 'такой логин уже занят попробуйте другой')

       	return cleaned_data 

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['username']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.is_active = False

        if commit:
            user.save()
        return user

class EmailValid(forms.Form):
	code = forms.CharField(max_length=6, label="Code in email")


class Loginform(forms.Form):
    username = forms.CharField(max_length= 40, label="Enter email")
    password = forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)

