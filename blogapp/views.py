from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,ViewsModel,Comment,Like,Category,Courosel,AboutUs,ReaderList
from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.
'''
def sample(request,slugtitle):
    if not request.session.exists(request.session.session_key):
            request.session.create()
    p=Post.objects.filter(TitleSlug=slugtitle)
    if p.exists():
        v=ViewsModel.objects.filter(User=request.session.session_key)
        
        if len(v)>0:
            vobject=v[0]
            if vobject.Post==p[0]:
                pass
            else:
            p=Post.objects.get(TitleSlug=slugtitle)
            p.Views=p.Views+1
            p.save(update_fields=['Views'])
            #v=ViewsModel(User=request.session.session_key,Post=p)
            
        else:
            p=Post.objects.get(TitleSlug=slugtitle)
            p.Views=p.Views+1
            p.save(update_fields=['Views'])
            v=ViewsModel(User=request.session.session_key,Post=p)
            
            v.save()
        p=Post.objects.get(TitleSlug=slugtitle)
        print(p.Content)
        return render(request,'sample.html',context={'post':p})
    else:
        return HttpResponse("Error")
'''


def home(request):
    post=Post.objects.all()    
    post=post[:3]
    categories=Category.objects.all()
    courosels=Courosel.objects.all()
    aboutus=AboutUs.objects.all()
    if len(aboutus)>0:
        about=aboutus[0]
        return render(request,'index.html',context={'post':post,'categories':categories,'courosels':courosels,'about':about})
    else:
        return render(request,'index.html',context={'post':post,'categories':categories,'courosels':courosels})

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
        categories=Category.objects.all()
        return render(request,'content.html',{'post':post,'comments':comments,'categories':categories})

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
    categoryObjects=Category.objects.filter(SlugName=category)
    if len(categoryObjects)>0:
        categoryObject=categoryObjects[0]
        posts=Post.objects.filter(Category=categoryObject)
        paginator=Paginator(posts,8)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        categories=Category.objects.all()
        return render(request,'blog.html',context={'page_obj':page_obj,'categories':categories})

def search(request):
    query=request.GET.get('search')
    
    posts=[]
    for q in set(query.split()):
        post=Post.objects.filter(Q(Title__contains=q) | Q(OverView__contains=q) |Q(Content__contains=q))
        if post not in posts:
            posts.extend(post)
    if len(posts)>0:
        paginator=Paginator(posts,8)
        page_number=request.GET.get('page')
        page_obj=paginator.get_page(page_number)
        categories=Category.objects.all()
        return render(request,'blog.html',context={'page_obj':page_obj,'categories':categories})
    else:
        return HttpResponse('''<h1>
        Bad query
        </h1>''')

def addReader(request):
    email=request.POST.get('email')
    reader=ReaderList(Email=email)
    reader.save()
    return redirect('home')