public class StringDemo {
    public static void main(String[] args) {

        // Length - Strings have a method to determine their length
        String ninja = "Coding Dojo is Awesome!";
        int length = ninja.length();
        System.out.println("String length is:" + length); // String length is:23

        // Concatenate - A String method that allows two strings to be squashed together. Since each string is immutable, this results in a brand new string
        String string1 = "My name is ";
        String string2 = "Refayat";
        String string3 = string1.concat(string2);
        System.out.println(string3); // My name is Refayat

        // Format - Another way of concatenating strings
        String ninjar = String.format("Hi %s, you owe me $%.2f", "Claudia", 12.50);
        System.out.println(ninjar); // Hi Claudia, you owe me $12.50
        // Where %s is expecting a string
        // And %.2f is expecting a float data type. The value 2 will just place two values to right of the decimal point

        // IndexOf - The indexOf() method searches left-to-right inside the given string for a "target" string. The indexOf() method returns the index number where the target string is first found or -1 if the target is not found
        String ninjab = "Welcome to Coding Dojo!";
        int a = ninjab.indexOf("Coding");
        int b = ninjab.indexOf("co");
        int c = ninjab.indexOf("pizza");
        System.out.println(a); // 11
        System.out.println(b); // 3
        System.out.println(c); // -1, bc 'pizza' is not found
    }
}
