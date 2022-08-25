#Program in python for binary search using recursion which returns index of the key needed.
def binary_search(my_list, low, high, key):

	
	if high >= low: 

		mid = (high + low)//2
		
		if my_list[mid] == key:
			return mid #If key is in middle
			
		elif my_list[mid] > key:
			return binary_search(my_list, low, mid - 1, key) #If key is small than mid it will be in left side of the list.
			
		else:
			return binary_search(my_list, mid + 1, high, key) #Else key can only be in the right side of the list.

	else:
		return "N/A" #If the value is not in the list.

nums=[7,16,23,44,56]
key=16

print("Element is present at index", binary_search(nums, 0, len(nums)-1, key))
