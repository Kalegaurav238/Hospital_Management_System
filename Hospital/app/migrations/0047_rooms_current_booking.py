# Generated by Django 4.1.4 on 2023-04-08 11:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0046_rooms_is_allocated_delete_availability_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='current_booking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.room_a'),
        ),
    ]
