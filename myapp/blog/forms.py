from django import forms
from .models import Post


class ImageForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['image1', 'image2', 'image3', 'image4']