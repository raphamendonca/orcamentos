# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-15 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name_plural': 'clientes',
                'verbose_name': 'cliente',
            },
            bases=('crm.person',),
        ),
        migrations.AlterField(
            model_name='person',
            name='person_type',
            field=models.CharField(blank=True, choices=[('c', 'cliente'), ('p', 'contato')], max_length=1, verbose_name='cliente ou contato'),
        ),
    ]
