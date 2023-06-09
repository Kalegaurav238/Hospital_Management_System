# Generated by Django 4.1.4 on 2023-03-31 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_services_remove_patient_payment_cost_of_treatment_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Services',
        ),
        migrations.AddField(
            model_name='patient_payment',
            name='cost_of_treatment',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='patient_payment',
            name='service_name',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
