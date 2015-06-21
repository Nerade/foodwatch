from __future__ import absolute_import

from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormMixin
from django.db.models import Q

from foodlist.models import Item

# Create your views here.

class ItemListView(ListView):
    
    model = Item
    template_name = 'foodlist/item_list.html'    
    redirect = False
    
    def get_queryset(self):
        try:
            query_term = self.request.GET['q'] 
        except:
            query_term = ''
            object_list = self.model.objects.all()
            
        try:
            object_list = self.model.objects.filter(ean_code__exact=query_term)
        except:
            object_list = self.model.objects.filter(Q(item_name__contains=query_term) | Q(description__contains=query_term)).order_by('item_name')
            
        if(object_list.count() == 1):
            self.redirect = True
            self.redirect_to = object_list[0].ean_code
            
        return object_list
        
    def get_context_data(self, **kwargs):
        context = super(ItemListView, self).get_context_data(**kwargs)
        return context
    def render_to_response(self, context):

        if self.redirect:
            return redirect('item/'+str(self.redirect_to))
    
        return super(ItemListView, self).render_to_response(context)
    

class ItemDetailView(DetailView):
    
    model = Item
    
    def get_context_data(self, **kwargs):
        context = super(ItemDetailView, self).get_context_data(**kwargs)
        return context