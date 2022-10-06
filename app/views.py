"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def loginView(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/login.html',
        {
            'title':'Log in',
            'year':datetime.now().year,
        }
    )

def globalchatlanding(request):
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return redirect("login")
    return render(
        request,
        'app/globalchatlanding.html',
        {
            'title':'Global Chat',
            'message':'Chat globally with people!',
            'year':datetime.now().year,
        }
    )

def globalchat(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    if not request.user.is_authenticated:
        return redirect("login")
    return render(
        request,
        'app/globalchat.html',
        {
            'title':'Global Chat',
            'message':'Chat globally with people!',
            'year':datetime.now().year,
        }
    )

def oneonone(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/oneonone.html',
        {
            'title':'1:1 Chat',
            'message':'Chat one-on-one with your friends!',
            'year':datetime.now().year,
        }
    )
