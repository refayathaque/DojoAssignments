class StringManipulationTest {
    public static void main(String[] args) {
        StringManipulation iD = new StringManipulation();

        String value = iD.trimAndConcat(" Hello ", " World");
        System.out.println(value); // HelloWorld, NOT _Hello__World

        Integer value1 = iD.getIndexOrNull("Hello", 'j');
        System.out.println(value1); // null
        // Set the TYPE to 'Integer' and not 'int' to be able to handle 'null'

        Integer value2 = iD.getIndexOrNull("Hello", "llo");
        System.out.println(value2); // 2

        String value3 = iD.concatSubstring("Hello", 1, 2, "World");
        System.out.println(value3); // eWorld
    }
}
