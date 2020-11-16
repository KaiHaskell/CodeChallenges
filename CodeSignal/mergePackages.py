# Given a package with a weight limit and an array of integers items of where each integer represents the weight of an item,
# implement a function merge_packages that finds the first two items in the items array whose
# sum of weights equals the given weight limit limit.

# Your function should return a pair [i, j] of the indices of the item weights,
# ordered such that i > j. If such a pair doesn’t exist, return an empty array.


def merge_packages(items, limit):
    cache = {}
    # creating a cache to hold onto enumerated values

    for i, n in enumerate(items):
        # finding the difference
        diff = limit - n
        # if the difference exists, we can safely return the flipped index values
        if diff in cache:
            return [i, cache[diff]]
        # otherwise add it to the cache
        cache[n] = i
    # if nothing works return an empty array
    return []

# Space Complexity: Worst Case O(n) | Best Case O(n)
# Time Complexity: Worst Case O(n) | Best Case O(1)

# Enumerate creates a copy, then mutates the copy thus creating more Space
