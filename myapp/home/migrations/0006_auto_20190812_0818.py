# Generated by Django 2.2.1 on 2019-08-12 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20190617_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='populardestination',
            name='Image1',
            field=models.ImageField(blank=True, upload_to='near_by_place'),
        ),
        migrations.AddField(
            model_name='populardestination',
            name='Image2',
            field=models.ImageField(blank=True, upload_to='near_by_place'),
        ),
        migrations.AddField(
            model_name='populardestination',
            name='Image3',
            field=models.ImageField(blank=True, upload_to='near_by_place'),
        ),
        migrations.AddField(
            model_name='populardestination',
            name='Image4',
            field=models.ImageField(blank=True, upload_to='near_by_place'),
        ),
        migrations.AddField(
            model_name='populardestination',
            name='Place1',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='populardestination',
            name='Place2',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='populardestination',
            name='Place3',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='populardestination',
            name='Place4',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]