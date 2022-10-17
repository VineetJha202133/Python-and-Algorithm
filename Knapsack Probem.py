bag_weight = int(input("\nEnter the weight of bag: "))  #Taking input of weight

w = input("\nEnter the weight of objects: ")    #Taking weights of different objects
w = w.split()
w = [int(x) for x in w]                      #Converting string to integer 
print("\nWeight List: ",w)                   #Printing the input taken

p = input("\nEnter the value of profits: ")  #Taking values  of profit
p = p.split()
p = [int(y) for y in p]                                     #Converting string to integer 
print("\nProfit List: ",p)

list = [(w[i],p[i]) for i in range(len(w))]  #Combining to make a list
print("\nWeight - Profit Pair: ",list)

def knapSack(bag_weight,list):  #Defining function
    list=sorted(list, key = lambda i : i[1], reverse=True)  #Sorting
    print("\nSorted list: ",list)

    total_profit = 0

    for item in list:
        if item[0] <= bag_weight:
            total_profit=total_profit + item[1]
            bag_weight= bag_weight-item[0]
    return total_profit

if __name__ == '__main__':             #Test_case
    A=knapSack(bag_weight,list)          #Function call
    print("\nMaximum Profit : ",A)
    print("\n")
