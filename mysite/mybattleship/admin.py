from django.contrib import admin

from .models import Player, Game, Battle_grid, Move

admin.site.register(Player)
admin.site.register(Game)
admin.site.register(Battle_grid)
admin.site.register(Move)