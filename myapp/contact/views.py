from django.shortcuts import render
from .models import Contact
from django.views.generic import ListView


def contact(request):
    if request.method == 'GET':
        detail = Contact.objects.all()
        context = {
            'detail': detail
        }
        return render(request, 'contact/contact.html', context)


class PostListView(ListView):
    model = Contact
    template_name = 'contact/contact.html'
    context_object_name = 'detail'
