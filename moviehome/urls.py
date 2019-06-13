from django.urls import path
from . import views
urlpatterns = [
    path('', views.homepage),
    path('latest-movies/', views.latestmovie),
    path('bollywood-movies/', views.latesthindi),
    path('hollywood-movies/', views.latestenglish),
    path('dual_audio/', views.dualaudio),
    path('hd-movies/', views.hdmovies),
    path('details/<slug:movie_details_url>', views.details),
    path('series/', views.comingsoon),
    path('coming-soon/', views.coming_soon),
    path('vpn/', views.vpn),
    path('coming-soon/<slug:movie_details_url>', views.upcoming),
    path('search/', views.search),
    path('contact-us/', views.contact_us),
    path('thank-you/', views.thankyou)
]
