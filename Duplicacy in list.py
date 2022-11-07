#Code to find duplicate values in the list.
def dupli(lis):                                       #Function to find duplicate values.
    dupli=[]                                          #List to store all duplicates
    for i in range(len(lis)):
        k=i+1
        for j in range(k,len(lis)):                     #Each value will be compared with another.
            if lis[i]==lis[j] and lis[i] not in dupli:  #If a elementis repeated more than once, it will be ignored through this condition
                dupli.append(lis[i])                    #Adding dupicate values in the list.
    return  dupli                                       #Result list containing all the duplicate values.

            
            
i=[2,6,5,7,5,4,6]                                    #Test 
print(dupli(i))
