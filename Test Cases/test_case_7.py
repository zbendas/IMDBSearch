# This test case should actively test all methods in
# and methods that can be called on the class Collection from collection.py
import collection
import imdb_search

init_test = collection.Collection([imdb_search.Movie("The Aviator")])
print("Size:", len(init_test), '\n', "Objects:", init_test.objects)
init_test2 = collection.Collection()
print("~~~~~~~~~~")
item_test = collection.Collection()
print(item_test.__setitem__("The Aviator", imdb_search.Movie("The Aviator")))
print(item_test.__setitem__(9, imdb_search.Movie("9")))
print("Size:", item_test.size, '\n', "Objects:", item_test.objects)
print("~~~~~~~~~~")
print(item_test.__getitem__("The Aviator"))
print(item_test.__getitem__(9))
print(item_test.__getitem__("The Nightmare Before Christmas"))
print("~~~~~~~~~~")
print(item_test.__delitem__("The Aviator"))
print("Size:", item_test.size, '\n', "Objects:", item_test.objects)
print(item_test.__delitem__(9))
print(item_test.__delitem__("The Nightmare Before Christmas"))
print("~~~~~~~~~~")
iter_test = collection.Collection()