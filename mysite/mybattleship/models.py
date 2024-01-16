from django.contrib.auth.models import User
from django.db import models

class Battlefield(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='owner')
    counter = models.IntegerField(default =0)


# Create your models here.
class Game(models.Model):
    score = models.IntegerField()
    comments = models.CharField(max_length = 200,default=None, null =True, blank =True)
    battlefield_1 = models.OneToOneField(Battlefield, on_delete=models.CASCADE, related_name='game_battlefield_1')
    battlefield_2 = models.OneToOneField(Battlefield, on_delete=models.CASCADE, related_name='game_battlefield_2')
    player1_move = models.BooleanField(default =True)
    winner =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='winner')


class Battle_grid(models.Model):
    battlefield = models.ForeignKey(Battlefield, on_delete=models.CASCADE) 
    x = models.IntegerField()
    y = models.IntegerField()
    is_ship = models.BooleanField()
    is_shot = models.BooleanField(default=False) 

    class Meta:
        unique_together = ('battlefield', 'x','y')

    def __str__(self):
        if self.is_ship:
            return f"X at ({self.x}, {self.y}) in Battlefield {self.battlefield_id}, is {self.is_shot}"
        else:
            return f"0 at ({self.x}, {self.y}) in Battlefield {self.battlefield_id}, is {self.is_shot}"

class Boat(models.Model):
    battle_grids = models.ManyToManyField(Battle_grid)
    size = models.IntegerField()
    life = models.IntegerField()
    is_dead = models.BooleanField()

    def save(self, *args, **kwargs):
        # Set default value for life based on size if not provided
        if self.life is None:
            self.life = self.size
        super().save(*args, **kwargs)

class Move(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE,default=None, null =True, blank =True) 
    battle_grid = models.OneToOneField(Battle_grid, on_delete=models.CASCADE)
    order = models.IntegerField()

    class Meta:
        unique_together = ('game', 'order')
    
    def __str__(self):
         return f"{self.order} - {self.battle_grid}"
    
class Invitation(models.Model):
    player1 =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='player1')
    player2 =  models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='player2')
    ships_sizes = models.JSONField(default=list)
    accept = models.BooleanField(default = False)
    
    def set_ships(self, sizes_list):
        self.ships_sizes = sizes_list

    def get_ships(self):
        return self.ships_sizes
    
from django.utils import timezone

class ChatMessage(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name='chat_messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Message from {self.sender} in game {self.game.id}'