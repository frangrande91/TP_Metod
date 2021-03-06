# Generated by Django 3.2.9 on 2021-11-17 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20211117_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='tasks.board'),
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='tasks.category'),
        ),
    ]
