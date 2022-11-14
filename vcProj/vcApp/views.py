from django.shortcuts import render, HttpResponse
import random
import string

# Create your views here.
users = {} # Keys = user_id, values = number of times visited

def index(request):
    if not request.COOKIES.get('user_id'):
        userName = "".join(random.choices(string.ascii_letters, k=10))
        users[userName] = 1
        data = {
            'user_id': userName,
            'num_vists' : users[userName]
        }
        response = render(request,'vcApp/index.html',data)
        response.set_cookie('user_id', userName, httponly=False, secure=False,max_age=5)
        response.set_cookie('num_visits', users[userName], httponly=False, secure=False,max_age=None)
        return response
        
        
        
    elif request.COOKIES.get('user_id'):
        userName = request.COOKIES.get('user_id')
        users[userName] += 1
        
        data = {
            'user_id': userName,
            'num_visits' : users[userName]
        }
          
        response = render(request,'vcApp/index.html',data)
        response.set_cookie('num_visits', users[userName], httponly=False, secure=False,max_age=None)
        return response
    