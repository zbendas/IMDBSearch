# This will eventually be a program that creates collections of the imdb_search.Movie objects
# and logs information about the collection into a file that can be read/written.


class Collection:
    """Base class for all collections"""

    # This class may need an update function associated with it, to be called to pull new information on each object.
    # Also, it may be important to catalog what TYPE of item is being added to the collection, e.g. movie
    # But this may be easier to accomplish with classes that inherit from this one

    def __init__(self, objects=None):
        if objects is None:
            # This branch allows a blank collection to be created.
            self.objects = {}
            self.size = 0
        else:
            # This definition of objects may need to be revised. Needs to accommodate for being passed
            # JUST the object, then extract its title
            # likely a for key, value in objects list comprehension style
            self.objects = {item.title: item for item in objects}
            self.size = len(self.objects)

    def __len__(self):
        return self.size

    def __setitem__(self, key, value):
        # This should raise a TypeError if the key being set is not a string. We want this function to look things
        # up by their names, not by anything else. Therefore, we need to set keys that are only strings.
        # If it doesn't raise a TypeError, it will add the key:value pair and return True.
        # Otherwise, raise TypeError and return False.
        try:
            if type(key) is not str:
                raise TypeError
            else:
                self.objects[key] = value
                self.size = len(self.objects)
                return True
        except TypeError:
            print("<Collection> TypeError: Key {", key, "} is not of type \'str\'.")
            return False

    def __getitem__(self, key):
        # Raises TypeError if key being accessed is not a string.
        try:
            if type(key) is not str:
                if hasattr(key, "title"):
                    return self.objects[key.title]
                else:
                    raise TypeError
            else:
                item = self.objects[key]
                return item
        except TypeError:
            print("<Collection> TypeError: Key {", key, "} is not of type \'str\'.")
            return False
        except KeyError:
            print("<Collection> KeyError: {", key, "} not found.")
            return False

    def __delitem__(self, key):
        try:
            if type(key) is not str:
                raise TypeError
            else:
                del self.objects[key]
                self.size = len(self.objects)
                return True
        except TypeError:
            print("<Collection> TypeError: Key {", key, "} is not of type \'str\'.")
            return False
        except KeyError:
            print("<Collection> KeyError: Key {", key, "} not found.")
            return False

    def __iter__(self):
        return iter(key for key in self.objects)

    def __iterkeys__(self):  # Suggested inclusion, as this is a map, not just a sequence
        return self.__iter__()

    def __str__(self):
        output_string = ''
        for item in iter(self):
            # Set output to string of the object found at key location in this collection's object dictionary
            output_string += '\n' + str(self.objects[item]) + '\n'
            # This should be sorted here, for the sake of organization.
        return output_string

    def sort_collection(self):
        # Maybe use OrderedDict here. Can be imported and supports the sorting of things like this.
        return "This method not yet implemented!"

    def collect(self, item):
        # Should be used as the default method of adding new items to the collection.
        if hasattr(item, "title"):
            # Add item here
            self.objects[item.title] = item
            self.size = len(self.objects)
            return True
        else:
            # Unable to add by title, object has no title
            print("Could not add to the collection! This item has no title.")
            return False
            # Currently, Collection disallows unnamed additions. This could be changed later, but would likely
            # require quite a few changes to the way information is stored, as there would be multiple different
            # objects known by "unknown" names; i.e., dictionaries cannot have duplicate keys for unique values.

    def update_item(self, item):
        # Updates an individual item in the collection

        # This branch is called if a string is passed to the update_item function
        if type(item) is str:
            # No need to check if it has a title, we'll use the string as the title
            if self.objects[item]:
                # can_update = hasattr(self.objects[item], "update")
                # print("Has update:", can_update)
                if callable(getattr(self.objects[item], "update")):
                    # Don't need to use item.title here because the item IS its title
                    self.objects[item].update()
                    return True
                else:
                    print("This item has no way of updating.")
                    return False
        # This branch will be called if the item passed to this function is an object
        # Checks to see if the item has a title, i.e., if the item belongs in the collection, as all objects
        # that are added to the collection should have a title
        # PASSING OBJECTS IN THIS WAY MAY BE ENTIRELY POINTLESS, not certain if they will update w/in the collection
        # or just update themselves... Not certain why you would pass an object to this anyway.
        elif self.objects[item.title]:
            # Checks if item has update function
            # can_update = hasattr(item, "update")
            # print("Has update:", can_update)
            if callable(getattr(item, "update")):
                # Using item.title here because the title is the key to the object
                self.objects[item.title].update()
                return True
            else:
                print("This item has no way of updating. (called by item)")
                return False
        else:
            print("This item has not been added to the collection yet. Please add it first.")
            return False
