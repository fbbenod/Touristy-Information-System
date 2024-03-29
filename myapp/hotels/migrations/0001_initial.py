# Generated by Django 2.2.1 on 2019-08-12 03:25

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Features', multiselectfield.db.fields.MultiSelectField(choices=[('Swimming', 'Swimming'), ('Casino', 'Casino'), ('Gymnasium', 'Gymnasium'), ('Air Condition', 'Air Condition'), ('Deluxe Rooms', 'Deluxe Rooms'), ('Seminar_Halls', 'Seminar_Halls'), ('Attached Bathroom', 'Attached Bathroom')], max_length=84)),
                ('Price', models.CharField(max_length=10)),
                ('Image', models.ImageField(upload_to="Hotel's Images")),
                ('Rooms', models.ImageField(blank=True, upload_to=' Hotel Details ')),
                ('Rooms1', models.ImageField(blank=True, upload_to=' Hotel Details ')),
                ('Rooms2', models.ImageField(blank=True, upload_to=' Hotel Details ')),
                ('Rooms3', models.ImageField(blank=True, upload_to=' Hotel Details ')),
                ('Rooms4', models.ImageField(blank=True, upload_to=' Hotel Details ')),
                ('Types', models.TextField(blank=True, max_length=600)),
                ('Location', models.TextField(blank=True, max_length=700)),
                ('description1', models.TextField(blank=True, max_length=600)),
                ('description2', models.TextField(blank=True, max_length=600)),
            ],
            options={
                'verbose_name_plural': 'Hotels',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('user_name', models.CharField(max_length=100)),
                ('comment', models.CharField(max_length=200)),
                ('rating', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')])),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotels')),
            ],
        ),
    ]
