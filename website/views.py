from django.shortcuts import render, redirect
from . import forms, models
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

def login_auth(fn):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return fn(request)
        else:
            return redirect('home')
    return wrapper

def home(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        # authenticate user and login if so
        user = authenticate(request, username=username, password=password)  # using imported function to check if username and password are valid
        if user is not None:
            login(request, user)  # this is the function we imported above
            messages.success(request, "Successful Login")
            return redirect('home')
        else:
            messages.success(request, "Invalid username or password. Please try again.")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

@login_auth
def table(request):
    all_data = models.ModelCRM.objects.all()
    return render(request, 'table.html', {'all_data': all_data})

@login_auth
def update(request, item_id):
    item = models.ModelCRM.objects.get(pk=item_id)
    return render(request, 'update.html', {"item": item})

@login_auth
def updateinfo(request, item_id):
    if request.method == "POST":
        item = models.ModelCRM.objects.get(pk=item_id)
        item.first_name = request.POST["first_name"]  # saving the items parameter 'first_name' with new value typed in from html and webpage
        item.last_name = request.POST["last_name"]
        item.email = request.POST["email"]
        item.address = request.POST["address"]
        item.city = request.POST["city"]
        item.province = request.POST["province"]
        item.postal_code = request.POST["postal_code"]
        item.save()  # saves to database
        messages.success(request,('Customer records successfully updated'))  # this message gets listed on the admin page inside the new database
        return redirect('table')
    else:
        item = models.ModelCRM.objects.get(pk=item_id)
        if request.user.is_authenticated:
            return render(request, 'updateinfo.html', {"item": item})

@login_auth
def addcustomer(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        address = request.POST["address"]
        city = request.POST["city"]
        province = request.POST["province"]
        postal_code = request.POST["postal_code"]
        model = models.ModelCRM(first_name=first_name, last_name=last_name, email=email,
                                address=address, city=city, province=province, postal_code=postal_code)  # sets 'form' equal to what was typed in to input on webpage
        model.save()  # saves to database
        messages.success(request,('Customer has been added successfully'))  # this message gets listed on the admin page inside the new database
        # return render(request, 'table.html', {})
        return redirect('table')
    else:
        return render(request, 'addcustomer.html', {})
  
@login_auth
def deletecustomer(request, item_id):
    item = models.ModelCRM.objects.get(pk=item_id)
    item.delete()
    messages.success(request, "Customer removed")
    return redirect('table')

def logout_user(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('home')
