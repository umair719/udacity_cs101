__author__ = 'Umair'


# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.

def make_hashtable(nbuckets):
    #hash_table= []
    #while nbuckets:
    #    hash_table.append([])
    #    nbuckets -= 1
    #return hash_table
    table = []
    for e in range(0, nbuckets):
        table.append([])
    return table


print(make_hashtable(5))