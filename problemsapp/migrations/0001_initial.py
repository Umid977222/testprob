# Generated by Django 4.1.2 on 2022-10-14 05:53

from django.db import migrations, models
import problemsapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Problems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_model', models.CharField(blank=True, max_length=200)),
                ('img', models.ImageField(default='posts/default.jpg', upload_to=problemsapp.models.upload_location)),
                ('description', models.TextField()),
                ('add_bot_button', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
