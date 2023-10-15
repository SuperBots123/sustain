from django.shortcuts import render
from django.views.generic import TemplateView

from users.models import Sustainer


class FriendsView(TemplateView):
    template_name = 'friends/friends.html'

    def get(self, request):
        friends = request.user.sustainer.following.all()
        context = {'not_friends' : Sustainer.objects.all().exclude(following__in=friends)}
        return render(request, self.template_name, context)