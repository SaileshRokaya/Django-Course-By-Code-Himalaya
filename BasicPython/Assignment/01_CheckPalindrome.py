# Q.No 1) check whether a string is palindrome or not

# Method 
# a) Find reverse of string
# b) Check if reverse and original are same or not.

def isPalindrome(s):
    return s == s[::-1]
 
 
# Driver code
s = input()
ans = isPalindrome(s)
 
if ans:
    print(f"Yes, {s} is palindrome.")
else:
    print(f"No, {s} is not palindrome.")