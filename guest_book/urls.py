# -*- coding=utf-8 -*-
from django.conf.urls import url
from guest_book import views
urlpatterns = [
    url(r'^guestbook/(?P<pid>\d+)*',views.guestbook),

]
