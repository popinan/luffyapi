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


class  Nav(BaseModel):
    """导航栏"""
    POSITION_OPTION = (
        (1, '顶部导航'),
        (2, '脚部导航'),
    )
    # 字段声明
    name = models.CharField(max_length=200, verbose_name='导航标题')
    link = models.CharField(max_length=200, verbose_name='导航链接')
    position = models.IntegerField(choices=POSITION_OPTION, default=1, verbose_name='导航位置')
    is_site = models.BooleanField(default=False, verbose_name='是否是站外地址')

    # 表信息
    class Meta:
        db_table = 'nav'
        verbose_name = '导航菜单'
        verbose_name_plural = verbose_name  # 避免出现多个复数数据时，自动加"s"，设置复数和单数一致

    # 自定义字段/查询方法
    def __str__(self):
        return self.name

