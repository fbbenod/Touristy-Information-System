from django.shortcuts import render, get_object_or_404
from .models import Hotels, Review
from django.views.generic import (
    ListView,
    DetailView
)
from .forms import ReviewForm
import datetime


def hotels(request):
    context = {
        "hotels": Hotels.objects.all(),
        "review": Review.objects.all()
    }
    return render(request, 'hotels/hotels.html', context)


class PostListView(ListView):
    model = Hotels
    template_name = 'hotels/hotels.html'
    context_object_name = 'hotels'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['latest_review_list'] = Review.objects.all()
        return context


class PostDetailView(DetailView):
    model = Hotels
    template_name = 'hotels/hotel_details.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['latest_review_list'] = Review.objects.filter(name=kwargs['object'].pk)
        context['form'] = ReviewForm
        return context


def add_review(request, hotel_id):
    name = get_object_or_404(Hotels, pk=hotel_id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.name = name
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        return render(request, 'hotels/thank.html')