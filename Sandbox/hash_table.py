# each bucket will contain a linked list containing the objects stored at that index
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    def __init__(self):
        # defines size of internal array
        self.capacity = INITIAL_CAPACITY
        self.size = 0
        self.buckets = [None] * self.capacity

    # the hash function turns the key(string) into an index, thus sorting them into different buckets
    def hash(self, key):
        hashsum = 0
        # for each character in the key

        for index, c in enumerate(key):
            # add (index + length of key) raised to (current char code)

            hashsum += (index + len(key)) **ord(c)
            #perform modullus to keep hashsum in range [0, self.capacity - 1]

            hashsum = hashsum % self.capacity
        return hashsum

    # continue at https://stephenagrice.medium.com/how-to-implement-a-hash-table-in-python-1eb6c55019fd
