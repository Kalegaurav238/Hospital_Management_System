# Generated by Django 4.1.4 on 2023-03-27 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_alter_patient_payment_invoice_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient_payment',
            name='advance_paid',
            field=models.IntegerField(),
        ),
    ]