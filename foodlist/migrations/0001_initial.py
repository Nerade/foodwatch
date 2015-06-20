# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_name', models.CharField(max_length=30)),
                ('price_rule', models.FloatField(default=0.4, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('ean_code', models.IntegerField(max_length=13, serialize=False, primary_key=True)),
                ('storage', models.CharField(max_length=2, choices=[(b'CF', b'Cafete'), (b'LD', b'Langer Dachboden'), (b'VD', b'Vorderer Dachboden'), (b'MK', b'Mate Keller'), (b'TK', b'Tiefk\xc3\xbchler'), (b'KS', b'K\xc3\xbchlschrank'), (b'SO', b'Sontiges')])),
                ('item_name', models.CharField(max_length=30)),
                ('prime_cost', models.DecimalField(max_digits=5, decimal_places=2)),
                ('premium_cost', models.DecimalField(editable=False, max_digits=5, decimal_places=2)),
                ('member_cost', models.DecimalField(editable=False, max_digits=5, decimal_places=2)),
                ('guest_cost', models.DecimalField(editable=False, max_digits=5, decimal_places=2)),
                ('energy', models.BooleanField(default=False)),
                ('description', models.TextField(null=True, blank=True)),
                ('category', models.ForeignKey(to='foodlist.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
