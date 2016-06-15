#-*- coding:utf8 -*-
from __future__ import unicode_literals

from django.db import models



class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'出版社'
        verbose_name_plural = verbose_name
        # app_label = u'忆'
        ordering = ['name']
        # db_table = 'books_publisher'

class Author(models.Model):
    first_name = models.CharField(max_length=30,verbose_name='名字')
    last_name = models.CharField(max_length=40,verbose_name='姓名')
    email = models.EmailField(blank=True,verbose_name='e-mail')

    def __str__(self):
        return u'%s %s' % (self.first_name,self.last_name)

    class Meta:
        verbose_name = u'作者'
        verbose_name_plural = verbose_name
        # app_label = u'忆'
        # db_table = 'books_author'

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = u'书本'
        verbose_name_plural = verbose_name
        # app_label = u'忆'
        # db_table = 'books_book'
