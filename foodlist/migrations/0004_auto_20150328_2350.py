# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodlist', '0003_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='price_rule',
            field=models.DecimalField(default=1.4, max_digits=4, decimal_places=3, blank=True),
            preserve_default=True,
        ),
    ]
