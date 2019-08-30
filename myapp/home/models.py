from django.db import models
from django.utils import timezone
# from PIL import Image


class FirstContent(models.Model):
    Text1 = models.CharField(max_length=100)

    def __str__(self):
        return self.Text1

    class Meta:
        verbose_name_plural="First Context Over Image"


class SecondContent(models.Model):
    Text2 = models.CharField(max_length=100)

    def __str__(self):
        return self.Text2

    class Meta:
        verbose_name_plural="Second Context Over Image"


class ThirdContent(models.Model):
    Text3 = models.CharField(max_length=100)

    def __str__(self):
        return self.Text3

    class Meta:
        verbose_name_plural = "Third Context Over Image"


class BodyContent1(models.Model):
    Text = models.CharField(max_length=50)

    def __str__(self):
        return self.Text

    class Meta:
        verbose_name_plural = "Body_Title"


class BodyContent2(models.Model):
    Text= models.TextField(max_length=100)

    class Meta:
        verbose_name_plural=\
            "Body Text"


class PopularDestination(models.Model):
    Price = models.CharField(max_length=15, default="DEFAULT VALUE ")
    Place = models.CharField(max_length=20, default="DEFAULT VALUE ")
    Image = models.ImageField(upload_to= 'Popular_Destination')
    Place1 = models.CharField(max_length=20, blank=True)
    Image1 = models.ImageField(upload_to='near_by_place',blank=True)
    Place2 = models.CharField(max_length=20,blank=True)
    Image2 = models.ImageField(upload_to='near_by_place',blank=True)
    Place3 = models.CharField(max_length=20, blank=True)
    Image3 = models.ImageField(upload_to='near_by_place',blank=True)
    Place4 = models.CharField(max_length=20, blank=True)
    Image4 = models.ImageField(upload_to='near_by_place',blank=True)
    Place5 = models.CharField(max_length=20, blank=True)
    Image5 = models.ImageField(upload_to='near_by_place', blank=True)
    Place6 = models.CharField(max_length=20, blank=True)
    Image6 = models.ImageField(upload_to='near_by_place', blank=True)

    def __str__(self):
        return self.Place

    class Meta:
        verbose_name_plural = "Images of Popular Destination"


class Package(models.Model):
    Title = models.CharField(max_length=60)
    Places = models.TextField(max_length=500)
    Prices = models.TextField(max_length=500)

    class Meta:
        verbose_name_plural="Package"

    def __str__(self):
        return self.Title


class OurService1(models.Model):
    Content = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Title For Our Service Area"


class OurService2(models.Model):
    Content = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Sub-Title For Our Service Area"


class OurServiceImage(models.Model):
    Title = models.CharField(max_length=50)
    Details = models.TextField(max_length=250)
    Content = models.ImageField(upload_to='Services')

    def __str__(self):
        return self.Title

    def save(self):
        super().save()

    class Meta:
        verbose_name_plural = "Contents to Our Service Area"


class HomeQuestion(models.Model):
    Question = models.TextField(max_length=200)
    Descriptions = models.TextField(max_length=300)
    Image = models.ImageField(upload_to='QuestionImage')
    Button = models.CharField(max_length=40)

    def __str__(self):
        return self.Question

    class Meta:
        verbose_name_plural = "Question Asking Division"


class OurPlaces(models.Model):
    Title = models.TextField(max_length=50)
    Details = models.TextField(max_length=150)
    Image = models.ImageField(upload_to="Famous_Places")
    Date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name_plural = " Our Popular Places "


class Footer(models.Model):
    Content = models.TextField(max_length=200)

    class Meta:
        verbose_name_plural = "Footer"














