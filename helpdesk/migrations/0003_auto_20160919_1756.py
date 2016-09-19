# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0002_auto_20160906_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customfield',
            name='label',
            field=models.CharField(help_text='The display label for this field', max_length=30, verbose_name='Label'),
        ),
    ]
