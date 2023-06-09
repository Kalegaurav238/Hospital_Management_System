# Generated by Django 4.1.4 on 2023-04-09 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_alter_rooms_available'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=100)),
                ('checkin_date', models.DateField()),
                ('checkout_date', models.DateField()),
                ('doctor_name', models.CharField(default=1, max_length=100)),
                ('status', models.CharField(choices=[('available', 'Available'), ('allocated', 'Allocated')], default='available', max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='rooms',
            old_name='room_no',
            new_name='roomnumber',
        ),
        migrations.RemoveField(
            model_name='rooms',
            name='available',
        ),
        migrations.AddField(
            model_name='rooms',
            name='is_icu',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Allotment',
        ),
        migrations.AddField(
            model_name='booking',
            name='room_s',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.rooms'),
        ),
    ]
