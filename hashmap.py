"""This module contains all the necessary code for instantiating a hashmap""" 
class HashMap:
    """Hashmap class; provides built in caching"""
    def __init__(self, initial_capacity=7):
        self.cap = initial_capacity
        self.buckets = [None] * self.cap
        self.siz = 0

    def _hash_function(self, key):
        """function for hashing"""
        row, column = key
        return (row * column) % self.cap

    def set(self, key, value):
        """sets a value in a hash table"""         
        if self.siz / self.cap >= 0.8:             
            self._rehash()
        index = self._hash_function(key)
        if self.buckets[index] is None:
            self.buckets[index] = []
        for kvp in self.buckets[index]:
            if kvp[0] == key:
                kvp[1] = value
                break
        else:
            self.buckets[index].append([key, value])             
            self.siz += 1

    def get(self, key):
        """gets the value of a specific key in the hash table"""         
        index = self._hash_function(key)
        if self.buckets[index] is None:
            raise KeyError()
        for kvp in self.buckets[index]:
            if kvp[0] == key:
                return kvp[1]
        raise KeyError()

    def remove(self, key):
        """removes the value of a specified key in the hashmap"""         
        index = self._hash_function(key)
        if self.buckets[index] is None:
            return
        for i, kvp in enumerate(self.buckets[index]):
            if kvp[0] == key:
                del self.buckets[index][i]
                self.siz -= 1
                break

    def clear(self):
        """clears the values out of the hash table"""         
        self.siz = 0
        self.cap = 7
        self.buckets = [None] * self.cap

    def _rehash(self):
        """rehashes the hash table"""         
        self.cap *= 2
        self.cap -= 1
        new_buckets = [None] * self.cap
        for bucket in self.buckets:
            if bucket is None:                 
                continue
            for kvp in bucket:
                index = self._hash_function(kvp[0])                 
                if new_buckets[index] is None:
                    new_buckets[index] = []                 
                new_buckets[index].append(kvp)
        self.buckets = new_buckets

    def list_buckets(self):
        """random bullshit"""
        for bucket in self.buckets:             
            print(bucket)

    def keys(self):
        """returns a list of hashmap keys"""         
        keys = []
        for bucket in self.buckets:
            if bucket:
                for k in bucket:                     
                    keys.append(k[0])
        return keys

    def capacity(self):
        """returns the capacity of the hash table"""         
        return self.cap

    def size(self):
        """returns the size of the hash table"""         
        return self.siz