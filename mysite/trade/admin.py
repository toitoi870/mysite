from django.contrib import admin
from .models import Player, Asset, Trade, Phase

admin.site.register(Player)
admin.site.register(Asset)
admin.site.register(Trade)
admin.site.register(Phase)

# Register your models here.
