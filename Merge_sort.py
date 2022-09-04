#Implement Merge Sort Algorithm with all the necessary functions.
def merge_sort(arr):
    
     if len(arr)>1:
        mid=len(arr)//2      #Dividing into two parts(Divide and conquer)

        L=arr[:mid]             #Slicing
        R=arr[mid:] 

        merge_sort(L)       #Recursion
        merge_sort(R) 


        i=j=k=0 
        while i<len(L) and j<len(R):                  #Copy data to array L[] and R[]
            if L[i]<R[j]:
                arr[k]=L[i]
                i +=1
            else:   
                arr[k]=R[j]
                j +=1
            k=k+1

        while i < len(L):                          #Checking if any element is left
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        
def printList(arr):
    for i in range(len(arr)):  #Printing the sorted array
        print(arr[i], end=" ")
    print()


arr = [2, 10, 14, 16, 9, 4]
merge_sort(arr)
printList(arr)   
