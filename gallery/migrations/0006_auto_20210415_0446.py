# Generated by Django 3.1.7 on 2021-04-15 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20210415_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Fotoğraf:'),
        ),
    ]