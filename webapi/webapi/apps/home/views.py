from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Banner
from .serializers import BannerListModelSerializer
from webapi.settings import constants


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by('-orders', '-id')[:constants.HOME_BANNER_LENGTH]
    serializer_class = BannerListModelSerializer
