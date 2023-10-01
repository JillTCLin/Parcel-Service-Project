# Ref: C950 - Webinar-1 - Let’s Go Hashing
# Ref: W-1_ChainingHashTable_zyBooks_Key-Value.py
# Ref: zyBooks: Figure 7.8.2: Hash table using chaining.

# D. Data struction: hash table
# E. Developed a chaining hash table
# Space Complexity:O(N)
class ChainingHashTable:
    '''
    A Chaining HashTable class with insert, search and remove function
    It's a data structure to store data.
    '''
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []    # build a list called table
        for i in range(initial_capacity):
            self.table.append([])  # append an empty list into table

    # Inserts a new item or update into the hash table.
    # Time Complexity:O(N)
    def insert(self, key, item):
        # hash function: get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # if key is already in the bucket, update the value
        # O(N)
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        # O(1)
        key_value = [key, item]         # construct a list from key and item
        bucket_list.append(key_value)
        return True

    # F. Develop a look-up function
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # Time Complexity:O(N)
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    # Time Complexity:O(N)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])
