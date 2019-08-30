from django.contrib import admin
from .models import Hotels, Review


class ReviewAdmin(admin.ModelAdmin):
    model = Review, Hotels
    list_display = ('name', 'user_name','rating','comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']


admin.site.register(Hotels)
admin.site.register(Review, ReviewAdmin)



