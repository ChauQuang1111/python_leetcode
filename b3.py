#  13/08/2025
#  342. Power of Four 
#  326. Power of Three


def  isPowerOfFour(n):
    if n<=0: return False
    while n%4==0:
        n=n/4
    if n==1:
        return True
    else:
        return False
    

def isPowerofThree(m):
    if m<=0 : return False
    while m%3==0:
        n=n/3
    if n==1:
        return True
    else:
        return False


numbers=[1,2,3,4]
res1=isPowerOfFour(numbers)
res2=isPowerofThree(numbers)