from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    # slug means inteded for use in URLs
    # slug = a short label that contains only letters, numbers, underscores, or hyphens
    # Add unique_for_date parameter to this field so that you can build URLs for posts using their publish date and slug
    # Django will prevent multiple posts from having the same slug for a given date.
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES, 
                              default='draft')

    class Meta:
        ordering = ('-publish', )
    
    def __srt__(self):
        return self.title