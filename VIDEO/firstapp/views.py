
from django.shortcuts import render,redirect
from .models import data

def Home(request):
    return render(request,"index.html")
def about(request):
    datas = data.objects.all()
    context = {
        'datas': datas
    }
    return render(request,"about.html",context)
def contact(request):
    return render(request,"contact.html")
def upload(request):
    if(request.method == "POST"):
        title = request.POST["title"]
        video = request.FILES["video"]
        datas = data(title=title,video=video)
        datas.save()
        return redirect("about")
    

    
    return render(request,"upload.html")