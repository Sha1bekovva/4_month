from django.shortcuts import render, get_object_or_404
from . import models
from .forms import FilmForm
from django.http import HttpResponse



def create_film_view(request):
    if request.method == 'POST':
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')  # или куда хотите перенаправить
    else:
        form = FilmForm()
    return render(request, 'films/create_film.html', {'form': form})


def film_list_view(request):
    if request.method == 'GET':
        film = models.Film.objects.all().order_by('-id')
        context = {
            'film': film,
        }
        return render(request,
                    template_name='films/films_list.html',
                    context=context
                    )
    
def film_detail_view(request, id):
    if request.method == 'GET':
        film_id = get_object_or_404(models.Film, id=id)
        context = {
            'film_id':film_id,
        }
        return render(request,
                    template_name='films/film_detail.html',
                    context=context)
