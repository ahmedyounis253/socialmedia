# Generated by Django 3.2.5 on 2021-07-24 08:01

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210723_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 24, 8, 1, 22, 970093, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 24, 8, 1, 22, 932190, tzinfo=utc)),
        ),
    ]
