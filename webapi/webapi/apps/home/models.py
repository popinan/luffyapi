from django.db import models
from webapi.utils.models import BaseModel

# Create your models here.


class Banner(BaseModel):
    """轮播图"""
    # 字段声明
    image = models.ImageField(upload_to='banner', null=True, blank=True, verbose_name='轮播图片')
    link = models.URLField(max_length=200, verbose_name='广告链接')
    name = models.CharField(max_length=200, verbose_name='广告标题')
    note = models.TextField(null=True, blank=True, verbose_name='备注信息')

    # 表信息
    class Meta:
        db_table = 'banner'
        verbose_name = '轮播广告'
        verbose_name_plural = verbose_name  # 避免出现多个复数数据时，自动加"s"，设置复数和单数一致

    # 自定义字段/查询方法
    def __str__(self):
        return self.name
