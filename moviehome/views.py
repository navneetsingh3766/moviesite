from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import MovieDetails, UpcomingDetails, UserInfo


def homepage(request):
    revers = MovieDetails.objects.all().order_by('-movie_release_date')
    movieshindi = revers.filter(movie_type_hindi=True)
    moviesenglish = revers.filter(movie_type_english=True)
    dualaudios = revers.filter(movie_audio_dual=True)
    hdmovies = revers.filter(movie_quality_hd=True)
    context = {
        'latestMovies': revers,
        'moviesHindi': movieshindi,
        'moviesEnglish': moviesenglish,
        'dualAudio': dualaudios,
        'hdMovies': hdmovies
    }
    return render(request, 'homepage.html', context)


def latestmovie(request):
    data = MovieDetails.objects.all().order_by('-movie_release_date')
    paginator = Paginator(data, 30)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    context = {
        'movies': movies,
        'page_title': 'Latest movies'
    }
    return render(request, 'seeAll.html', context)


def latesthindi(request):
    data = MovieDetails.objects.all().order_by('-movie_release_date')
    data = data.filter(movie_type_hindi=True)
    paginator = Paginator(data, 30)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    context = {
        'movies': movies,
        'page_title': 'bollywood movies'
    }
    return render(request, 'seeAll.html', context)


def latestenglish(request):
    data = MovieDetails.objects.all().order_by('-movie_release_date')
    data = data.filter(movie_type_english=True)
    paginator = Paginator(data, 30)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    context = {
        'movies': movies,
        'page_title': 'hollywood movies'
    }
    return render(request, 'seeAll.html', context)


def dualaudio(request):
    data = MovieDetails.objects.all().order_by('-movie_release_date')
    data = data.filter(movie_audio_dual=True)
    paginator = Paginator(data, 30)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    context = {
        'movies': movies,
        'page_title': 'hollywood movies'
    }
    return render(request, 'seeAll.html', context)


def hdmovies(request):
    data = MovieDetails.objects.all().order_by('-movie_release_date')
    data = data.filter(movie_quality_hd=True)
    paginator = Paginator(data, 30)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    context = {
        'movies': movies,
        'page_title': 'hd movies'
    }
    return render(request, 'seeAll.html', context)


def details(request, movie_details_url):
    movie_details = MovieDetails.objects.get(movie_details_page=movie_details_url)
    context = {
        'object': movie_details
    }
    return render(request, 'details.html', context)


def upcoming(request, movie_details_url):
    movie_coming = UpcomingDetails.objects.get(movie_details_page=movie_details_url)
    context = {
        'object': movie_coming
    }
    return render(request, 'details.html', context)


def comingsoon(request):
    return render(request, 'comingsoon.html', {})


def vpn(request):
    return render(request, 'vpn.html', {})


def search(request):
    data = MovieDetails.objects.all().order_by('-movie_release_date')
    coming_movie_data = UpcomingDetails.objects.all().order_by('movie_release_date')
    query = request.GET.get("q")
    if query:
        if data.filter(movie_name__icontains=query).count() is not 0:
            revers = data.filter(movie_name__icontains=query)
            paginator = Paginator(revers, 30)
            page = request.GET.get('page')
            movies = paginator.get_page(page)
            return render(request, 'seeAll.html', {'movies': movies})
        elif coming_movie_data.filter(movie_name__icontains=query).count() is not 0:
            revers = coming_movie_data.filter(movie_name__icontains=query)
            paginator = Paginator(revers, 30)
            page = request.GET.get('page')
            movies = paginator.get_page(page)
            return render(request, 'coming-soon.html', {'movies': movies})
        else:
            revers = 'check your spelling or go to'
            home_link = 'home page'
            return render(request, 'seeAll.html', {'page_title': revers, 'home_link': home_link})
    else:
        revers = 'check your spelling or go to'
        home_link = 'home page'
        return render(request, 'seeAll.html', {'page_title': revers, 'home_link': home_link})


def coming_soon(request):
    data = UpcomingDetails.objects.all().order_by('movie_release_date')
    data = data.filter(movie_released=False)
    paginator = Paginator(data, 30)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    context = {
        'movies': movies,
        'page_title': 'UpComing Movies'
    }
    return render(request, 'coming-soon.html', context)


def contact_us(request):
    return render(request, 'contact-us.html', {})


def thankyou(request):
    user_name = request.POST["name"]
    user_email = request.POST["email"]
    user_comment = request.POST["comment"]
    if user_name != '' and user_email != '' :
        user_info = UserInfo(user_name=user_name, user_email=user_email, user_comment=user_comment)
        user_info.save()
        return render(request, 'thankyou.html', {})
    else:
        return redirect('/contact-us/')
