from django.shortcuts import render
from app.models import Contact

# Create your views here.


def home(request):
    con = Contact.objects.all()
    context = {'contact':con}
    return render(request,'index.html',context)