def findReverse(num):
    temp = abs(num)
    reverse = 0
    while(temp):
        last = temp % 10
        reverse = reverse * 10 + last
        temp = temp // 10
    return reverse
        
def isPalindrome(x):
        reverse = findReverse(x)
        if( x == reverse ):
            return True
        else:
            return False

    
# print(isPalindrome(121))
print(isPalindrome(-121))

