from django.contrib import admin

from .models import Invitation, Battlefield, Game, Battle_grid, Move

admin.site.register(Game)
admin.site.register(Battle_grid)
admin.site.register(Move)
admin.site.register(Battlefield)
admin.site.register(Invitation)