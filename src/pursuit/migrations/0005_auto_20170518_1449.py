# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-18 06:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('pursuit', '0004_iddistributor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Vendor Name')),
                ('phone', models.CharField(max_length=40, unique=True, verbose_name='Phone Number')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('at', models.DateTimeField(auto_now_add=True, verbose_name='At')),
                ('by', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profiles.Profile')),
            ],
            options={
                'db_table': 'vendor',
            },
        ),
        migrations.CreateModel(
            name='VendorType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Vendor Type')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'db_table': 'vendor_type',
            },
        ),
        migrations.AddField(
            model_name='vendor',
            name='vendor_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='pursuit.VendorType'),
        ),
    ]
