from django.db import models
from multiselectfield import MultiSelectField
# from django.utils import timezone
# from django.contrib.auth.models import User
from django.urls import reverse


class Hotels(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    FEATURE = (
        ('Swimming', 'Swimming'),
        ('Casino', 'Casino'),
        ('Gymnasium', 'Gymnasium'),
        ('Air Condition', 'Air Condition'),
        ('Deluxe Rooms', 'Deluxe Rooms'),
        ('Seminar_Halls', 'Seminar_Halls'),
        ('Attached Bathroom', 'Attached Bathroom')
    )

    Name = models.CharField(max_length=50)
    Features = MultiSelectField(choices=FEATURE)
    Price = models.CharField(max_length=10)
    Image = models.ImageField(upload_to= "Hotel's Images")
    Rooms = models.ImageField(upload_to=' Hotel Details ', blank=True)
    Rooms1 = models.ImageField(upload_to=' Hotel Details ', blank=True)
    Rooms2 = models.ImageField(upload_to=' Hotel Details ', blank=True)
    Rooms3 = models.ImageField(upload_to=' Hotel Details ', blank=True)
    Rooms4 = models.ImageField(upload_to=' Hotel Details ', blank=True)
    Types = models.TextField(max_length=600, blank=True)
    Location = models.TextField(max_length=700, blank=True)
    description1 = models.TextField(max_length=600, blank= True)
    description2 = models.TextField(max_length=600, blank=True)

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = "Hotels"

    def get_absolute_url(self):
        return reverse('Hotel1', kwargs={'pk': self.pk})


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    name = models.ForeignKey(Hotels, on_delete=models.CASCADE)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.comment










