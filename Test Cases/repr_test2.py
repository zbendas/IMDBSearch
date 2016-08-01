from library import Library
from imdb_search import Movie

repr_movie = Movie("The Nightmare Before Christmas")
print(repr(repr_movie))
repr_test = Library([repr_movie])
print(repr_test, "AAAA")
#print(repr(repr_test))
#evaluated = eval(repr(repr_test))
#print(evaluated)