class BasicJavaTest {
    public static void main(String[] args) {
        BasicJava iD = new BasicJava();

        int value = iD.print1To255();
        System.out.println(value);

        iD.printodd1To255();
        // Just INVOKE here because we have System.out.println(q) in method

        iD.printSum();

        int[] myArray;
        myArray = new int[3];
        myArray[0] = 1;
        myArray[1] = 2;
        myArray[2] = 3;

        iD.iterateArray(myArray);

        int[] myArray2;
        myArray2 = new int[3];
        myArray2[0] = -4;
        myArray2[1] = -3;
        myArray2[2] = -32;

        iD.findMax(myArray2);

        int[] myArray3;
        myArray3 = new int[3];
        myArray3[0] = 2;
        myArray3[1] = 4;
        myArray3[2] = 6;

        iD.getAverage(myArray3);

        iD.arrayOdd();

        Integer[] myArray4;
        myArray4 = new Integer[5];
        myArray4[0] = 2;
        myArray4[1] = 4;
        myArray4[2] = 6;
        myArray4[3] = -4;
        myArray4[4] = 1;

        iD.greaterY(myArray4, 1);

        Integer[] myArray5;
        myArray5 = new Integer[5];
        myArray5[0] = 1;
        myArray5[1] = 2;
        myArray5[2] = 3;
        myArray5[3] = 4;
        myArray5[4] = 5;

        iD.squareVal(myArray5);

        Integer[] myArray6;
        myArray6 = new Integer[5];
        myArray6[0] = -1;
        myArray6[1] = 2;
        myArray6[2] = -3;
        myArray6[3] = 4;
        myArray6[4] = -5;

        iD.elimNegs(myArray6);

        Integer[] myArray7;
        myArray7 = new Integer[4];
        myArray7[0] = 4;
        myArray7[1] = 6;
        myArray7[2] = -4;
        myArray7[3] = 10;

        iD.minMaxAvg(myArray7);

        Integer[] myArray8;
        myArray8 = new Integer[4];
        myArray8[0] = 1;
        myArray8[1] = 2;
        myArray8[2] = 3;
        myArray8[3] = 4;

        iD.shiftVal(myArray8);
    }
}
