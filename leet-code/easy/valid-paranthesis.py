# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

#     Open brackets must be closed by the same type of brackets.
#     Open brackets must be closed in the correct order.

# Input: s = "()"
# Output: true


# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false

stack = []
def pop():
    return stack.pop()
def push(ele):
    return stack.append(ele)

def isValid(s):
    for element in s[:]:
        if(element in ['{','(','[']):
            push(element)
        else:
            if(element == ')' and stack[-1] == '('):
                pop()
            elif(element == ']' and stack[-1] == '['):
                pop()
            elif(element == '}' and stack[-1] == '{'):
                pop()
            else:
                return False
    return len(stack) == 0

print(isValid('{[]}'))