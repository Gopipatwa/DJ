from django.shortcuts import render
from app.models import Contact

# Create your views here.

# git remote add origin https://github.com/Gopipatwa/DJ.git
# git branch -M main
# git push -u origin main
# https://careerkarma.com/blog/git-permission-denied-publickey/:~:text=The%20%E2%80%9CPermission%20denied%20(publickey).%20fatal:%20Could%20not%20read,it%20is%20not,%20add%20your%20key%20to%20Git.



def home(request):
    con = Contact.objects.all()
    context = {'contact':con}
    return render(request,'index.html',context)