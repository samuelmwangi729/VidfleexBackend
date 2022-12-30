from django.urls import path 
from . import views
urlpatterns = [
    path('',views.MoviesList.as_view(),name='movies'),
    path('Cast/',views.CastsList.as_view(),name='casts'),
    path("Genres/",views.GenreList.as_view(),name="genres"),
    path('Trailers',views.TrailerList.as_view(),name="trailers")
]
