from django.shortcuts import render, HttpResponse,redirect,get_object_or_404,reverse
from article.forms import ArticleForm
from django.contrib import messages
from article.models import Article,Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    context = {
        "numbers":[1,2,3,4,5,6,7,8]
    }
    return render(request,"index.html",context= context)
     #burası direk olarak templates içinde aramaya başlıyor belirtildiği gibi.

def addComment(request,id):
    article = get_object_or_404(Article,id=id)
    
    if request.method == "POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
    return redirect(reverse("article:detailarticle",kwargs={"id":id}))


def about(request):
    return render(request,"about.html")

def articles(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles= Article.objects.filter(title__contains = keyword)
        return render(request,"articles.html",{"articles":articles})
    articles = Article.objects.all()
    return render(request,"articles.html",{"articles":articles})


def detail(request,id):
    return HttpResponse("Detail:"  + str(id))

@login_required(login_url='user:login')
def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context={
        "articles" : articles
    }
    return render(request,"dashboard.html",context)

@login_required(login_url='user:login')
def addarticle(request):
    form =ArticleForm(request.POST or None, request.FILES or None)
    context={
        "form" : form
    }
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        
        messages.success(request,"Makale başarıyla kayıt edilmiştir.")
        return redirect("index")
    return render(request,"addarticle.html",context)
    
@login_required(login_url='user:login')
def updatearticle(request,id):
    article = get_object_or_404(Article,id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        
        messages.success(request,"Makale başarıyla güncellendi.")
        return redirect("index")
    context={
        "form":form
    }
    return render(request,"updatearticle.html",context)

@login_required(login_url='user:login')
def deletearticle(request,id):
    article = get_object_or_404(Article, id=id)
    article.delete()
    messages.success(request,"Makale Başarıyla Silindi.")
    return redirect("article:dashboard") # article uygulaması altındaki dashboarda git

@login_required(login_url='user:login')
def detailarticle(request,id):
    #article = Article.objects.filter(id=id).first()
    article = get_object_or_404(Article,id=id)
    comments = article.comments.all()
    return render(request,"detailarticle.html",{"article":article,"comments":comments})