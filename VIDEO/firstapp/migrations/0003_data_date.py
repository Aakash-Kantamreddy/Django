# Generated by Django 5.0.3 on 2024-03-19 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0002_rename_aakash_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2024, 3, 19, 18, 3, 16, 597033)),
        ),
    ]
