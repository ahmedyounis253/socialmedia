# Generated by Django 3.2.5 on 2021-09-06 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_remove_group_posts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='published_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
