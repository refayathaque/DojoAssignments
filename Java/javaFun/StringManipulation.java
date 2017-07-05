public class StringManipulation {

    public String trimAndConcat(String string, String string1) {
        String string3 = string.trim().concat(string1.trim());
        return string3;
        // Trim method will get rid of spaces BEFORE and AFTER a string, not spaces in the middle of strings
    }

    public Integer getIndexOrNull(String string, char letter) {
        if(string.indexOf(letter) > 0) {
            int number1 = string.indexOf(letter);
            return number1;
        }
        else {
            return null;
        }
    }
    // Set the TYPE to 'Integer' and not 'int' to be able to handle 'null'

    public Integer getIndexOrNull(String string, String string1) {
        if(string.indexOf(string1) > 0) {
            int number1 = string.indexOf(string1);
            return number1;
        }
        else {
            return null;
        }
    }

    public String concatSubstring(String string, int number, int number1, String string1) {
        String first = string.substring(number, number1);
        String finalv = first.concat(string1);
        return finalv;
    }
    // Substring method can be used like SPLICE in JavaScript
}
