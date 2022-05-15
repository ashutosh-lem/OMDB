from rest_framework import serializers
from movie.models import MovieDetail

class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDetail
        fields='__all__'
        