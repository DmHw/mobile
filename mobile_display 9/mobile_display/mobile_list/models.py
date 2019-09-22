# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Liantong(models.Model):
    mobile_name = models.TextField(blank=True, null=True)
    mobile_price = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'liantong'


class MobileDianxinFormated(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mobile_dianxin_name = models.TextField(blank=True, null=True)
    mobile_dianxin_price = models.FloatField(blank=True, null=True)

    class Meta:
       # managed = False
        db_table = 'mobile_dianxin_formated'


class MobileLiantongFormated(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mobile_liantong_name = models.TextField(blank=True, null=True)
    mobile_liantong_price = models.FloatField(blank=True, null=True)

    class Meta:
       # managed = False
        db_table = 'mobile_liantong_formated'


class MobileYidongFormated(models.Model):
    id = models.BigIntegerField(primary_key=True)
    mobile_yidong_name = models.TextField(blank=True, null=True)
    mobile_yidong_price = models.FloatField(blank=True, null=True)

    class Meta:
        #managed = False
        db_table = 'mobile_yidong_formated'


class Yidong(models.Model):
    mobile_yidong_name = models.TextField(blank=True, null=True)
    mobile_yidong_price = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'yidong'
