#Solution for reverse integer problem.
#Given a 32-bit signed integer, reverse digits of an integer.
#Assume we are dealing with an environment which could only hold integers within the 32-bit signed integer range. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
class Solution(object):
    def reverse(self, x):
        maxNum = 2147483647;
        strVal = str(x);
        isSigned = False;
        
        if ("-" in strVal) == True:
            isSigned = True;
        
        reversed = "";
        for i in xrange(len(strVal)-1,-1,-1):
            reversed += strVal[i];
            
        if isSigned == False:
            reversed = int(reversed);
        else:
            reversed = -int(reversed[0:len(reversed)-1]);
        
        if( reversed >  maxNum or reversed < -maxNum):
            return 0;
        else:
            return reversed;
