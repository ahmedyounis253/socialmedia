# Generated by Django 3.2.5 on 2021-09-02 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_rename_t_account_groups'),
        ('posts', '0001_initial'),
        ('groups', '0002_rename_t_group_members'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='members', through='groups.Membership', to='accounts.Account'),
        ),
        migrations.AlterField(
            model_name='group',
            name='posts',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.post'),
        ),
    ]
