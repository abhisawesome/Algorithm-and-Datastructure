# Input 321 
# Output 123
# -2^31 <= x <= 2^31 - 1

def sign(number):
    if(number >0):
        return 1
    if(number == 0):
        return 0
    if(number < 0):
        return -1
def reverse(input):
    if(-2**31 <=input and input <=((2**31)-1)):
        num = abs(input)
        reverseTemp = 0
        while num:
            temp = num %10
            reverseTemp = reverseTemp*10 + temp
            num = num // 10
        return (reverseTemp * sign(input))
    else:
        return 0

print(reverse(321))
print(reverse(-123))
print(reverse(0))
print(reverse(1534236469))
