# Generated by Django 3.0.8 on 2020-07-15 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='wishlist',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
