# Generated by Django 5.0.4 on 2024-04-28 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_name', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='images')),
                ('scientific_name', models.CharField(max_length=100)),
                ('cost', models.CharField(blank=True, max_length=5)),
            ],
        ),
    ]
