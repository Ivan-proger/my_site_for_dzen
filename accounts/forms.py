from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class SignUpForm(UserCreationForm):
    captcha = ReCaptchaField()

    email = forms.CharField(required=True, max_length=55, label='Email',  min_length=2)
    first_name = forms.CharField(required=True, max_length=25, label='Логин', min_length=3)    
    password1 = forms.CharField(required=True, max_length=30, label='Пароль', min_length=8, widget=forms.PasswordInput())
    password2 = forms.CharField(required=True, max_length=30, label='Повторите пароль', widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('first_name', 'email', 'password1', 'password2', 'captcha')

    def clean(self):
        cleaned_data = super().clean()
        if User.objects.filter(email=cleaned_data.get('email')).exists():
            prof = User.objects.filter(email=cleaned_data.get('email')).filter(is_active=True)
            if prof:
                self.add_error('email', "Эта почта уже зарегестрированна")
            else:
                prof = User.objects.filter(email=cleaned_data.get('email')).filter(is_active=False)
                prof.delete()

        if User.objects.filter(first_name=cleaned_data.get('first_name')).exists():
            fprof = User.objects.filter(first_name=cleaned_data.get('first_name')).filter(is_active=True)
            if fprof:
                self.add_error('first_name', 'такой логин уже занят попробуйте другой')
            else:
                fprof = User.objects.filter(first_name=cleaned_data.get('first_name')).filter(is_active=False)
                fprof.delete()

       	return cleaned_data 

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.email = self.cleaned_data['email']
        user.username = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']
        user.is_active = False

        if commit:
            user.save()
        return user



class CodeValid(forms.Form):
	code = forms.CharField(max_length=6, label="Code in email")


class Loginform(forms.Form):
    username = forms.CharField(max_length= 40, label="Enter email")
    password = forms.CharField(max_length= 30, label='Password', widget=forms.PasswordInput)

