from django.urls import path 
from . import views
urlpatterns = [
    path('Movies/',views.MoviesList.as_view(),name='movies'),
    path('Cast/',views.CastsList.as_view(),name='casts'),
    path("Genres/",views.GenreList.as_view(),name="genres"),
    path('Trailers/',views.TrailerList.as_view(),name="trailers"),
    path("Latest/",views.LatestList.as_view(),name="latest"),
    path("Upcoming/",views.UpcomingList.as_view(),name="upcoming"),
    path("Featured/",views.FeaturedList.as_view(),name="featured"),
    path("Top/",views.TopList.as_view(),name="top"),
    path("Suggested/",views.SuggestedList.as_view(),name="suggested"),
    path("Trending/",views.TrendingList.as_view(),name="trending"),
    path("Recommended/",views.RecommendedList.as_view(),name="recommended"),
    path("Popular/",views.PopularList.as_view(),name="popular"),
    path("Special/",views.SpecialList.as_view(),name="special"),
    path("Banner/",views.BannerList.as_view(),name="banner"),
    path("Sliders/",views.SlidersList.as_view(),name="sliders"),
    path("MoY/",views.MovieofTheYear.as_view(),name="moy"),
    path("MostPopular/",views.MostPopular.as_view(),name="mop"),
    path("PostMessage/",views.getMessage.as_view(),name="contact"),
    path("Details/<str:movieId>",views.getDetails.as_view(),name="details"),
    path("Trailer/<str:movieId>",views.getTrailer.as_view(),name="trailer"),
]
