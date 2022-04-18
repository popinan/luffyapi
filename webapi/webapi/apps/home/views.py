from django.shortcuts import render
from rest_framework.generics import ListAPIView

from .models import Banner, Nav
from .serializers import BannerListModelSerializer, NavListModelSerializer
from webapi.settings import constants


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by('-orders', '-id')[:constants.HOME_BANNER_LENGTH]
    serializer_class = BannerListModelSerializer


class HeaderNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False, position=1).order_by('-orders', '-id')[:constants.HOME_HEADER_LENGTH]
    serializer_class = NavListModelSerializer


class FooterNavListAPIView(ListAPIView):
    queryset = Nav.objects.filter(is_show=True, is_delete=False, position=2).order_by('-orders', '-id')[:constants.HOME_FOOTER_LENGTH]
    serializer_class = NavListModelSerializer