# Generated by Django 3.2.5 on 2021-07-24 08:02

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210724_1001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 24, 8, 2, 2, 952438, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 24, 8, 2, 2, 915031, tzinfo=utc)),
        ),
    ]
