# Generated by Django 4.2.16 on 2024-11-21 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("TicTacToe", "0005_remove_tictactoegame_board_state"),
    ]

    operations = [
        migrations.AddField(
            model_name="tictactoegame",
            name="board_state",
            field=models.CharField(default="---------", max_length=9),
        ),
    ]
