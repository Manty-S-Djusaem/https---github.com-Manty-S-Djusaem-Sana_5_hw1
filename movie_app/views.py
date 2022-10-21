from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ReviewSerializer, DirectorSerializer, MovieSerializer
from .models import Director, Movie, Review
from rest_framework import status


@api_view(['GET'])
def directors_view(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)
    return Response(data=serializer.data)


@api_view(['GET'])
def director_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(status=404)
    serializer = DirectorSerializer(director)
    return Response(data=serializer.data)

@api_view(['GET'])
def movies_view(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=not False)
    return Response(data=serializer.data)

@api_view(['GET'])
def movie_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'movie: not found'})
    serializer = MovieSerializer(movie)
    return Response(data=serializer.data)

@api_view(['GET'])
def reviews_view(request):
    reviews = Review.objects.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(data=serializer.data)

@api_view(['GET'])
def review_view(request, id):
    review = Review.objects.get(id=id)
    serializer = ReviewSerializer(review)
    return Response(data=serializer.data)