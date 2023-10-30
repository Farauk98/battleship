from django.contrib.auth.models import User
from django.db import models

class Player(User):
    score = models.IntegerField(default=0)


# Create your models here.
class Game(models.Model):
    score = models.IntegerField()

class Battle_grid(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE) 
    x = models.IntegerField()
    y = models.IntegerField()
    is_ship = models.BooleanField()
    def __str__(self):
        if self.is_ship:
            f"X at ({self.x}, {self.y}) in Game {self.game_id}"
        else:
            f"0 at ({self.x}, {self.y}) in Game {self.game_id}"

class Move(models.Model):
    battle_grid = models.ForeignKey(Battle_grid, on_delete=models.CASCADE)
    order = models.IntegerField()