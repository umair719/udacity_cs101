__author__ = 'Umair'


# Define a function, hash_string,
# that takes as inputs a keyword
# (string) and a number of buckets,
# and returns a number representing
# the bucket for that keyword.

def hash_string(keyword, buckets):
    total_ord = 0
    for s in keyword:
        total_ord += ord(s)
    return total_ord % buckets


print(hash_string('a', 12))
#>>> 1

print(hash_string('b', 12))
#>>> 2

print(hash_string('a', 13))
#>>> 6

print(hash_string('au', 12))
#>>> 10

print(hash_string('udacity', 1000))
#>>> 11

print(hash_string('', 12))


def test_hash_function(func, keys, size):
    results = [0] * size
    keys_used = []
    for w in keys:
        if w not in keys_used:
            hv = func(w, size)
            results[hv] += 1
            keys_used.append(w)
    return results

