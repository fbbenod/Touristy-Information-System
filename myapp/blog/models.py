from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, null='True')
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image1 = models.ImageField(blank='True',  upload_to='Blog_Photos')
    image2 = models. ImageField(blank='True', upload_to='Blog_Photos')
    image3 = models. ImageField(blank='True', upload_to='Blog_Photos')
    image4 = models. ImageField(blank='True', upload_to='Blog_Photos')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
