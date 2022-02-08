/*
Written by: Parker Cranfield
Feb 4th, 2022
THE LOGIC IN THIS CODE IS NOT MINE - this program was made to help learn how to use Java from C and was rewritten from C code

This encrytion program encrypts an decrypted string using a password
Usage: 'java encrypt <word> <password>'
*/
public class encrypt {

    public static String encryptString(String message, String password) {
        int m = 0, p = 0, i;
        char[] messageChar = message.toCharArray();
        char[] passwordChar = password.toCharArray();
        int len = message.length();
        for (i = 0; i < len; i++)
        {
            messageChar[m] = (char)(65 + ((messageChar[m] & 0x9F) + (passwordChar[p] & 0x9F)) % 26); // Encrypts each char in the word
            m++;
            p++;
            if (passwordChar[p] == 0)
                p = 0;
        } 
        String decrypted = new String(messageChar);
        return decrypted;
    }


    public static void main(String[] args) {
        if (args.length < 2) { // I/O Check
            System.out.println("Usage: java encrypt <word> <password>");
            System.out.println("Cannot decrypt without supplying both a word and a password!");
            return; // Failure
        } 

        String decrypted = args[0];
        // Decrypt the word
        String encrypted = encryptString(decrypted, args[1]);
        // Output the word
        System.out.println("Encrypted word is: "+ encrypted);
        // Success
        return; 
    }
}
