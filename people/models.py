from __future__ import unicode_literals

from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=256)
    age = models.IntegerField()

    def __str__(self):
    # def __unicode__(self):
        return "name: %s , age: %d " %(self.name,self.age)