from django.shortcuts import render
from .models import AboutUs, Team, Our
from django.views.generic import ListView


def about(request):
    if request.method == 'GET':
        about_us = AboutUs.objects.all()
        team = Team.objects.all()
        our = Our.objects.all()
        context = {
            'about_us': about_us,
            'team': team,
            'our': our,

        }
        return render(request, 'about/about.html', context)


class PostListView(ListView):
    model = AboutUs, Team, Our
    template_name = 'about/about.html'
    context_object_name = 'about_us', 'team', 'our'

