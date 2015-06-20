# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(null=False,max_length=30)
    price_rule = models.DecimalField(max_digits=4,decimal_places=3,default=1.4,blank=True)
    
    def __unicode__(self):
        return self.category_name


class Item(models.Model):
    STORAGE_ROOMS = (
                     ('CF','Cafete'),
                     ('LD','Langer Dachboden'),
                     ('VD','Vorderer Dachboden'),
                     ('MK','Mate Keller'),
                     ('TK','Tiefkühler'),
                     ('KS','Kühlschrank'),
                     ('SO','Sontiges'),
                      )
    
    ean_code = models.IntegerField(primary_key=True,max_length=13)
    category = models.ForeignKey(Category)
    storage = models.CharField(max_length=2, choices=STORAGE_ROOMS)
    image = models.ImageField(blank=True,null=True,upload_to='product_images')
    image_thumbnail = ImageSpecField(source='image',
                                     processors=[ResizeToFill(100,100)],
                                     format='PNG',
                                     )
    
    item_name = models.CharField(max_length=30)
    prime_cost = models.DecimalField(max_digits=5,decimal_places=2)
    premium_cost = models.DecimalField(editable=False,max_digits=5,decimal_places=2)
    member_cost = models.DecimalField(editable=False,max_digits=5,decimal_places=2)
    guest_cost = models.DecimalField(editable=False,null=False,max_digits=5,decimal_places=2)
    energy = models.BooleanField(default=False,blank=True)
    description = models.TextField(blank=True,null=True)
    
    def save(self):
        
        self.premium_cost = self.prime_cost * self.category.price_rule
        self.member_cost = self.premium_cost * self.category.price_rule
        self.guest_cost = self.member_cost * self.category.price_rule
        super(Item,self).save()
    
    def __unicode__(self):
        return self.item_name +"(" + str(self.ean_code) + ")"
    