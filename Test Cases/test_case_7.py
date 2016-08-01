# This test case should actively test all methods in
# and methods that can be called on the class Library from collection.py
import collection
import imdb_search

test_init = False
test_item_functions = False
test_iteration = True
test_string = False
test_collect = False
test_update = False
test_sort = True

# alphaMovie = imdb_search.Movie("The Nightmare Before Christmas")
# print(alphaMovie.alpha_title)
# print(imdb_search.Movie("The Shining").alpha_title, imdb_search.Movie("The Happening").alpha_title,
#       imdb_search.Movie("The Avengers").alpha_title,
#       imdb_search.Movie("The Curious Case of Benjamin Button").alpha_title,
#       imdb_search.Movie("The Incredibles").alpha_title, imdb_search.Movie("Avatar").alpha_title,
#       imdb_search.Movie("Elf").alpha_title, imdb_search.Movie("Inception").alpha_title, sep='\n')

if test_init:
    print("INIT TESTS")
    init_test = collection.Library([imdb_search.Movie("The Aviator"),
                                    imdb_search.Movie("The Nightmare Before Christmas")])
    print("Size:", len(init_test), '\n', "Objects:", init_test.objects)
    init_test2 = collection.Library()
    print("~~~~~~~~~~")

if test_item_functions:
    print("ITEM FUNCTIONS TESTS")
    item_test = collection.Library()
    print(item_test.__setitem__("The Aviator", imdb_search.Movie("The Aviator")))  # True
    print(item_test.__setitem__(9, imdb_search.Movie("9")))  # False, TypeError
    print("Size:", item_test.size, '\n', "Objects:", item_test.objects)  # Size: 1
    print("~~~~~~~~~~")
    print(item_test.__getitem__("The Aviator"))  # Returns properly
    print(item_test.__getitem__(9))  # False, TypeError
    print(item_test.__getitem__("The Nightmare Before Christmas"))  # False, KeyError
    print("~~~~~~~~~~")
    print(item_test.__setitem__("Edward Scissorhands", imdb_search.Movie("Edward Scissorhands")))  # True
    print(item_test.__delitem__("The Aviator"))  # True
    print("Size:", item_test.size, '\n', "Objects:", item_test.objects)  # Size: 1
    print(item_test.__delitem__(9))  # False, TypeError
    print(item_test.__delitem__("The Nightmare Before Christmas"))  # False, KeyError
    print("~~~~~~~~~~")

if test_iteration:
    print("ITERATION TEST")
    iter_test = collection.Library([imdb_search.Movie("The Aviator"), imdb_search.Movie("Edward Scissorhands"),
                                    imdb_search.Movie("The Nightmare Before Christmas")])
    # print(iter_test.objects)
    for i in iter(iter_test):
        print(i)
    print("~~~~~~~~~~")
    for i in iter_test.__iterkeys__():
        print(i)
    print("~~~~~~~~~~")

if test_string:
    print("STRING OUTPUT TEST")
    string_test = collection.Library([imdb_search.Movie("The Aviator"), imdb_search.Movie("Edward Scissorhands"),
                                      imdb_search.Movie("The Nightmare Before Christmas"), imdb_search.Movie("9")])
    print(string_test)
    print("~~~~~~~~~~")

if test_collect:
    print("COLLECT TEST")
    collect_test = collection.Library()
    Aviator = imdb_search.Movie("The Aviator")
    print(collect_test.collect(Aviator))  # True
    print(collect_test.objects["The Aviator"])
    print(collect_test[Aviator])
    print("~~~~~~~~~~")

if test_update:
    print("UPDATE TEST")
    NBC = imdb_search.Movie("The Nightmare Before Christmas")
    update_test = collection.Library([NBC])
    # update_test.update_item(NBC)  # Test passing item as object
    update_test.update_item("The Nightmare Before Christmas")  # Test passing item as string (as title of item)
    print("~~~~~~~~~~")

if test_sort:
    print("SORT TEST")
    sort_test = collection.Library([imdb_search.Movie("The Aviator"), imdb_search.Movie("Zoolander"),
                                    imdb_search.Movie("Men in Black"), imdb_search.Movie("Edward Scissorhands"),
                                    imdb_search.Movie("The Nightmare Before Christmas")])
    print(sort_test.sort_library())
