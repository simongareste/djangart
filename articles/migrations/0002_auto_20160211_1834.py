# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-11 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlecategory',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.ArticleCategory'),
        ),
    ]
