# Generated by Django 3.0.14 on 2023-12-15 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mybattleship', '0006_game_player1_move'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battlefield',
            name='player',
        ),
        migrations.AddField(
            model_name='battlefield',
            name='opponent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opponent', to='mybattleship.Player'),
        ),
        migrations.AddField(
            model_name='battlefield',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='mybattleship.Player'),
        ),
    ]