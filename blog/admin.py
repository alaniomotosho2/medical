# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Post, Comment


from markdownx.admin import MarkdownxModelAdmin
from .models import  Download

#admin.site.register(Post)


#from django.contrib import admin
#from .models import Post
#class PostAdmin(admin.ModelAdmin):
#	list_display = ('title', 'slug', 'author', 'publish','status')




class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish','status')
	#admin.site.register(Post, PostAdmin)
	list_filter = ('status', 'created', 'publish', 'author')
	search_fields = ('title','body')
	prepopulated_fields = {'slug': ('title',)}
	raw_id_fields = ('author',)
	date_hierarchy = 'publish'
	ordering = ['status', 'publish']

	#myfield = MarkdownxField()

class CommentAdmin(admin.ModelAdmin):
	list_display = ('name', 'email', 'post', 'created', 'active')
	list_filter = ('active', 'created', 'updated')
	search_fields = ('name', 'email', 'body')


class DownloadAdmin(admin.ModelAdmin):
	list_display = ('filee','comments')


#admin.site.register(MyModel, MarkdownxModelAdmin)

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Download,DownloadAdmin);