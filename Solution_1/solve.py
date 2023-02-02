"""
To solve this problem, 
We can use Dynamic Programming. The basic idea is to keep track of the number of ways to attend classes on each day. 
We can use three variables X, Y, and Z to store the number of ways to attend classes on the current day, the day before, and two days before, respectively. 
The number of ways to attend classes on the current day can be calculated as the sum of the number of ways to attend classes on the two days before and the day before, as we cannot miss four or more consecutive days. 
We can calculate the number of ways to attend classes over N days by adding the values of X, Y, and Z. 
The probability of missing the graduation ceremony can be calculated as the number of ways to miss the ceremony divided by the total number of ways to attend classes over N days.
"""

def solve(n):
    #check if the input is less than 4.
    if n<1:
        raise ValueError("The input must be a positive integer.")
    if n<4 and n>=1:
        return str(2**(n-1))+'/'+str(2**n)
    X=2 
    Y=1
    Z=1
    P = 4
    count = 8
    for i in range(4,n+1):
        temp= Z
        Z=Y
        Y=X
        X=P
        P= count
        count = (count-temp)*2+temp
    return str(X+Y+Z)+'/'+str(count)