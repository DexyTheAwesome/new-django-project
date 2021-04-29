from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE,)
    body = models.TextField(null=True)
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])
    
    
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=50, default='', editable=True)
    comment = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    
    
    # def get_absolute_url(self):
    #     return reverse('post_detail')
    

    class Meta:
    
        ordering = ['created_on']
    

        def __str__(self):
            return 'Comment {} by {}'.format(self.comment, self.name)
    

    