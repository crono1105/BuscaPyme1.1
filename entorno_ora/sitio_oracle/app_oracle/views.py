

from app_oracle.forms import registroPyme
from app_oracle.models import pyme
from django.shortcuts import redirect, render
from .forms import *

# Create your views here.
def index(request):
    return render(request,"app_oracle/index.html")

def contact(request):
    return render(request,"app_oracle/contact.html")

def about(request):
    return render(request,"app_oracle/about.html")   

def listing(request):
    return render(request,"app_oracle/listing.html")    

def listingdetails (request):
    return render(request,"app_oracle/listingdetails.html")  

def register(request):
    pyme = registroPyme(request.POST or None)
    context = {'formulario': pyme}
    if request.method=="POST":
        pyme.save()
        pyme.clean()
        return redirect(to='index')
        
    return render(request,"app_oracle/register.html",context)

def agendar(request):
    return render(request,"app_oracle/agendar.html")
