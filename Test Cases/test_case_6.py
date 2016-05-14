# Test whether or not imdb_search.Movie.__repr__ properly supplies an exact string representation of itself
from imdb_search import Movie

Aviator = Movie("The Aviator")
Aviator2 = eval(repr(Aviator))
print(Aviator2)  # Succeeds
