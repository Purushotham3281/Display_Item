from django.shortcuts import render
from icecreame.models import Menu
# Create your views here.

def fun1(request):
    result=Menu.objects.all()
    
    context={"result":result}
    return render(request,"home.html",context)
    
