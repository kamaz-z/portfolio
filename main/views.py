from django.shortcuts import render
from main.models import Skills,Progets

def main(request):
    projects = Progets.objects.all()
    return render(request,'main/index.html',{'projects':projects})
