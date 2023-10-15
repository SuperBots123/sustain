from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .models import Sustainer
from challenges.models import Challenge


class FeedView(TemplateView):
    template_name = 'feed/feed.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        friends = request.user.sustainer.following.all()
        context = {'posts': Challenge.objects.filter(sustainer__in=friends, completionStatus=True).order_by('time').reverse(), 'not_friends' : Sustainer.objects.all().exclude(following__in=friends)}
        return render(request, self.template_name, context)
    

class FollowView(TemplateView):
    
    def get(self, request, pk):
        request.user.sustainer.following.add(Sustainer.objects.get(pk=pk))
        return redirect('feed:feed')
