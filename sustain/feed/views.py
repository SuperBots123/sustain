from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class FeedView(TemplateView):
    template_name = 'feed/feed.html'
    
    def get(self, request):
        # if not request.user.is_authenticated:
        #     return redirect('users:login')
        return render(request, self.template_name)
    
    def post(request):
        pass
