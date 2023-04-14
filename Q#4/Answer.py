#Boolean function to check for digit repetition in a number
def fun(s):
    s = ''.join(sorted(s))  #Sorting elements of string
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            return False     #If the digits repeat
        
    return True  #If digits doesnot repeat

#Taking inputs from user
lB = int(input())  #For lower bound
uB = int(input())  #For upper bound

count = 0  #To count numbers without digit repetitioin 

for i in range(lB,uB+1):
    if(fun(str(i))):  #if digits doesnot repeat
        count + = 1   #Incrementing value of count
        
#Printing number of integers in range without digit Repetition
print(count)
