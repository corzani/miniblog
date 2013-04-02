from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    creationDate = models.DateTimeField()

    def __unicode__(self):
        return self.title

# Probably the next release ;)

class Comment(models.Model):
    post = models.ForeignKey(Post);
    comment = models.TextField()
    creationDate = models.DateTimeField()
    
class Tag(models.Model):
    name = models.CharField(max_length=20,unique=True)
    posts = models.ManyToManyField(Post)

    def __unicode__(self):
        return self.title

