import os
assert 'SYSTEMROOT' in os.environ
from random import randint
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import auth
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .models import Profile
from .forms import SignUpForm, Loginform


def random_cod():
	cod = str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9)) + str(randint(0,9))
	return int(cod)



class MyRegisterFormView(FormView):
    form_class = SignUpForm
    success_url = "/accounts/login/"
    template_name = "signup.html"

    def form_valid(self, form):
        form.save()

        my_password1 = form.cleaned_data.get('password1')
        username = form.cleaned_data.get('username')

        u_f = User.objects.get(username=username, email=username, is_active=False)
        code = str(random_cod())
        user = authenticate(username=username, password=my_password1)
        # send_mail('Welcome!', code, None, ['lox32lox32@gmail.com'], fail_silently=False)
        Profile.objects.create(user=u_f, code=code)
        print(Profile.objects.filter(code=code))
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)



def pagelogin(request):
    form = Loginform(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None:
            print(login(request, user))
            # login(request, user)
            return redirect('/')

        else:
            context= {'form': form,
                    'error': 'The username and password combination is incorrect'}
            print("это else после if user is not...")
            return render(request, 'registration/login.html', context )

    else:
        context= {'form': form}
        return render(request, 'registration/login.html', context)