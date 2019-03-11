from django.db import models

class Player(models.Model):
    player_id = models.IntegerField(primary_key=True)
    player_name = models.CharField(max_length=64)

    def __str__(self):
        return player_name

class Asset(models.Model):
    player_id = models.OneToOneField(Player, on_delete=models.PROTECT, primary_key=True)
    fund = models.IntegerField(default=10000)
    stock = models.IntegerField(default=50)

    def __str__(self):
        return str(fund)

class Phase(models.Model):
    phase_id = models.IntegerField(primary_key=True)
    price = models.IntegerField(default=200)

    def __str__(self):
        return str(phase_id)

class Trade(models.Model):
    trade_id = models.IntegerField(primary_key=True)
    quantity = models.IntegerField(default=0)
    player_id = models.ForeignKey(Player, on_delete=models.PROTECT)
    phase_id = models.ForeignKey(Phase, on_delete=models.PROTECT)

    def __str__(self):
        return str(trade_id)
