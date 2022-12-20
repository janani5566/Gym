from django.shortcuts import render

from GymApp.models import Register
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def registerPage(request):


    if request.method == "POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        goal = request.POST.get('goal')
        gender = request.POST.get('gender')

        en = Register(name=name, age=age, address=address, phone=phone, goal=goal, gender=gender)
        en.save()
        if en.is_valid():
            en.save()
            messages.success(request, 'thank you')


    return render(request, 'core/register.html')
def saveEnquiry(request):
    if request.method=="POST":
        name = request.POST.get('name')
        age = request.POST.get('age')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        goal = request.POST.get('goal')
        gender = request.POST.get('gender')

        ins = Register(name=name, age=age, address=address, phone=phone, goal=goal, gender=gender)
        ins.save()

    return render(request, 'core/register.html')
