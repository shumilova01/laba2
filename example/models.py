# -*- coding: utf-8 -*-
from django.db import models

class Produkty(models.Model):
    
    Naimenovanie = models.CharField(max_length=30)
    ed_izmereniya = models.CharField(max_length=10)
    Adres_proizvoditelya = models.CharField(max_length=30)

    
class Sklady(models.Model):
    naimenovanie = models.CharField(max_length=50)
    address_sklada = models.CharField(max_length=70)
    gorod = models.CharField(max_length=17, blank=True)
    kruglosutochno = models.CharField(max_length=100, blank=True)
 



class Postavki(models.Model):
    produkty = models.ForeignKey(Produkty)
    sklady = models.ForeignKey(Sklady)
    operaciya = models.CharField(max_length=50)
    kolichestvo = models.IntegerField()
    



     