


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_board_owner'),
        ('user', '0003_alter_myuser_boardstocollaborate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='boardsToCollaborate',
            field=models.ManyToManyField(blank=True, related_name='team', to='tasks.Board'),
        ),
    ]
