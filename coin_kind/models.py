from django.db import models
from common.models import CommonModel


# Create your models here.
class CoinKind(CommonModel):
    coin_name = models.CharField(
        max_length=30,
    )
    # 코인의 티커 심볼 (예: BTC, ETH)
    ticker_symbol = models.CharField(
        max_length=10,
    )
    # 코인의 간단한 설명
    description = models.TextField()

    # # 코인의 시가총액 (단위: 원)
    # market_cap = models.DecimalField(max_digits=15, decimal_places=2)
    # # 코인의 현재 가격 (단위: 원)
    # current_price = models.DecimalField(max_digits=10, decimal_places=5)
    # # 코인의 거래량 (단위: 원)
    # trading_volume = models.DecimalField(max_digits=15, decimal_places=2)
    # # 코인의 유통 공급량 (단위: 개)
    # circulating_supply = models.DecimalField(max_digits=15, decimal_places=2)
    # # 코인의 최대 공급량 (단위: 개)
    # max_supply = models.DecimalField(max_digits=15, decimal_places=2)
    # # 코인의 가격 변동성 (예: 0.0345)
    # price_volatility = models.DecimalField(max_digits=5, decimal_places=4)
    # 코인의 공식 웹사이트 URL
    website = models.URLField()
    # 필요한 필드를 추가하세요

    def __str__(self):
        return self.coin_name

    class Meta:
        verbose_name_plural = "코인 종류"
