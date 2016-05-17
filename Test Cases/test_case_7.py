# This test case should actively test all methods in
# and methods that can be called on the class Collection from collection.py
import collection
import imdb_search

test_init = False
test_item_functions = False
test_iteration = False
test_string = False
test_collect = False
test_update = False
test_sort = True

if test_init:
    print("INIT TESTS")
    init_test = collection.Collection([imdb_search.Movie("The Aviator"),
                                       imdb_search.Movie("The Nightmare Before Christmas")])
    print("Size:", len(init_test), '\n', "Objects:", init_test.objects)
    init_test2 = collection.Collection()
    print("~~~~~~~~~~")

if test_item_functions:
    print("ITEM FUNCTIONS TESTS")
    item_test = collection.Collection()
    print(item_test.__setitem__("The Aviator", imdb_search.Movie("The Aviator")))
    print(item_test.__setitem__(9, imdb_search.Movie("9")))
    print("Size:", item_test.size, '\n', "Objects:", item_test.objects)
    print("~~~~~~~~~~")
    print(item_test.__getitem__("The Aviator"))
    print(item_test.__getitem__(9))
    print(item_test.__getitem__("The Nightmare Before Christmas"))
    print("~~~~~~~~~~")
    print(item_test.__setitem__("Edward Scissorhands", imdb_search.Movie("Edward Scissorhands")))
    print(item_test.__delitem__("The Aviator"))
    print("Size:", item_test.size, '\n', "Objects:", item_test.objects)
    print(item_test.__delitem__(9))
    print(item_test.__delitem__("The Nightmare Before Christmas"))
    print("~~~~~~~~~~")

if test_iteration:
    print("ITERATION TEST")
    iter_test = collection.Collection([imdb_search.Movie("The Aviator"), imdb_search.Movie("Edward Scissorhands"),
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
    string_test = collection.Collection([imdb_search.Movie("The Aviator"), imdb_search.Movie("Edward Scissorhands"),
                                         imdb_search.Movie("The Nightmare Before Christmas"), imdb_search.Movie("9")])
    print(string_test)
    print("~~~~~~~~~~")

if test_collect:
    print("COLLECT TEST")
    collect_test = collection.Collection()
    Aviator = imdb_search.Movie("The Aviator")
    print(collect_test.collect(Aviator))
    print(collect_test.objects["The Aviator"])
    print(collect_test[Aviator])
    print("~~~~~~~~~~")

if test_update:
    print("UPDATE TEST")
    NBC = imdb_search.Movie("The Nightmare Before Christmas")
    update_test = collection.Collection([NBC])
    # update_test.update_item(NBC)  # Test passing item as object
    update_test.update_item("The Nightmare Before Christmas")  # Test passing item as string (as title of item)
    print("~~~~~~~~~~")

if test_sort:
    print("SORT TEST")
    sort_test = collection.Collection([imdb_search.Movie("The Aviator"), imdb_search.Movie("Edward Scissorhands"),
                                       imdb_search.Movie("The Nightmare Before Christmas")])
    sort_test.sort_collection()
