from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie


# Create your views here.


def index(request):
    movie = Movie.objects.all()
    return render(request, 'index.html', {'movie_list': movie})


def details(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'detail.html', {'movie': movie})


def add_details(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        details = request.POST.get('details')
        year = request.POST.get('year')
        img = request.FILES['img']

        movie = Movie(name=name, img=img, year=year, details=details)
        movie.save()

    return render(request, 'add.html')


def update(request, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request, 'update.html', {'movie': movie, 'form': form})

def delete(request, id):
    if request.method=='POST':
        movie=Movie.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')