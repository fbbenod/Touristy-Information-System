from django.shortcuts import render
from .models import FirstContent, SecondContent,ThirdContent,Package,BodyContent1,\
    BodyContent2, OurService1, OurService2,\
    OurServiceImage, PopularDestination, HomeQuestion, OurPlaces, Footer
from django.views.generic import (
    ListView,
    DetailView
)


def index(request):
    if request.method == 'GET':
        firstcontent=FirstContent.objects.all()
        secondcontent=SecondContent.objects.all()
        thirdcontent = ThirdContent.objects.all()
        bodycontent1= BodyContent1.objects.all()
        bodycontent2= BodyContent2.objects.all()
        populardestination = PopularDestination.objects.all()
        ourservice1 = OurService1.objects.all()
        ourservice2 = OurService2.objects.all()
        ourserviceimage = OurServiceImage.objects.all()
        package = Package.objects.all()
        homequestion = HomeQuestion.objects.all()
        ourplaces = OurPlaces.objects.all()
        footer = Footer.objects.all()

        context = {
            'firstcontent': firstcontent,
            'secondcontent': secondcontent,
            'thirdcontent' : thirdcontent,
            'bodycontent1' :bodycontent1,
            'bodycontent2' :bodycontent2,
            'populardestination': populardestination,
            'ourservice1' : ourservice1,
            'ourservice2' : ourservice2,
            'ourserviceimage':  ourserviceimage,
            'package' : package,
            'homequestion' :homequestion,
            'ourplaces' : ourplaces,
            'footer':footer
        }
        return render(request, 'home/index.html', context)


class PostListView(ListView):
    model = FirstContent
    template_name = 'home/index.html'
    context_object_name = 'firstcontent'

    def get_context_data(self, **kwargs):
        context =  super(PostListView, self).get_context_data(**kwargs)
        context.update({
            'secondcontent':SecondContent.objects.all(),
            'thirdcontent': ThirdContent.objects.all(),
            'bodycontent2': BodyContent2.objects.all(),
            'bodycontent1': BodyContent1.objects.all(),
            'populardestination': PopularDestination.objects.all(),
            'ourservice1': OurService1.objects.all(),
            'ourservice2': OurService2.objects.all(),
            'ourserviceimage': OurServiceImage.objects.all(),
            'package': Package.objects.all(),
            'homequestion': HomeQuestion.objects.all(),
            'ourplaces': OurPlaces.objects.all(),
            'footer': Footer.objects.all(),
        })
        return context


class PostDetailView(DetailView):
    model = PopularDestination
    template_name = 'home/index2.html'
    context_object_name = 'populardestinations'




