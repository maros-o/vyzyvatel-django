# Generated by Django 4.1.5 on 2023-01-20 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_imagequestion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='vyzyvatel-django/')),
            ],
        ),
    ]
