# Generated by Django 4.1.5 on 2023-01-24 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_testimagemodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TestImageModel',
        ),
        migrations.RemoveField(
            model_name='imagequestion',
            name='image_url',
        ),
        migrations.AddField(
            model_name='imagequestion',
            name='image',
            field=models.ImageField(blank=True, upload_to='image_question/'),
        ),
    ]
