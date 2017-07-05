public class FizzBuzz {
    public String fizzBuzz(int number) {
        if(number % 3 == 0 && number % 5 == 0) {
            return "FizzBuzz";
        }
        else if(number % 3 == 0) {
            return "Fizz";
        }
        else if(number % 5 == 0) {
            return "Buzz";
        }
        else {
            String x = String.valueOf(number);
            return x;
            // Must convert to String because everything else above returns a String, also Test is expecting a String
        }
    }
}
