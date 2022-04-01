from django.db import models


class BaseModel(models.Model):
    is_show = models.BooleanField(verbose_name="是否上架", default=False)
    orders = models.IntegerField(default=0, verbose_name='显示顺序')
    is_delete = models.BooleanField(default=False, verbose_name="逻辑删除")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        # 把当前类设置为django的抽象模型，那么django在数据迁移的时候，就不会对这个模型进行数据表的创建
        abstract = True