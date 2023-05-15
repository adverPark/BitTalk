from django.db import models


class CommonModel(models.Model):

    """기본적인 모델 생성 : 아래 모델이 공통이기 때문에."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 데이터 베이스 등록을 하지 않기 위해.
    class Meta:
        abstract = True
