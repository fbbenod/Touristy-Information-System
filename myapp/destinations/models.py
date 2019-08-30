from django.db import models


class CulturalPlaceTitle(models.Model):
    Heading1 = models.CharField(max_length=50)
    Heading2 = models.TextField(max_length=100)

    def __str__(self):
        return self.Heading1

    class Meta:
        verbose_name_plural = "Title For Cultural Place"


class NaturalPlaceTitle(models.Model):
    Heading1 = models.CharField(max_length=50)
    Heading2 = models.TextField(max_length=100)

    def __str__(self):
        return self.Heading1

    class Meta:
        verbose_name_plural = "Title For Natural Place"


class CulturalPlaceDetails(models.Model):
    Location = models.CharField(max_length=40)
    Image = models.ImageField(upload_to='Cultural_Places_Image')
    Details = models.TextField(max_length=500)
    ExtraContent = models.TextField(max_length=100,default='Null')

    def __str__(self):
        return self.Location

    class Meta:
        verbose_name_plural = "Cultural Place Info"


class NaturalPlaceDetails(models.Model):
    Location = models.CharField(max_length=40)
    Image = models.ImageField(upload_to='Cultural_Places_Image')
    Details = models.TextField(max_length=500)
    ExtraContent = models.TextField(max_length=100,default='Null')

    def __str__(self):
        return self.Location

    class Meta:
        verbose_name_plural = "Natural Place Info"


