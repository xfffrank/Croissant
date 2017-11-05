from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from markdownx.models import MarkdownxField

# Create your models here.

# class Category(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class Tag(models.Model):
#     name = models.CharField(max_length=100)
#
#     def __str__(self):
#         return self.name

class Post(models.Model):
    """
    title：题目；
    body：文章内容；
    created_time：创建时间；
    modified_time：最后一次修改时间；
    author：作者；
    category：博文分类；
    tags：标签；
    """
    title = models.CharField(max_length=70)
    # body = models.TextField()
    body = MarkdownxField()

    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # category = models.ForeignKey(Category)
    # tags = models.ManyToManyField(Tag, blank=True)

    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

class AboutMe(models.Model):
    title = models.CharField(max_length=70)
    body = MarkdownxField()
    # subheading = models.CharField(max_length=70)

    def __str__(self):
        return self.title




