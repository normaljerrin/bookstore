# Generated by Django 4.1.7 on 2023-03-04 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=222)),
                ('author', models.CharField(max_length=222)),
                ('description', models.CharField(max_length=555)),
                ('price', models.FloatField(blank=True, null=True)),
                ('image_url', models.CharField(blank=True, max_length=2222)),
                ('follow_author', models.CharField(blank=True, max_length=2222)),
                ('book_available', models.BooleanField()),
                ('star', models.FloatField()),
            ],
        ),
    ]
