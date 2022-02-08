/*
Written by: Parker Cranfield
Feb 4th, 2022
THE LOGIC IN THIS CODE IS NOT MINE - this program was made to help learn how to use Java from C and was rewritten from C code

This converting program reverses a string
Usage: 'java convert <word>'
*/
public class convert {

    public static String changeString(String message) { // returns a reversed String
        int len = message.length();
        int i;
        char[] reversedChars = message.toCharArray();
        for (i = 0; i < len/2; i++) {
            char temp = reversedChars[i];
            reversedChars[i] = reversedChars[len - i - 1];
            reversedChars[len - i - 1] = temp;
        }
        String reversedString = new String(reversedChars);
        return reversedString;
    }
    public static void main(String[] args) {
        if (args == null) { // Makes sure someone has entered a word
            System.out.println("You need to provide the word to decode on the command line.");
            return;
        } 

        String word = args[0];
        String reversedWord = changeString(word); // Gets the reversed word and prints it
        System.out.println("Reversed word is: " + reversedWord);
        
    }
}