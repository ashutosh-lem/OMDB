from movie.views import MovieView
from django.urls import path,include

urlpatterns = [
    path('<slug:title>/', MovieView.as_view())
]