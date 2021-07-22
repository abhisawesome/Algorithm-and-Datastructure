# Given a string s, find the length of the longest substring without repeating characters.

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


def longest(s):
    long = 0
    char=""
    for i in s:
        if i not in char:
            char +=i
        else:
            long = max(long,len(char))
            char = char[char.index(i)+1:] + i
    return max(long,len(char))



print(longest("abcabcbb")) # 3
print(longest("pwwkew")) # 3
print(longest("")) # 0
print(longest("bbbbb")) # 1

print(longest("aab")) # 2
