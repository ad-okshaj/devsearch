from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
    },
    {'id': '2',
        'title': 'Portfolio Website',
        'description': 'fully functional portfolio website', },
    {'id': '3',
     'title': 'Social Network Website',
     'description': 'Social network website project', },
]


def projects(request):
    page = 'projects'
    number = 11
    context = {'page': page, 'number': number, 'projects': projectsList}
    return render(request, 'projects/projects.html', context)


def project(request, pk):
    projectObj = None
    for i in projectsList:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})
