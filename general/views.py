from multiprocessing import context
from django.shortcuts import render

# Create your views here.

def homepage(request):
    context = {
        'title': 'Homepage'
    }
    return render(request, 'general/index.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'general/about.html', context)

def property_grid(request):
    context = {
        'title': 'Property'
    }
    return render(request, 'general/property-grid.html', context)

def property_single(request):
    context = {
        'title': 'Property-single'
    }
    return render(request, 'general/property-single.html', context)

def blog_grid(request):
    context = {
        'title': 'Blog-grid'
    }
    return render(request, 'general/blog-grid.html', context)

def blog_single(request):
    context = {
        'title': 'Blog-single'
    }
    return render(request, 'general/blog-single.html', context)

def pages(request):
    context = {
        'title': 'Pages'
    }
    return render(request, 'general/pages.html', context)

def contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'general/contact.html', context)

def agents_grid(request):
    context = {
        'title': 'Agents-grid'
    }
    return render(request, 'general/agents-grid.html', context)

def agent_single(request):
    context = {
        'title': 'Agent-single'
    }
    return render(request, 'general/agent-single.html', context)