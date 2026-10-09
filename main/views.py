from django.shortcuts import render
from main.models import Skills,Progets
from django.views.generic import DetailView

def main(request):
    projects = Progets.objects.all()
    skills = Skills.objects.all()

    return render(
        request,
        'main/index.html',
        {'projects': projects, 'skills': skills},
    )

class Progect_Detail_View(DetailView):
    model = Progets
    template_name = 'main/progect_detail.html'
    context_object_name = 'progects_info'
