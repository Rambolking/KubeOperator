#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''=================================================
@Author ：zk.wang
@Date   ：2020/3/13
=================================================='''

from rest_framework.routers import DefaultRouter
from django.urls import path
from message_center import api

app_name = "message_center"
router = DefaultRouter()

router.register('notification/subscribe', api.SubscribeViewSet, 'subscribe')


urlpatterns = [
                  path('notification/email/check/', api.EmailCheckView.as_view()),
                  path('notification/workWeixin/check/', api.WorkWeixinCheckView.as_view()),
              ] + router.urls
