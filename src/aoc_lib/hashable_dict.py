class HashableDict(dict):
    def __hash__(self):
        return hash(tuple(self.items()))

    def __setitem__(self, key, value):
        # The key must be hashable because it's a dictionary. We run a hash on the value to make sure that is. since
        # that will raise a TypeError if it's not we don't need to do anything else.
        hash(value)
        super().__setitem__(key, value)


class HashableSet(set):
    def __hash__(self):
        return hash(tuple(n for n in self))

    def add(self, element):
        # We run a hash on the element to make sure that is. since that will raise a TypeError if it's not we don't
        # need to do anything else.
        hash(element)
        super().add(element)
