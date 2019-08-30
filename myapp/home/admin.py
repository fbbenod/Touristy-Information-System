from django.contrib import admin
from .models import FirstContent, SecondContent,ThirdContent,\
    BodyContent1,BodyContent2,Package, PopularDestination, \
    Footer,OurService1,OurService2,OurServiceImage, HomeQuestion, OurPlaces

admin.site.register(Package)
admin.site.register(FirstContent)
admin.site.register(SecondContent)
admin.site.register(ThirdContent)
admin.site.register(PopularDestination)
admin.site.register(BodyContent1)
admin.site.register(BodyContent2)
admin.site.register(Footer)
admin.site.register(OurService1)
admin.site.register(OurService2)
admin.site.register(OurServiceImage)
admin.site.register(HomeQuestion)
admin.site.register(OurPlaces)



