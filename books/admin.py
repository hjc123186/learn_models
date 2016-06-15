#-*- coding:utf8 -*-
# Register your models here.
from django.contrib import admin
from books.models import Publisher,Author,Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','email')
    search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher','publication_date')
    list_filter = ('publication_date',)
    search_fields = ('title',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    # fields = ('title','authors','publisher','publication_date')
    filter_horizontal = ('author',)
    raw_id_fields = ('publisher',)
    # fieldsets = (
    #     ('书',{'fields':('title',)}),
    #      )


admin.site.register(Publisher)
# admin.site.register(Author)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Book,BookAdmin)
