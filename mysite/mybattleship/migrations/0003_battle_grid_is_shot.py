# Generated by Django 3.0.14 on 2023-12-14 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mybattleship', '0002_remove_boat_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='battle_grid',
            name='is_shot',
            field=models.BooleanField(default=False),
        ),
    ]
