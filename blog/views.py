from django.core.paginator import Paginator
from django.shortcuts import render, redirect
import requests
from blog.models import Post, Contact, Comment


def home_view(request):
    posts = Post.objects.filter(is_published=True)

    context = {
        'posts': posts,
        'home': 'active',
    }

    return render(request, 'index.html', context)


def blog_view(request):
    data = request.GET
    cat = data.get('cat')
    page = data.get('page', 1)
    if cat:
        posts = Post.objects.filter(is_published=True, category_id=cat)
    else:
        posts = Post.objects.filter(is_published=True)

    page_obj = Paginator(posts, 1)
    context = {
        'posts': page_obj.page(page),
        'blog': 'active',
    }
    return render(request, 'blog.html', context)


def blog_detail_view(request, pk):
    if request.method == 'POST':
        data = request.POST
        obj = Comment.objects.create(post_id=pk, name=data['name'], email=data['email'], message=data['message'])
        obj.save()
        return redirect(f'/blog/{pk}')
    post = Post.objects.filter(id=pk).first()
    comments = Comment.objects.filter(post_id=pk)

    return render(request, 'blog-single.html', {'post': post, 'comments': comments})


def about_view(request):
    context = {
        'about': 'active'
    }
    return render(request, 'about.html')


def contact_view(request):
    if request.method == 'POST':
        data = request.POST

        obj = Contact.objects.create(name=data['name'], subject=data['subject'], email=data['email'],
                                     message=data['message'])
        obj.save()
        token = '6617362077:AAEtf2XpYMWLVtAg3kiUNCFvNvcenHfQt9M'
        requests.get(f"""http://api.telegram.org/bot{token}sendMessage
        ?chat_id=992767398&text=MOOSE\nid: {obj.id}\nname: {obj.name}\nemail: {obj.email}\nmessage: {obj.message}""")
        return redirect('/contact')

    context = {
        'contact': 'active',
    }
    return render(request, 'contact.html', context)