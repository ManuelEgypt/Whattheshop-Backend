# Generated by Django 2.2.6 on 2019-10-14 06:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20191014_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(days=5)),
        ),
    ]
