# Generated by Django 4.2.6 on 2023-11-08 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybattleship', '0002_game_comments_move_game'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='move',
            unique_together={('game', 'order')},
        ),
    ]
