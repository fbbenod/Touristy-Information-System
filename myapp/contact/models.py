from django.db import models


class Contact(models.Model):
    Address = models.CharField(max_length=50)
    Phone_Number = models.CharField(max_length=15)
    Email = models.EmailField(max_length=30)

    class Meta:
        verbose_name_plural = "Contact"

        def __str__(self):
            return self.Name


class map(models.Model):
    city=models.CharField(max_length=20)
    place=models.CharField(max_length=20)




