from django.shortcuts import render
from django.views.generic import TemplateView
from challenges.models import Challenge
from .forms import EditProfileModelForm
from django.shortcuts import redirect


from django.http import HttpResponseRedirect


# Create your views here.
class ProfileView(TemplateView):
    template_name = 'profiles/new_profile.html'
    
    def get(self, request):
        challenges = Challenge.objects.filter(sustainer=request.user.sustainer, completionStatus=True).order_by('time').reverse()
        form = EditProfileModelForm(instance=request.user.sustainer)
        context = {
            'challenges': challenges,
            'form': form
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        form = EditProfileModelForm(request.POST, request.FILES, instance=request.user.sustainer)
        if form.is_valid():
            form.save()
            return redirect('profiles:profile')
        else:
            print(form.errors)
        
        challenges = Challenge.objects.filter(sustainer=request.user.sustainer, completionStatus=True).order_by('time').reverse()
        context = {
            'challenges': challenges,
            'form': form,
        }
        return render(request, self.template_name, context)
        
    
