# Generated by Django 4.1.4 on 2023-04-08 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0045_icuroom_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='is_allocated',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Availability',
        ),
        migrations.DeleteModel(
            name='ICURoom',
        ),
    ]
