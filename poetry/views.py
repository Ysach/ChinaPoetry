# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# import json
import models
import user_des
from django.db.models import Q
from django.contrib.auth import authenticate, logout, login


# Create your views here.
def page_not_found(request):
    # response = render_to_response('404.html', context=RequestContext(request))
    # response.status_code = 404
    # return response
    return render(request, 'error/404.html', status=404)


def user_login(request):
    next_url = request.GET.get('next', '/')
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        url = request.POST.get('next', '/')
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(url)
    context = {
        'next': next_url
    }
    return render(request, "login/login.html", context, status=200)


def index(request):
    if request.method == "GET":
        poetry_obj = models.Poetry.objects.all().order_by('id')[0:20]
        context = {
            'poetry': poetry_obj,
            'home': True
        }
        return render(request, 'poetry_index.html', context)
    if request.method == "POST":
        pages = int(request.POST.get('pages'))
        poetry_obj = models.Poetry.objects.all().order_by('id')[pages:(pages + 10)]
        context = {
            'poetry': poetry_obj,
            'home': True
        }
        print "--------------",pages
        return render(request, 'mobile_template/poetry_index_append.html', context, status=200)


def poetry_content(request, poetry_id):
    if request.method == "GET":
        try:
            _love_ = False
            poetry_id = user_des.user_encrypt(poetry_id)
            cur_poetry = models.Poetry.objects.get(id=poetry_id)
            _love = cur_poetry.love_set.filter(poetry_id_id=poetry_id, user_id_id=request.user.id)
            if len(_love) > 0:
                _love_ = True
            context = {
                'cur_poetry': cur_poetry,
                'content': True,
                'content_love': _love_
            }
        except Exception as e:
            print str(e)
            context = {
                'error': str(e)
            }
            return render(request, 'error/500.html', context, status=500)
        else:
            return render(request, 'poetry_content.html', context, status=200)


def search_home(request):
    # author = models.Author.objects.all()[40:60]
    author = models.HostSearch.objects.all()[0:20]
    poetry_type = models.PoetryType.objects.all()[0:20]
    dynasty = models.Poetry.objects.values('dynasty').distinct()
    context = {
        'search': True,
        'author': author,
        'poetry_type': poetry_type,
        'dynasty': dynasty
    }
    return render(request, 'poetry_search.html', context, status=200)


def search(request):
    author = request.GET.get('author', '')
    dynasty = request.GET.get('dynasty', '')
    poetry_type = request.GET.get('type', '')
    content = request.GET.get('content', '')
    if request.method == 'GET':
        if author:
            try:
                author_obj = models.Author.objects.get(name=author).poetry_set.all()[0:20]
            except Exception as e:
                print str(e)
                context = {
                    'error': str(e)
                }
                return render(request, 'error/500.html', context, status=500)
            else:
                context = {
                    'search_obj': author_obj,
                    'search_content': True
                }
                return render(request, 'poetry_search_content.html', context, status=200)

        elif dynasty:
            try:
                dynasty_obj = models.Poetry.objects.filter(dynasty=dynasty)[0:20]
            except Exception as e:
                print str(e)
                context = {
                    'error': str(e)
                }
                return render(request, 'error/500.html', context, status=500)
            else:
                context = {
                    'search_obj': dynasty_obj,
                    'search_content': True
                }
                return render(request, 'poetry_search_content.html', context, status=200)

        elif poetry_type:
            try:
                poetry_obj = models.Poetry.objects.filter(tags__contains=poetry_type)[0:20]
            except Exception as e:
                print str(e)
                context = {
                    'error': str(e)
                }
                return render(request, 'error/500.html', context, status=500)
            else:
                context = {
                    'search_obj': poetry_obj,
                    'search_content': True
                }
                return render(request, 'poetry_search_content.html', context, status=200)

        elif content:
            try:
                content_obj = models.Poetry.objects.filter(
                    Q(name__contains=content) |
                    Q(dynasty__contains=content) |
                    Q(content__contains=content) |
                    Q(tags__contains=content) |
                    Q(author_id__name__contains=content)
                )[0:20]
            except Exception as e:
                print str(e)
                context = {
                    'error': str(e)
                }
                return render(request, 'error/500.html', context, status=500)
            else:
                context = {
                    'search_obj': content_obj,
                    'search_content': True
                }
                return render(request, 'poetry_search_content.html', context, status=200)
        else:
            context = {
                'search_content': True
            }
            return render(request, 'error/404.html', context, status=200)

    if request.method == 'POST':
        # author = request.POST.get('author', '')
        # dynasty = request.POST.get('dynasty', '')
        # poetry_type = request.POST.get('type', '')
        # content = request.POST.get('content', '')
        # print "当前的-----》", content
        print author
        pages = int(request.POST.get('pages', 0))
        print "search", pages
        if author:
            try:
                author_obj = models.Author.objects.get(name=author).poetry_set.all()[pages:(pages + 20)]
            except Exception as e:
                print str(e)
                context = {
                    'error': str(e)
                }
                return render(request, 'error/500.html', context, status=500)
            else:
                context = {
                    'search_obj': author_obj,
                    'search_content': True
                }
                return render(request, 'mobile_template/poetry_search_append.html', context, status=200)

        if dynasty:
            try:
                dynasty_obj = models.Poetry.objects.filter(dynasty=dynasty)[pages:(pages + 20)]
            except Exception as e:
                print str(e)
                context = {
                    'error': str(e)
                }
                return render(request, 'error/500.html', context, status=500)
            else:
                context = {
                    'search_obj': dynasty_obj,
                    'search_content': True
                }
                return render(request, 'mobile_template/poetry_search_append.html', context, status=200)

        if poetry_type:
            try:
                poetry_obj = models.Poetry.objects.filter(tags__contains=poetry_type)[pages:(pages + 20)]
            except Exception as e:
                print str(e)
                context = {
                    'error': str(e)
                }
                return render(request, 'error/500.html', context, status=500)
            else:
                context = {
                    'search_obj': poetry_obj,
                    'search_content': True
                }
                return render(request, 'mobile_template/poetry_search_append.html', context, status=200)

        if content:
            try:
                content_obj = models.Poetry.objects.filter(
                    Q(name__contains=content) |
                    Q(dynasty__contains=content) |
                    Q(content__contains=content) |
                    # Q(tags__contains=content) |
                    Q(author_id__name__contains=content)
                )[pages:(pages + 20)]
            except Exception as e:
                print str(e)
                context = {
                    'error': str(e)
                }
                return render(request, 'error/500.html', context, status=500)
            else:
                context = {
                    'search_obj': content_obj,
                    'search_content': True
                }
                return render(request, 'mobile_template/poetry_search_append.html', context, status=200)


def love(request):
    if request.method == 'GET':
        poetry_obj = models.Love.objects.filter(user_id_id=request.user.id).all()
        context = {
            'love': True,
            'poetry': poetry_obj
        }
        return render(request, 'poetry_love.html', context, status=200)
    if request.method == 'POST':
        poetry_id = request.POST.get('poetry_id', '')
        try:
            size, created = models.Love.objects.get_or_create(poetry_id_id=poetry_id, user_id_id=request.user.id)
            if not created:
                size.delete()
                return HttpResponse('del')
        except Exception as e:
            print str(e)
            context = {
                'error': str(e)
            }
            return render(request, 'error/500.html', context, status=500)
        else:
            return HttpResponse('success')
    return render(request, 'error/400.html', status=404)


def mine(request):
    context = {
        'mine': True
    }

    return render(request, 'poetry_mine.html', context, status=200)
