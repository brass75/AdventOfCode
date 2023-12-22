class HashableDict(dict):
    def __hash__(self):
        return hash(tuple(self.items()))