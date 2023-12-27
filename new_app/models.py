from django.db import models


class Ticker(models.Model):
    symbol = models.CharField(max_length=24)
    volume = models.CharField(max_length=512)
    trade_price = models.CharField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"symbol: {self.symbol}: {self.trade_price}"
