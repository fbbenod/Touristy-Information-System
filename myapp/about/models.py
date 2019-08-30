from django.db import models


class AboutUs(models.Model):
    content = models.TextField(default='DEFAULT VALUE')
    Pic = models.ImageField(upload_to='AboutUs_Photos')

    class Meta:
        verbose_name_plural='About Us'


class Team(models.Model):
    Link = models.CharField(max_length=100, default='DEFAULT VALUE')
    Name = models.CharField(max_length=30)
    Role = models.CharField(max_length=30)
    Hobby = models.TextField(max_length=50, default='DEFAULT VALUE')
    Image = models.ImageField(upload_to='Team_Photos')

    def __str__(self):
        return self.Name

    class Meta:
        verbose_name_plural = 'Team'


class Our(models.Model):
    text = models.TextField(max_length=50, default='DEFAULT VALUE')

    class Meta:
        verbose_name_plural = "Our Motto"