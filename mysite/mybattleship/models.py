from django.contrib.auth.models import User
from django.db import models

class Player(User):
    score = models.IntegerField(default=0)


# Create your models here.
class Game(models.Model):
    score = models.IntegerField()
    comments = models.CharField(max_length = 200,default=None, null =True, blank =True)

class Battle_grid(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE) 
    x = models.IntegerField()
    y = models.IntegerField()
    is_ship = models.BooleanField()

    class Meta:
        unique_together = ('game', 'x','y')

    def __str__(self):
        if self.is_ship:
            return f"X at ({self.x}, {self.y}) in Game {self.game_id}"
        else:
            return f"0 at ({self.x}, {self.y}) in Game {self.game_id}"

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE,default=None, null =True, blank =True) 
    battle_grid = models.ForeignKey(Battle_grid, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        unique_together = ('game', 'order')