from __future__ import absolute_import

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from foodlist.models import Item

# Create your views here.

class ItemListView(ListView):
    
    model = Item 
    
    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        return context

class ItemDetailView(DetailView):
    
    model = Item