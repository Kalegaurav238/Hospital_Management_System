# Generated by Django 4.1.4 on 2023-03-26 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0035_rename_patient_payment_patient_bill'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_bill',
            name='Invoice_id',
            field=models.IntegerField(default=0),
        ),
    ]
