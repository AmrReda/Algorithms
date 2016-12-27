__author__ = "Amr Reda"
#Selection Sort, time complexity: O(n^2)

#find the smallest value in an array
def findSmallest(arr):
    #store the smallest value
    smallest = arr[0]

    #store the index of smallest value
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

#sort array
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        #find the smallest element in array and adds it to the new array
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print selectionSort([5, 3, 6, 2, 10])