from src.models import BaseModel
from rest_framework.serializers import ModelSerializer


class BaseModelSerializer(ModelSerializer):
    class Meta:
        model = BaseModel
        fields = '__all__'
        db_table = 'BaseModel'
        managed = True
        verbose_name = 'BaseModel'
        verbose_name_plural = 'BaseModels'
