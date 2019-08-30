from django.shortcuts import render
from .models import CulturalPlaceTitle, NaturalPlaceTitle,CulturalPlaceDetails,NaturalPlaceDetails
from django.views.generic import ListView


def destinations(request):
    if request.method == 'GET':
        culturalplacetitle= CulturalPlaceTitle.objects.all()
        naturalplacetitle= NaturalPlaceTitle.objects.all()
        culturalplacedetails = CulturalPlaceDetails.objects.all()
        naturalplacedetails = NaturalPlaceDetails.objects.all()
        context = {
            'culturalplacetitle': culturalplacetitle,
            'naturalplacetitle': naturalplacetitle,
            'culturalplacedetails': culturalplacedetails,
            'naturalplacedetails' : naturalplacedetails,
        }
        return render(request, 'destinations/destinations.html', context)


class PostListView(ListView):
    model = CulturalPlaceTitle, NaturalPlaceTitle, CulturalPlaceDetails, NaturalPlaceDetails
    template_name = 'destinations/destinations.html'
    context_object_name = 'culturalplacetitle','naturalplacetitle','culturalplacedetails','naturalplacedetails'


