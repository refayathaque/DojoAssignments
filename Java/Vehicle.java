public class Vehicle {
    // Don't have to explicitly mention 'public', it is public by default
    private int numberOfWheels;
    private String color;

    public Vehicle() {
        // ^ OVERLOADING the constructor method so class will compile even if we don't pass in default parameter values
        // * We can also put in DEFAULT values here
        this("Red", 10);
        // Will instantate 'Bus' and 'Truck', both Red with 10 wheels
    }

    public Vehicle(String color) {
        // ^ Constructor, executes code before OBJECT instantiation, here this sets a DEFAULT member (We will set Vehicle color) We will pass in 'color' through our executable when instantating the OBJECT
        this.color = color;
        // 'this.' IMPORTANT! Or default parameter values won't work!
    }
    public Vehicle(int number) {
        numberOfWheels = number;
        // ^ Constructor if we ONLY pass in 'number' default parameter values
    }
    public Vehicle(String color, int number) {
        this.color = color;
        numberOfWheels = number;
     }
    // ^ Constructor if we pass in default parameter values for 'color' AND 'numberOfWheels'

    // * All four CONSTRUCTORS above have different method SIGNATURES

    // Setters for 'numberOfWheels' and 'color'
    public void setNumberOfWheels(int number) {
        numberOfWheels = number;
        // 'void' because we are not returning anything
    }
    public void setColor(String c) {
        color = c;
    }

    // Getters for 'numberOfWheels' and 'color'
    public int getNumberOfWheels() {
        return numberOfWheels;
        // 'int' because we that is the data type we are returning
    }
    public String getColor() {
        return color;
    }

    public static void main(String[] args) {
        // Our executable ^ (doing this in lieu of a Test.java class)
        Vehicle truck = new Vehicle();
        Vehicle bus = new Vehicle();
        // Instantiating OBJECTS from Vehicle class, now we can access these two objects using variables 'truck' and 'bus'
        // DEFAULT values for constructor can be passed in with OBJECT instantiation ^

        // Using Getters and Setters to GET and SET member values
        truck.setNumberOfWheels(6); // Comment out to use DEFAULT values
        truck.setColor("Blue"); // Comment out to use DEFAULT values
        int truckWheels = truck.getNumberOfWheels();
        String truckColor = truck.getColor();

        bus.setNumberOfWheels(10); // Comment out to use DEFAULT values
        bus.setColor("Yellow"); // Comment out to use DEFAULT values
        int busWheels = bus.getNumberOfWheels();
        String busColor = bus.getColor();

        // Printing OBJECTS instantiated with member values we SET and GET (GOT)
        System.out.println("Truck has " + truckWheels + " wheels, and its color is " + truckColor);
        System.out.println("Bus has " + busWheels + " wheels, and its color is " + busColor);
    }

}
