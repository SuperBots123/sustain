import datetime

from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout

from .forms import RegistrationForm
from .models import Sustainer


class LoginView(TemplateView):
    template_name = 'users/login.html'
    
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('feed:feed')
        return render(request, self.template_name)
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed:feed')
        return redirect('users:login')
    
    
class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('users:login')
    
    
class RegisterView(TemplateView):
    template_name = 'users/register.html'
    
    def get(self, request):
        return render(request, "users/register.html")
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            user_profile = Sustainer(user=user, joined=datetime.date.today())
            user_profile.save()
            return redirect('feed:feed')
        for error in form.errors:
            print(error) 
        return redirect('users:register')