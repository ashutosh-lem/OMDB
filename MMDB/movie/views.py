from django.shortcuts import render
from movie.models import MovieDetail
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from movie.serializers import MovieDetailSerializer
# Create your views here.
class MovieView(APIView):
    def get(self,request,*args,**kwargs):
        title=kwargs.get('title')
        movieobj = MovieDetail.objects.filter(title__iexact=title).first()
        if not movieobj:
            response = requests.get(url=f"http://www.omdbapi.com/?t={title}&apikey=d18b305a")
            response_data=response.json()
            print(response,response_data)
            if response_data.get('Response')=="False":
                return Response (data=response_data.get("Error"))
            movieobj= MovieDetail.objects.create(title=response_data["Title"],year=response_data["Year"],rated=response_data["Rated"],
            released=response_data["Released"],imdbrating=response_data["imdbRating"])
        data=MovieDetailSerializer(movieobj)
        print(data.data)
        return Response(data=data.data,status=200)
