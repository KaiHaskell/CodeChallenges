# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.


# class Solution:
#     def isPalindrome(self, s: str) -> bool:

#         s = "".join(c for c in s if c.isalnum()).lower()

#         def isPal(s):
#             if len(s) < 2:
#                 return True

#             return s[0] == s[-1] and isPal(s[1:-1])

#         return isPal(s)

class Solution:
    # def isPalindrome(self, s: str) -> bool:
    def isPalindrome(self, s):
        s = "".join(c for c in s if c.isalnum()).lower()

        def ispal(s):
            if len(s) < 2:
                return True
            return s[0] == s[-1] and ispal(s[1:-1])

        return ispal(s)


string = "A man, a plan, a canal: Panama"

Solution.isPalindrome(string)
