/*
Return the number of different transformations (From alphabets to . & -) among all words we have.
*/

class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        String[] array = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};
      
        Set<String> transformedWords = new HashSet<String>();
        
        // going through the words array
        for(int i = 0; i< words.length; i++){
            String transformedWord="";
            for(int j = 0; j< words[i].length(); j++){
                int c = words[i].charAt(j)-97;
                transformedWord += array[c];
            }
            transformedWords.add(transformedWord);
            transformedWord="";
        }
        return transformedWords.size();
        
    }
}
