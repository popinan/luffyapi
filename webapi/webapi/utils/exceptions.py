from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status
from django.db import DatabaseError
from redis import RedisError
import logging
log = logging.getLogger("django")


def custom_exception_handler(exc, context):
    """
        自定义异常处理
        :param exc: 异常类
        :param context: 抛出异常的上下文
        :return: Response响应对象
    """
    response = exception_handler(exc, context)
    if response is None:
        """当response结果为None时，则当前程序运行的结果有2种可能： 
            1. 程序真的没有报错！
            2. 程序报错了，但是drf框架不识别!
        """
        view = context['view']
        if isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
            """数据库异常"""
            log.error('[%s] %s' % (view, exc))
            return Response({'message': '系统内部存储错误！'}, status=status.HTTP_507_INSUFFICIENT_STORAGE)
    return response




