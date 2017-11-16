#Solution to converting Roman numeral to an integer
#Given a roman numeral, convert it to an integer.
#Input is guaranteed to be within the range from 1 to 3999.

class Solution(object):
 def romanToInt(self, s):
  dic = {"I":1, "V":5, "X": 10, "L":50, "C":100 ,"D":500, "M":1000};
  dicComb = {"IV":4, "IX":9,"XL":40,"XC":90,"CD":400,"CM":900}
  strLen = len(s);

  val = 0;
  i =0
  #for i in range(0,strLen):
  while(i < strLen):
   if((i+1 < strLen) and ((s[i] + s[i+1]) in dicComb )):
    val += dicComb[(s[i] + s[i+1])];
    i = i + 1;
   else:
    val += dic[s[i]];
    print dic[s[i]];
    i = i + 1;
    return val;

  """
  :type s: str
  :rtype: int
  """
        
