from django.db import models


class MovieDetails(models.Model):
    movie_name = models.CharField(max_length=255)
    movie_details_page = models.CharField(max_length=255, blank=True, default='')
    movie_released = models.BooleanField(default=False)
    movie_release_date = models.IntegerField(blank=True, null=True)
    movie_year = models.IntegerField(blank=True, null=True)
    movie_month = models.IntegerField(blank=True, null=True)
    movie_date = models.IntegerField(blank=True, null=True)
    movie_audio = models.TextField(max_length=20, blank=True, default='')
    movie_audio_hindi = models.BooleanField(default=False)
    movie_audio_english = models.BooleanField(default=False)
    movie_audio_dual = models.BooleanField(default=False)
    movie_image_url = models.CharField(max_length=2083, blank=True, default='')
    movie_quality = models.CharField(max_length=100, blank=True, default='')
    movie_quality_hd = models.BooleanField(default=False)
    movie_quality_sd = models.BooleanField(default=False)
    movie_quality_cam = models.BooleanField(default=False)
    movie_stars_in_movie = models.CharField(max_length=100, blank=True, default='')
    movie_type = models.CharField(max_length=20, blank=True, default='')
    movie_type_hindi = models.BooleanField(default=False)
    movie_type_english = models.BooleanField(default=False)
    movie_director = models.CharField(max_length=50, blank=True, default='')
    movie_story_long = models.TextField(max_length=900000, blank=True, default='')
    movie_story_short = models.TextField(max_length=5000, blank=True, default='')
    movie_review = models.TextField(max_length=4000, blank=True, default='')
    movie_rating = models.FloatField(blank=True, null=True)
    movie_trailer = models.CharField(max_length=2083, blank=True, default='')
    movie_trailer2 = models.CharField(max_length=2083, blank=True, default='')
    movie_trailer_review = models.TextField(max_length=3000, blank=True, default='')
    movie_download_link1_website = models.TextField(max_length=100, blank=True, default='')
    movie_download_link1 = models.CharField(max_length=2083, blank=True, default='')
    movie_download_link1_adds = models.TextField(max_length=100 ,blank=True, default='')
    movie_download_link2_website = models.TextField(max_length=100, blank=True, default='')
    movie_download_link2 = models.CharField(max_length=2083, blank=True, default='')
    movie_download_link2_adds = models.TextField(max_length=100, blank=True, default='')
    movie_download_link3_website = models.TextField(max_length=100, blank=True, default='')
    movie_download_link3 = models.CharField(max_length=2083, blank=True, default='')
    movie_download_link3_adds = models.TextField(max_length=100, blank=True, default='')
    movie_download_link4_website = models.TextField(max_length=100, blank=True, default='')
    movie_download_link4 = models.CharField(max_length=2083, blank=True, default='')
    movie_download_link4_adds = models.TextField(max_length=100, blank=True, default='')
    movie_download_link5_website = models.TextField(max_length=100, blank=True, default='')
    movie_download_link5 = models.CharField(max_length=2083, blank=True, default='')
    movie_download_link5_adds = models.TextField(max_length=100, blank=True, default='')
    movie_download_link6_website = models.TextField(max_length=100, blank=True, default='')
    movie_download_link6 = models.CharField(max_length=2083, blank=True, default='')
    movie_download_link6_adds = models.TextField(max_length=100, blank=True, default='')
    movie_download_link7_website = models.TextField(max_length=100, blank=True, default='')
    movie_download_link7 = models.CharField(max_length=2083, blank=True, default='')
    movie_download_link7_adds = models.TextField(max_length=100, blank=True, default='')
    movie_download_link8_website = models.TextField(max_length=100, blank=True, default='')
    movie_download_link8 = models.CharField(max_length=2083, blank=True, default='')
    movie_download_link8_adds = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link1_website = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link1 = models.CharField(max_length=2083, blank=True, default='')
    # movie_download_link1_adds = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link2_website = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link2 = models.CharField(max_length=2083, blank=True, default='')
    # movie_download_link2_adds = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link3_website = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link3 = models.CharField(max_length=2083, blank=True, default='')
    # movie_download_link3_adds = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link4_website = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link4 = models.CharField(max_length=2083, blank=True, default='')
    # movie_download_link4_adds = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link5_website = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link5 = models.CharField(max_length=2083, blank=True, default='')
    # movie_download_link5_adds = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link6_website = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link6 = models.CharField(max_length=2083, blank=True, default='')
    # movie_download_link6_adds = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link7_website = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link7 = models.CharField(max_length=2083, blank=True, default='')
    # movie_download_link7_adds = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link8_website = models.TextField(max_length=100, blank=True, default='')
    movie_stream_link8 = models.CharField(max_length=2083, blank=True, default='')
    # movie_download_link8_adds = models.TextField(max_length=100, blank=True, default='')


class UpcomingDetails(models.Model):
    movie_name = models.CharField(max_length=255)
    movie_details_page = models.CharField(max_length=255, blank=True, default='')
    movie_released = models.BooleanField(default=False)
    movie_release_date = models.IntegerField(blank=True, null=True)
    movie_year = models.IntegerField(blank=True, null=True)
    movie_month = models.IntegerField(blank=True, null=True)
    movie_date = models.IntegerField(blank=True, null=True)
    movie_audio = models.TextField(max_length=100, blank=True, default='')
    movie_audio_hindi = models.BooleanField(default=False)
    movie_audio_english = models.BooleanField(default=False)
    movie_audio_dual = models.BooleanField(default=False)
    movie_image_url = models.CharField(max_length=2083, blank=True, default='')
    movie_quality = models.CharField(max_length=100, blank=True, default='')
    movie_quality_hd = models.BooleanField(default=False)
    movie_quality_sd = models.BooleanField(default=False)
    movie_quality_cam = models.BooleanField(default=False)
    movie_stars_in_movie = models.CharField(max_length=100, blank=True, default='')
    movie_type = models.CharField(max_length=20, blank=True, default='')
    movie_type_hindi = models.BooleanField(default=False)
    movie_type_english = models.BooleanField(default=False)
    movie_director = models.CharField(max_length=50, blank=True, default='')
    movie_story_long = models.TextField(max_length=900000, blank=True, default='')
    movie_story_short = models.TextField(max_length=5000, blank=True, default='')
    movie_review = models.TextField(max_length=4000, blank=True, default='')
    movie_rating = models.FloatField(blank=True, null=True)
    movie_trailer = models.CharField(max_length=2083, blank=True, default='')
    movie_trailer2 = models.CharField(max_length=2083, blank=True, default='')


class UserInfo(models.Model):
    user_name = models.TextField(max_length=30)
    user_email = models.CharField(max_length=30)
    user_comment = models.TextField(max_length=200)
