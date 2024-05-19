from django.shortcuts import get_object_or_404, render
from app.models import Fruits

def fruit_detail(request,pk):
    fruit=get_object_or_404(Fruits,pk=pk)
    context={
        'fruit':fruit,
    }
    return render(request,'fruit_detail.html',context)


