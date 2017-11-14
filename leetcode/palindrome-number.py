class Solution(object):
    def isPalindrome(self, x):
        sign =  cmp(x,0);
        if sign < 0:
            return False;
        elif int(`x*sign`[::-1]) == x:
            return True;
        else:
            return False;
