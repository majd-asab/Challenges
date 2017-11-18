#Write a function to find the longest common prefix string amongst an array of strings.
class Solution(object):
	def longestCommonPrefix(self, strs):
		strSoFar="";
		isSimilar=True;
		for i in range(0,len(strs)):
			if(strs[i] == "") or (isSimilar == False):
				return "";
			else:
				if(strSoFar == ""):
					strSoFar = strs[i];
    else:
    	if(len(strs[i]) >= len(strSoFar)):
    		tempStrs="";
    		for j in range(0,len(strSoFar)):
    			if(strSoFar[j] == strs[i][j]):
    				tempStrs += strs[i][j];
    			else:
    				break;
  				isSimilar = not(tempStrs == "");
  				strSoFar = tempStrs;
  			else:
  				tempStrs="";
  				for j in range(0,len(strs[i])):
  					if(strSoFar[j] == strs[i][j]):
  						tempStrs += strs[i][j];
  					else:
  						break;
						isSimilar = not(tempStrs == "");
						strSoFar = tempStrs;
 	return strSoFar;


"""
:type strs: List[str]
:rtype: str
"""
