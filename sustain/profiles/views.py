from django.shortcuts import render
from django.views.generic import TemplateView
from challenges.models import Challenge


# Create your views here.
class ProfileView(TemplateView):
    template_name = 'profiles/profile.html'
    def get(self, request):
            # self.sustainer.user
        sustainer_challenges = Challenge.objects.filter(sustainer=request.user.sustainer)
        context = {
            'sustainer_challenges':sustainer_challenges
        }
        return render(request, self.template_name, context)
        
    
