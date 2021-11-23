# Generated by Django 3.2.9 on 2021-11-22 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_board_owner'),
        ('user', '0002_auto_20211122_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='boardsToCollaborate',
            field=models.ManyToManyField(blank=True, null=True, related_name='team', to='tasks.Board'),
        ),
    ]
