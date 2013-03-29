from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from blogmodule.models import Post, Tag
from blogmodule.forms import AddPostForm
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    """ Add a post to blog """

    lastestPosts = Post.objects.all().order_by('-creationDate')
    return render(request, 'blogmodule/post.html', {'posts': lastestPosts})

def post(request, postId):
    """ Add a post to blog """
    try:
        posts = Post.objects.get(pk=postId)
    except Post.DoesNotExist:
        raise Http404
    return render(request, 'blogmodule/post.html', {'posts': posts})

def tag(request, tagId):
    """ Add a post to blog """

    try:
        tag = Tag.objects.get(pk=tagId)
        postsByTag = tag.posts.order_by('-creationDate')
    except Tag.DoesNotExist:
        raise Http404
    return render(request, 'blogmodule/post.html',{'posts': postsByTag})


def add_form(request):
    """ Add a post to blog """
    form = AddPostForm(request.POST)
    return render(request, 'blogmodule/add_form.html', {'form': form})
    

def insert_post(request):
    """ Add a post to blog """

    # A the moment there is no check to control if fields are empty

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            postTitle = form.cleaned_data['title']
            postBody = form.cleaned_data['body']
            postTags = form.cleaned_data['tags']

            # Tags become uppercase because it's simplier to handle
            tagList = [el.strip().upper() for el in postTags.split(',')] 

            # This should be done in one transaction
            
            post = Post(title=postTitle,body=postBody,creationDate=timezone.now())
            post.save()
            tempTag = None
            for tag in tagList:
                try:
                    tempTag = Tag.objects.get(name=tag)
                except ObjectDoesNotExist:
                    tempTag = Tag(name=tag)
                    tempTag.save()
                post.tag_set.add(tempTag)
            post.save()
            
#        else:
#            form = AddPostForm()
            
    return HttpResponseRedirect('/blog/')