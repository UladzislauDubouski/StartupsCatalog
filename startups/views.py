from django.shortcuts import render

# Create your views here.

from startups.models import Startup


def startup_index(request):
    startups = Startup.objects.all()
    context = {
        'startups': startups
    }
    return render(request, 'startup_index.html', context)


def startup_detail(request, pk):
    startup = Startup.objects.get(pk=pk)
    context = {
        'startup': startup
    }
    return render(request, 'startup_detail.html', context)