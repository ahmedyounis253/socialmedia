# Generated by Django 3.2.5 on 2021-09-11 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_alter_group_published_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
