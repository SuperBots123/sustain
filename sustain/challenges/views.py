from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class ChallengeView(TemplateView):
    template_name = 'challenges/challenges.html'
    def get(self, request):
        return render(request, self.template_name)
