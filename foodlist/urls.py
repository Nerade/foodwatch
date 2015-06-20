from __future__ import absolute_import

from django.conf.urls import patterns, url
from foodlist.views import ItemListView, ItemDetailView

urlpatterns = patterns('',
            url(r'^item/(?P<item_id>\d+)$',ItemDetailView.as_view(),name='item-detail'),
            url(r'^$',ItemListView.as_view(),name='item-list'),
            )