from django.http import HttpResponse
from django.shortcuts import render

from . models import Movie


# Create your views here.
def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list':movie
    }
    return render(request, 'index.html', context )

def detail(request,movie_id):
    return HttpResponse("THIS IS MOVIE NUMBER %s" % movie_id)