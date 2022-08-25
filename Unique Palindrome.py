#Function which return all the unique palindromes from a given string

class unique_palindrome: #Initializing class
    
    def __init__(self,string):
        self.my_str=string
        self.unique_set=set()
        
    def substring(self): #Function to find unique palindrome of given string
        i = 0
        while i <len(self.my_str):
            j = len(self.my_str) - 1
            while (j>i):
                if self.my_str[i] == self.my_str[j]:
                    if self.is_palindrome(i,j):
                        self.unique_set.add(self.my_str[i:j+1])
                        i = (i+j)//2
                        break
                j -= 1
            i+=1
            
    def is_palindrome(self,start,end): #Function to check palindrome
        while(start<=end):
            if(self.my_str[start]==self.my_str[end]):
                start+=1
                end-=1
            else:
                return False
        return True
        
string="abbabab" #Main
result=unique_palindrome(string)
result.substring()
print("The unique palindromes of the given string:", result.unique_set) #Output
