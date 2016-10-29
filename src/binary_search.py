__author__ = "Amr Reda"
#Binary Search, time complexity: O(log(n))


def binary_search(list, item):
    # low and high keep track of which part of the list you'll search in
    low = 0
    high = len(list) - 1


    #While you haven't narrowed it down to one element .. 
    while low <= high:
        # ... check the middle element
        mid = (low + high) // 2
        guess = list[mid]
        # found the item.
        if guess == item:
            return mid
        
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


mylist = [1, 3, 5, 7 , 9, 11]
print binary_search(mylist, 3) # => 1

# 'None' means null python. We us to indicate that item wasn't found.
print binary_search(mylist, -1) # => None