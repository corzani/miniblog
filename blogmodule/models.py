from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    creationDate = models.DateTimeField('blog entry date') 

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post);
    comment = models.TextField()
    creationDate = models.DateTimeField('comment date')

class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True)
    posts = models.ManyToManyField(Post)

    def __unicode__(self):
        return self.title

