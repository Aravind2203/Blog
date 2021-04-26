from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,ViewsModel,Comment,Like,Category
from django.core.paginator import Paginator
# Create your views here.



def home(request):
    post=Post.objects.all()
    post=post[:3]
    categories=Category.objects.all()
    return render(request,'index.html',context={'post':post,'categories':categories})

def blogViewPage(request,slug):
    if not request.session.exists(request.session.session_key):
        request.session.create()

    posts=Post.objects.filter(TitleSlug=slug)
    if len(posts)>0:
        post=posts[0]
        views=ViewsModel.objects.filter(User=request.session.session_key)
        if len(views)>0:
            for view in views:
                if view.Post==post:
                    break
            else:
                post.Views=post.Views+1
                post.save(update_fields=['Views'])

                NewViewObject=ViewsModel(User=request.session.session_key,Post=post)
                NewViewObject.save()
        else:
            post.Views=post.Views+1
            post.save(update_fields=['Views'])

            NewViewObject=ViewsModel(User=request.session.session_key,Post=post)
            NewViewObject.save()
        comments=Comment.objects.filter(Post=post)
        return render(request,'content.html',{'post':post,'comments':comments})

    else:
        return HttpResponse('''
        <h1>Error 404 </h1>
        <h6>Page not Found!</h6>
        ''')

def like(request,slug):
    if not request.session.exists(request.session.session_key):
        request.session.create()

    posts=Post.objects.filter(TitleSlug=slug)
    if len(posts)>0:
        post=posts[0]
        likes=Like.objects.filter(User=request.session.session_key)
        if len(likes)>0:
            for like in likes:
                if like.Post==post:
                    break
            else:
                post.Likes=post.Likes+1
                post.save(update_fields=['Likes'])

                newLike=Like(User=request.session.session_key,Post=post)
                newLike.save()
        else:
            post.Likes=post.Likes+1
            post.save(update_fields=['Likes'])

            newLike=Like(User=request.session.session_key,Post=post)
            newLike.save()
        return redirect('posts',slug=slug)
    else:
        return HttpResponse(posts)

def addComment(request,slug):
    if not request.session.exists(request.session.session_key):
        request.session.create()
    if request.method=='POST':
        posts=Post.objects.filter(TitleSlug=slug)
        if len(posts)>0:
            post=posts[0]

            comment=request.POST.get('comment')
            
            newCommentObject=Comment(Name=request.session.session_key,Comment=comment,Post=post)
            newCommentObject.save()
            
            post.CommentCount+=1
            post.save(update_fields=['CommentCount'])
            return redirect('posts',slug=slug)
        else:
            return HttpResponse('''
            <h1>Invalid Request</h1>
            <h3>Post does not exist.</h3>
            ''')
    else:
        return redirect('home')


def categoryFilter(request,category):
    categoryObjects=Category.objects.filter(Name=category)
    if len(categoryObjects)>0:
        categoryObject=categoryObjects[0]
        posts=Post.objects.filter(Category=categoryObject)
        paginator=Paginator(posts,8)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        return render(request,'blog.html',context={'page_obj':page_obj})

'''
contact_list = Contact.objects.all()
    paginator = Paginator(contact_list, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list.html', {'page_obj': page_obj})
'''
