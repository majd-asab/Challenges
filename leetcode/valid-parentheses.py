#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
class Solution(object):
    def isValid(self, s):
        parenArr = []; # if you see a paren, add it to the array 
        
        if(s[0] == ")" or s[0] ==  "]" or s[0] ==  "}"):
            return False;
        else:
            for i in range(0,len(s)):
                if(s[i] == "(" or s[i] == "[" or s[i] == "{"):
                    parenArr.append(s[i]);
                elif(s[i] == ")" and len(parenArr) > 0 and (parenArr[len(parenArr)-1] == "(")):
                    parenArr.pop(len(parenArr)-1);
                elif(s[i] == "]" and len(parenArr) > 0 and (parenArr[len(parenArr)-1]  == "[")):
                    parenArr.pop(len(parenArr)-1);
                elif(s[i] == "}" and len(parenArr) > 0 and (parenArr[len(parenArr)-1]  == "{")):
                    parenArr.pop(len(parenArr)-1);
                else:
                    return False;
            if not (len(parenArr) == 0):
                return False;
            return True
        
        """
        :type s: str
        :rtype: bool
        """
