from django.shortcuts import render, redirect
from .models import Post, Contact, Comment
import requests
from django.core.paginator import Paginator


def home_view(request):
    posts = Post.objects.filter(is_published=True)
    d = {
        'posts': posts
    }
    return render(request, 'index.html', context=d)


def articles_view(request):
    data = request.GET
    cat = data.get("cat")
    page = data.get("page", 1)
    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
    else:
        posts = Post.objects.filter(is_published=True)
    paginator = Paginator(posts, 2)

    return render(request, 'blog.html', context={'posts': paginator.page(page)})


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == "POST":
        data = request.POST

        obj = Contact.objects.create(name=data.get('name'), email=data.get('email'),
                                     subject=data.get('subject'), message=data.get('message'))
        obj.save()
        token = '6617362077:AAEtf2XpYMWLVtAg3kiUNCFvNvcenHfQt9M'
        requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id=992767398&text=MOOSE\nID: {obj.id}\nName: {obj.name}\nEmail: {obj.email}\nMessage: {obj.message}')
        return redirect("/contact")
    return render(request, 'contact.html')


def blog_detail_view(request, pk):
    if request.method == "POST":
        data = request.POST
        obj = Comment.objects.create(post_id=pk, name=data['name'], email=data['email'], message=data['message'])
        obj.save()
        return redirect(f'/blog/{pk}')
    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post_id=pk)
    return render(request, 'blog-single.html', context={'post': post, 'comments': comments})
