import imdb_search

# Standard tests taken from others
imdb_search.search_imdb("The Aviator")
imdb_search.search_imdb("Avatar 3")

# Following tests are attempting to force the "[x] not found" debug statements to print
print(imdb_search.misc_format(["PG-13", "runtime"], [], []))
print(imdb_search.misc_format([], ["2h 50min", "genre"], []))
print(imdb_search.misc_format([], [], ["Biography", "Horror", "rating"]))
