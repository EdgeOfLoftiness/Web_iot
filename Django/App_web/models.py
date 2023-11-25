from django.db import models

from django.db import models

class PC(models.Model):
    name = models.CharField(max_length=100)

class GPU(models.Model):
    name = models.CharField(max_length=100)

class CPU(models.Model):
    name = models.CharField(max_length=100)

class Fan(models.Model):
    name = models.CharField(max_length=100)

class Motherboard(models.Model):
    name = models.CharField(max_length=100)
