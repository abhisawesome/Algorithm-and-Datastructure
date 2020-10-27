# Input: x = 123
# Output: 321

def reverse (x):
    num = abs(x)
    output = 0
    
    while(num > 0):
        lastDigit = num % 10
        output = output * 10 + lastDigit 
        num = num // 10
    if(output >= (-2 ** 31 ) or output <= (2 ** 31)-1):
        if(str(x)[0] == '-'):
             return(-1*output) 
        else:
            return(output)
    else:
        return 0

print(reverse(1534236469))