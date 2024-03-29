# Generated by Django 4.1.2 on 2022-12-22 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_alter_numericquestion_category_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.CharField(max_length=255)),
                ('question', models.CharField(max_length=255)),
                ('right_answer', models.CharField(max_length=64)),
                ('wrong_answer_1', models.CharField(max_length=64)),
                ('wrong_answer_2', models.CharField(max_length=64)),
                ('wrong_answer_3', models.CharField(max_length=64)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.category')),
            ],
        ),
    ]
