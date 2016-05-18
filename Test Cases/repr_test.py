from imdb_search import Movie

repr_test = Movie("The Nightmare Before Christmas")
print(repr(repr_test))
evaluated = eval(repr(repr_test))
print(evaluated.alpha_title)