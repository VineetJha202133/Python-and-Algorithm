# Implementation of quick sort in python.

def partition(array, low, high):#Function to find partition position
    pivot = array[high] #Choosing right most element as pivot
    i = low - 1 

    for j in range(low, high):
        if array[j] <= pivot:#If element smaller than pivot swap it the greater element
          i = i + 1                                                
          (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quickSort(array, low, high):# Function of quicksort
  if low < high:
    pi = partition(array, low, high)

    quickSort(array, low, pi - 1)#Recursive call on the left

    quickSort(array, pi + 1, high)#Recursive call on the right
 

data = [11, 7, 2, 6, 0, 9, 3]#Function call
print("Unsorted Array")
print(data)

quickSort(data, 0, len(data) - 1)

print('Sorted Array in Ascending Order:')
print(data)
