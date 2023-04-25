import json
import requests
import io
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from .froms import *
from .models import *


def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # checking if user with that username exist::
        try:
            user = User.objects.get(username=username)
            user = auth.authenticate(
                request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'username or password is incorrect')
        except:
            messages.error(request, 'User does not exist')

        # checking if user with that username has that password::

    context = {
        "page": "login"
    }
    return render(request, 'base/login_register.html', context)


def registerUser(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid:
            try:
                user = form.save(commit=False)
                user.username = user.username.lower()
                user.save()
                auth.login(request, user)
                return redirect('home')
            except:
                messages.error(request, 'Passwords dont match')
        else:
            messages.error(request, 'Error occured during registeration')
    form = RegisterForm()

    context = {
        "page": "register",
        'form': form
    }
    return render(request, 'base/login_register.html', context)


def logoutUser(request):
    auth.logout(request)
    return redirect('home')


def home(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        message = request.POST.get('message')
        Comment.objects.create(
            username=request.user,
            title=title,
            message=message
        )
        return redirect('home')
    form = CommentForm()
    comments = Comment.objects.all().order_by('-created')
    context = {
        'comments': comments,
        'form': form
    }
    return render(request, 'base/home.html', context)


def libraryhome(request):

    if request.method == 'POST':
        post = request.POST
        sem = post.get('semester')
        branch = post.get('branch')
        return redirect(f'books/{branch}/{sem}')
    form = SubjectForm()
    form.fields['semester'].queryset = Semester.objects.order_by('number')
    context = {
        'form': form,
    }
    return render(request, 'base/library-home.html', context)


def libraryOut(request, base, branch, sem):

    subjects = Subject.objects.all().filter(semester=sem, branch=branch)
    print(subjects)
    pyqs = Pyq.objects.filter(subject__in=subjects)

    print(pyqs)
    print(f"pyqs = {pyqs}")

    if (base == "books"):
        links = BookLink.objects.all()
        context = {
            'subjects': subjects,
            'branch': branch,
            'sem': sem,
            'links': links,
        }
        return render(request, 'base/library-books.html', context)
    elif (base == "pyqs"):
        context = {
            'pyqs': pyqs,
            'branch': branch,
            'sem': sem,
        }
        return render(request, 'base/library-pyqs.html', context)


def contact(request):
    context = {

    }
    return render(request, 'base/contact.html', context)


def courses(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    if request.GET.get('q') == None: 
        q = ''
    print(q)
    videos = Video.objects.filter(title__icontains=q)
    results = None if q == '' else len(videos)
    topics = Topic.objects.all()
    context = {
        'topics': topics,
        'videos': videos,
        'results': results,
    }
    return render(request, 'base/courses.html', context)


def createVideo(request):
    if request.method == 'POST':
        video_id = request.POST.get('id')
        api_key = "AIzaSyDjSwM29FKKygXoZky8Xa4p6H9GMsMx154"
        response = requests.get(
            f'https://www.googleapis.com/youtube/v3/videos?part=snippet&id={video_id}&key={api_key}')

        video_info = json.loads(response.text)
        try:
            thumbnail_url = video_info['items'][0]['snippet']['thumbnails']['high']['url']
            thumbnail = requests.get(thumbnail_url)
            image = io.BytesIO(thumbnail.content)

            title = video_info['items'][0]['snippet']['title']
            description = video_info['items'][0]['snippet']['description']
            url = f"https://www.youtube.com/watch?v={video_id}"

            video = Video(title=title, description=description[0:250], url=url)
            video.thumbnail.save(f"{video_id}.jpg", image)
            video.save()

        except Exception as e:
            print(e)

    return render(request, 'base/insert.html')
