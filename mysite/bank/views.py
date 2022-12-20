from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from . import database_handler
from . import validator
import sqlite3

def index(request):
    return render(request, template_name="bank/index.html")


def register(request):
    return render(request, template_name="bank/register.html")

@csrf_exempt
def register_user(request):

    status = request.POST['status']
    username = request.POST['username']
    password1 = request.POST['password1']
    password2 = request.POST['password2']

    database_handler.register_user(username, password1, password2, status)
    

    return redirect("/")

def login(request):

    username = request.POST['username']
    password = request.POST['password']

    account = database_handler.get_account(username, password)
    
    if validator.validate_login(username, password, account):
        return redirect("/")

    else:
        return redirect("/register")

# Partial fix for Flaw 4: 
# @login_required 
def account_information(request):
    # Flaw 4. Broken Access Control
    # This flaw consits of no check that user who calls this method is actually a superuser.
    # Although there is no button to click to call this function currently it can still be hardwritten into the url: /account_information
    # Second Fix: Implement admin check before querying for accounts.
    # if request.user.is_superuser:
    # Only if this is true execute the code below.

    accounts = database_handler.get_all_accounts()
    return render(request, "bank/index.html", {"accounts":accounts})

# Flaw 5 Security Misconfiguration:
# Specifically: Default accounts and their passwords are still enabled and unchanged.
# Default test accounts with very simple passwords have not been removed. 