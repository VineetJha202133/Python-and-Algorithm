#Function that returns all the permutation of the given string of length 3

def permutation(word): #Function which will return all permutation
    result=[]    #List to store results
     
    for i in range(len(word)):
        for j in range(len(word)):
            if i==j:
                continue 
            for k in range(len(word)):
                if j==k or i==k:    #if index j==k or i==k then it will skip that arrangement and return others    
                    continue
                result.append(word[i]+word[j]+word[k])  #Adding all the words in list
    print(result)
permutation("WHY")  #Calling function
