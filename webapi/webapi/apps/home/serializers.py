from rest_framework import serializers
from .models import Banner


class BannerListModelSerializer(serializers.ModelSerializer):
    """轮播广告的序列化器"""
    # 模型序列化器的相关声明
    class Meta:
        model = Banner
        fields = ['image', 'link', 'name']
