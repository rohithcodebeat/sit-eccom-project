# Generated by Django 4.2.2 on 2023-06-19 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='date_of_delivery',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='date_of_order',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
