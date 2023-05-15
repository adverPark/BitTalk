from django.contrib import admin
from .models import CoinKind

# Register your models here.


@admin.register(CoinKind)
class CoinKindAdmin(admin.ModelAdmin):
    list_display = (
        "coin_name",
        "ticker_symbol",
        "website",
    )
