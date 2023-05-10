# Generated by Django 4.1.4 on 2023-04-09 06:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_remove_rooms_current_booking_rooms_is_allocated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allotment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('room_type', models.CharField(max_length=100, null=True)),
                ('patient_name', models.CharField(max_length=100)),
                ('allotment_date', models.CharField(max_length=100)),
                ('discharge_date', models.CharField(max_length=100)),
                ('doctor_name', models.CharField(max_length=100)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.patient')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rooms')),
            ],
        ),
        migrations.DeleteModel(
            name='Room_A',
        ),
    ]
