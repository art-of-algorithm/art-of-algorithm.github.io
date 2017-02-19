#Following function check a no n for prime using fermat little theorem
def fermat(n):
    if n==2:
        return True
    if not n and 1:
        return False
    return pow(2,n-1,n)==1

#Main function for checking above function
n=int(raw_input())
if fermat(n):
    print n
