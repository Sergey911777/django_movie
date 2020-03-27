from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib.auth import views, login

from django_movie import settings
from . import views
from .views import RegisterView, ProfileView, LogoutView, EditProfileView

urlpatterns = [
    path("", views.MoviesView.as_view(), name='index'),
    path("filter/", views.FilterMoviesView.as_view(), name='filter'),
    path("add-rating/", views.AddStarRating.as_view(), name='add_rating'),
    path("search/", views.SearchMoviesView.as_view(), name='search'),
    path("<slug:slug>/", views.MovieDetailView.as_view(), name="movie_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name="add_review"),
    path("actor/<str:slug>/", views.ActorView.as_view(), name="actor_detail"),
    path('accounts/', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', login, name="login"),
    url(r'^accounts/logout/$', LogoutView.as_view(), name="logout"),
    url(r'^accounts/register/$', RegisterView.as_view(), name="register"),
    url(r'^accounts/profile/$', ProfileView.as_view(), name="profile"),
    url(r'^accounts/profile/edit/$', EditProfileView.as_view(), name="edit_profile"),
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS) +\
              static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)