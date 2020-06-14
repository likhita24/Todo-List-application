from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from .models import users, todoitems
from django.db import connection
from django.http import JsonResponse
from collections import namedtuple


def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

def signuppage(request):
     return render(request, "todopages/signup.html")
   
def signup(request):
    name = request.POST["username"]
    pwd = request.POST["password"]
    client = users(username = name, password = pwd)
    client.password = make_password(password = pwd, salt = None, hasher = 'unsalted_md5')
    client.save()
    return render(request, "todopages/signup.html")

def signinpage(request):
    return render(request, "todopages/signin.html")

def signin(request):
     if request.method == 'POST':
        username = request.POST['username']
        password =  make_password(password = request.POST['password'], salt = None, hasher = 'unsalted_md5')
        person = users.objects.filter(username = username, password = password)
        if person:
            request.session['username'] = username
            results = todoitems.objects.filter(user_id_id = person[0].id)
            return render(request, 'todopages/add.html', {"person" : person, "items" : results})
        else: 
            return render(request, 'todopages/signup.html', {})
def add(request):
    itemname = request.POST["taskname"]
    if request.session.has_key('username'):
        name = request.session['username']
        query = users.objects.filter(username = name) 
        saveitems = todoitems(Task_name = itemname, user_id_id = query[0].id)
        saveitems.save()
        results = todoitems.objects.filter(user_id_id = query[0].id)
    return render(request, 'todopages/add.html', { "items": results, "person" : 
                                                  query })

def remove(request):
    #id = request.GET["userid"]
    taskname = request.GET["taskname"]
    #sqlquery = "delete from todopages_todoitems where user_id_id={0} and Task_name='{1}'".format(id, taskname)
    #with connection.cursor() as cursor:
    #    cursor.execute(sqlquery)
    if request.session.has_key('username'):
        name = request.session['username']
        query = users.objects.filter(username = name) 
        todoitems.objects.filter(user_id_id = query[0].id, Task_name = taskname).delete()
        return JsonResponse({ 'is_success': True })
    #query = users.objects.filter(username = name) 
    #results = todoitems.objects.filter(user_id_id = query[0].id)
    #return render(request, 'todopages/add.html', {"items" : results})
        

def logout(request):
    try:
        del request.session['username']
    except:
     pass
    return render(request, 'todopages/signin.html', {})



    


# Create your views here.
