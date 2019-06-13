from django.contrib import admin
from .models import MovieDetails, UpcomingDetails, UserInfo


class MovieListAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'movie_audio', 'movie_quality', 'movie_type', 'movie_released', 'movie_release_date')


class UpcomingDetailsAdmin(admin.ModelAdmin):
    list_display = ('movie_name', 'movie_released', 'movie_release_date', 'movie_type')


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'user_email')


admin.site.register(MovieDetails, MovieListAdmin)
admin.site.register(UpcomingDetails, UpcomingDetailsAdmin)
admin.site.register(UserInfo, UserInfoAdmin)
