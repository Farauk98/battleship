# Generated by Django 4.2.9 on 2024-01-15 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mybattleship', '0008_alter_battle_grid_id_alter_battlefield_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='battlefield',
            name='opponent',
        ),
    ]
