public class Vehicle {
    // Don't have to explicitly mention 'public', it is public by default
    private int numberOfWheels;
    private String color;

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
        // Our executable (doing this in lieu of a Test.java class)
        Vehicle truck = new Vehicle();
        Vehicle bus = new Vehicle();
        // Instantiating OBJECTS from Vehicle class, now we can access these two objects using variables 'truck' and 'bus'

        // Using Getters and Setters to GET and SET member values
        truck.setNumberOfWheels(6);
        truck.setColor("Blue");
        int truckWheels = truck.getNumberOfWheels();
        String truckColor = truck.getColor();

        bus.setNumberOfWheels(10);
        bus.setColor("Yellow");
        int busWheels = bus.getNumberOfWheels();
        String busColor = bus.getColor();

        // Printing OBJECTS instantiated with member values we SET and GET (GOT)
        System.out.println("Truck has " + truckWheels + " wheels, and its color is " + truckColor);
        System.out.println("Bus has " + busWheels + " wheels, and its color is " + busColor);
    }

}
