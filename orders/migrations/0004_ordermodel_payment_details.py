# Generated by Django 4.2.2 on 2023-06-23 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='payment_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='OrderModel_payment_details', to='orders.paymentdetailmodel'),
        ),
    ]
