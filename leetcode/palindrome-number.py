# Solution for Palindrome Problem
# Determine whether an integer is a palindrome. Do this without extra space.
class Solution(object):
    def isPalindrome(self, x):
        sign =  cmp(x,0);
        if sign < 0:
            return False;
        elif int(`x*sign`[::-1]) == x:
            return True;
        else:
            return False;
