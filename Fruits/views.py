from django.shortcuts import render
from app.models import Fruits
def home(request):
    fruit=Fruits.objects.all()
    context={
        'fruit':fruit,
    }
    return render(request,'home.html',context)