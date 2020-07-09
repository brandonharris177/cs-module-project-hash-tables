class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity, items=0):
        # Your code here
        # Sets the capacity to an array of Nones with the length equal to the capacity
        self.capacity = [None] * capacity
        self.items = items


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.capacity)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        load_factor = self.items/self.get_num_slots()
        return load_factor


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # makes sure the key is a string and then encode it into bytes
        str_key = str(key).encode()
        # hash value set according to the algorithm
        hash = 0xcbf29ce484222325

        for byte in str_key:
            hash *= 0x100000001b3
            hash ^= byte
            hash &= 0xffffffffffffffff 
        return hash


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.get_num_slots()
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current_Node = self.capacity[index]
        if current_Node is None:
            self.capacity[index] = HashTableEntry(key, value)
            self.items += 1
            if self.get_load_factor() > 0.7:
                self.resize(self.get_num_slots() * 2)
        else:
            #loop through the list
            while current_Node is not None:
            #find value
                if current_Node.key == key:
                    current_Node.value = value
                    break
                current_Node = current_Node.next
            if current_Node is None:
                next_value = self.capacity[index]
                self.capacity[index] = HashTableEntry(key, value)
                self.capacity[index].next = next_value
                self.items += 1
                if self.get_load_factor() > 0.7:
                    self.resize(self.get_num_slots() * 2)
        


    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        current_Node = self.capacity[index]
        
        if current_Node is None:
            print("Key not found")
        elif current_Node.key == key:
            self.capacity[index] = current_Node.next
            self.items -= 1
        else:
            #loop through the list
            while current_Node.next is not None:
            #find value
                if current_Node.next.key == key:
                    current_Node.next = current_Node.next.next
                    self.items -= 1
                    break
                current_Node = current_Node.next
            print("Key not found")


    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)

        current_Node = self.capacity[index]
        #loop through the list
        while current_Node is not None:
        #find value
            if current_Node.key == key:
                #return the node
                return current_Node.value
            current_Node = current_Node.next
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        new_hash_table = HashTable(new_capacity)
        for table in self.capacity:
            loop_table = table
            while loop_table is not None:
                new_hash_table.put(table.key, table.value)
                loop_table = loop_table.next
        self.capacity = new_hash_table.capacity

# if __name__ == "__main__":
# ht = HashTable(8)

# ht.put("line_1", "'Twas brillig, and the slithy toves")
# ht.put("line_2", "Did gyre and gimble in the wabe:")
# ht.put("line_3", "All mimsy were the borogoves,")
# ht.put("line_4", "And the mome raths outgrabe.")
# ht.put("line_5", '"Beware the Jabberwock, my son!')
# print(len(ht.capacity))
# ht.put("line_6", "The jaws that bite, the claws that catch!")
# print(len(ht.capacity))
# ht.put("line_7", "Beware the Jubjub bird, and shun")
# ht.put("line_8", 'The frumious Bandersnatch!"')
# ht.put("line_9", "He took his vorpal sword in hand;")
# ht.put("line_10", "Long time the manxome foe he sought--")
# ht.put("line_11", "So rested he by the Tumtum tree")
# ht.put("line_12", "And stood awhile in thought.")

# print(ht.items)

# ht.delete("line_12")

# print(ht.items)

#     # Test storing beyond capacity
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     # Test resizing
#     old_capacity = ht.get_num_slots()
#     ht.resize(ht.capacity * 2)
#     new_capacity = ht.get_num_slots()

#     print(f"\nResized from {old_capacity} to {new_capacity}.\n")

#     # Test if data intact after resizing
#     for i in range(1, 13):
#         print(ht.get(f"line_{i}"))

#     print("")