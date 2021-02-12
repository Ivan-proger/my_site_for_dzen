import os
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView
from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render, redirect
from django.core.mail import send_mail

from .forms import SignUpForm


class MyRegisterFormView(FormView):
    form_class = SignUpForm
    success_url = "/accounts/login/"
    template_name = "signup.html"

    def form_valid(self, form):
        self.email = form.cleaned_data.get('email')
        print(self.email)
        assert 'SYSTEMROOT' in os.environ
        send_mail('Welcome!', 'eiwuyrsadhjknuiesldhjfk', None, ['lox32lox32@gmail.com'], fail_silently=False) 
        form.save()
        return super(MyRegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(MyRegisterFormView, self).form_invalid(form)

