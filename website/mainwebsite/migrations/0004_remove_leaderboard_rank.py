# Generated by Django 2.2.3 on 2019-09-24 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainwebsite', '0003_auto_20190924_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leaderboard',
            name='rank',
        ),
    ]
