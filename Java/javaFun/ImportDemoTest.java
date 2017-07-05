class ImportDemoTest {
    public static void main(String[] args) {
        ImportDemo iD = new ImportDemo(); // 1.
        String currentDate = iD.getCurrentDate(); // 2.
        System.out.println(currentDate); // 3.
    }
}

// From this point forward, we will be creating a test file that runs our Java classes. Our ImportDemo class should only contain information that belongs to the class itself. We want to separate class information to testing/running information. Therefore, we create a new file ImportDemoTest and it has the main entry method that actually implements our ImportDemo class

// 1. We are instantiating a new ImportDemo object. Now, all public methods of the ImportDemo class are available to the object

// 2. Calling the getCurrentDate() method on the object

// 3. Printing the currentDate string

// ***As long as both ImportDemo and ImportDemoTest files are in the same directory, you do not have explicitly import one into another. Also, you can just run the javac compiler on ImportDemoTest and it will compile both files for us
