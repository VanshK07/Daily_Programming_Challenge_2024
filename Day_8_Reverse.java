public class ReverseWords {
    public static String reverseWords(String s) {
        String[] words = s.trim().split("\\s+");
        StringBuilder reversedString = new StringBuilder();
        
        for (int i = words.length - 1; i >= 0; i--) {
            reversedString.append(words[i]);
            if (i != 0) {
                reversedString.append(" ");
            }
        }
        
        return reversedString.toString();
    }

    public static void main(String[] args) {
        String s = "The Sky is blue ";
        System.out.println(reverseWords(s)); 
    }
}
