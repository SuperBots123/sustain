from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .models import Post, Sustainer


class FeedView(TemplateView):
    template_name = 'feed/feed.html'
    
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('users:login')
        friends = request.user.sustainer.following.all()
        context = {'posts': Post.objects.filter(sustainer__in=friends)}
        return render(request, self.template_name, context)
    
    def post(request):
        pass
