from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.utils import timezone
from blogmodule.models import Post, Tag
from blogmodule.forms import AddPostForm, AddCommentForm
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    """ Add a post to blog """

    lastestPosts = Post.objects.all().order_by('-creationDate')
    return render(request, 'blogmodule/post.html', {'posts': lastestPosts, 'viewFullData' : False})

def post(request, postId):
    """ Add a post to blog """
    try:
        posts = [Post.objects.get(pk=postId)]
        form = AddCommentForm()
    except Post.DoesNotExist:
        return HttpResponseRedirect('/blog/')
    return render(request, 'blogmodule/post.html', {'posts': posts, 'viewFullData' : True,'form' : form}) # , 'comments' : comments})

def delete_post(request, postId):
    """ Add a post to blog """
    
    post = Post.objects.get(pk=postId).delete()
    
    return HttpResponseRedirect('/blog/')



def tag(request, tagId):
    """ Add a post to blog """

    try:
        tag = Tag.objects.get(pk=tagId)
        postsByTag = tag.posts.order_by('-creationDate')
    except Tag.DoesNotExist:
        raise Http404
    return render(request, 'blogmodule/post.html', {'posts': postsByTag, 'viewFullData' : False})

def add_form(request):
    """ Add a post to blog """
    form = AddPostForm()
    return render(request, 'blogmodule/add_form.html', {'form': form})

def insert_comment(request, postId):
    if request.method == 'POST':
        form = AddCommentForm(request.POST)
        if form.is_valid():
            postComment = form.cleaned_data['comment']
            try:
                tempPost = Post.objects.get(pk=postId)
                tempPost.comment_set.create(comment=postComment, creationDate=timezone.now())
                tempPost.save()
            except ObjectDoesNotExist:
                # Post doesn't exist, at the moment I simply redirect to home page without showing alerts...
                return HttpResponseRedirect('/blog/')

    # 
    return HttpResponseRedirect('/blog/post/'+postId)
    

def insert_post(request):
    """ Add a post to blog """

    # A the moment there is no check to control if fields are empty

    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            postTitle = form.cleaned_data['title']
            postBody = form.cleaned_data['body']
            postTags = form.cleaned_data['tags'].strip()

            # Tags become uppercase because it's simplier to handle
            tagList = [el.strip().upper() for el in postTags.split(',')]
            
            # Delete empty tags...
            tagList = [el for el in tagList if el != ""]

            # This should be done in one transaction
            
            post = Post(title=postTitle, body=postBody, creationDate=timezone.now())
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
            return HttpResponseRedirect('/blog/')
            
    return render(request, 'blogmodule/add_form.html', {'form': form})
