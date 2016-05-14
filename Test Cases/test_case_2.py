# Support for the "print_[x]" functions now deprecated
import imdb_search

imdb_search.search("The Aviator")
imdb_search.search("Mommie Dearest", print_reviews=False)
imdb_search.search("Avatar 3", print_summary=False)
