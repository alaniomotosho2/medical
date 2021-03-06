# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager

from markdownx.models import MarkdownxField

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.widgets import CKEditorWidget

#from .models import Post, Comment
#from .forms import EmailPostForm, CommentForm



#this just enehanced not a must though---creating custom manager
class PublishedManager(models.Manager):
	def get_queryset(self):
		return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):
	STATUS_CHOICES = (('draft', 'Draft'),('published', 'Published'),)
	title = models.CharField(max_length=250)
	slug = models.SlugField(max_length=250,unique_for_date='publish')
	author = models.ForeignKey(User,related_name='blog_posts')
	#body = models.TextField()
	body = RichTextUploadingField()
	#body = MarkdownxField()
	publish = models.DateTimeField(default=timezone.now)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')

	objects = models.Manager() # The default manager.
	published = PublishedManager() # Our custom manager.
	tags = TaggableManager()

	def get_absolute_url(self):
		return reverse('blog:post_detail',args=[self.publish.year,self.publish.strftime('%m'),
			self.publish.strftime('%d'),self.slug])

	class Meta:
		ordering = ('-publish',)

	def __str__(self):
		return self.title


class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='comments')
	name = models.CharField(max_length=80)
	email = models.EmailField()
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	class Meta:
		ordering = ('created',)

	def __str__(self):
		return 'Comment by {} on {}'.format(self.name, self.post)






#class MyModel(models.Model):
#	body = MarkdownxField()


class Download(models.Model):
	comments = models.CharField(max_length=200);
	filee = models.FileField()




#class Postt(models.Model):
#	content = RichTextField()
#	cont = RichTextUploadingField()

