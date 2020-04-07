# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        # Part 1: Hash collisions should be handled with an error warning. (Think about and
        # investigate the impact this will have on the tests)

        # Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''

        index = self._hash_mod(key)
        current = self.storage[index]  # Pair at current index
        pair = None  # Pair to insert

        # Check if current location is empty
        # Handle collisions by adding new LinkedPair
        while current and current.key != key:
            pair = current
            current = pair.next
        # If a node is found with same key
        if current:
            current.value = value
        # If a node is not found
        else:
            new = LinkedPair(key, value)
            new.next = self.storage[index]
            self.storage[index] = new

        # [{'hello': 'world'}, {'jump': 'rope'}, None]

        ### scenario 1
        # 'hi', 'john'
        # index = 0
        # current = (hello, world)
        # pair = (hello, world)
        # current = None

        ### scenario 2
        # hello, john
        # index = 0
        # current = hello, world
        # key's match
        # current.value = john

        ### scenario 3
        # hi, john
        # index = 2
        # new.next = None
        # new = hi, john
        


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]
        pair = None

        while current and current.key != key:
            pair = current
            current = pair.next
        # If key isn't in our storage
        if self.storage[index] is None:
            print("Key not found")
        # If key is in our storage
        else:
            # Remove the first element in the linked list
            # then basically making the head what was previously the next node
            if pair is None:
                self.storage[index] = current.next
            else:
                pair.next = current.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        current = self.storage[index]

        # keep looping through nodes until you find the key
        # else return None

        while current:
            if current.key == key:
                return current.value
            else:
                current = current.next
        return None


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_storage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        # loop through old storage, including nodes and add them to new storage

        for i in old_storage:
            current = i
            while current:
                self.insert(current.key, current.value)
                current = current.next

        





if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
