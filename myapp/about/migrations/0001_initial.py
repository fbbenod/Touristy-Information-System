# Generated by Django 2.2.1 on 2019-06-12 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='DEFAULT VALUE')),
                ('Pic', models.ImageField(upload_to='AboutUs_Photos')),
            ],
        ),
        migrations.CreateModel(
            name='Our',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='DEFAULT VALUE', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Link', models.CharField(default='DEFAULT VALUE', max_length=100)),
                ('Name', models.CharField(max_length=30)),
                ('Role', models.CharField(max_length=30)),
                ('Hobby', models.TextField(default='DEFAULT VALUE', max_length=50)),
                ('Image', models.ImageField(upload_to='Team_Photos')),
            ],
        ),
    ]
