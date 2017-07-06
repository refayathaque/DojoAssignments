import java.util.ArrayList;
import java.lang.Math;

public class BasicJava {

    public int print1To255() {
        int i = 1;
        while(i < 255) {
            System.out.println(i);
            i++;
        }
        return i;
    }

    public void printodd1To255() {
        for(int q = 1; q < 255; q++) {
            if(q % 2 == 1) {
            // ^ Way to find odd numbers!
                System.out.println(q);
            }
        }
    }

    public void printSum() {
        int y = 0;
        for(int z = 0; z < 256; z++) {
            y += z;
            System.out.println("New number:" + z);
            System.out.println("Sum:" + y);
        }
    }

    public void iterateArray(int[] myArray) {
        for(int g = 0; g < myArray.length; g++) {
        // Only use size() to determine length of array when instantiating from ArrayList class
            System.out.println(myArray[g]);
        }
    }

    public void findMax(int[] myArray2) {
        int max = myArray2[0];
        for(int c = 0; c < myArray2.length; c++) {
            if(max < myArray2[c]) {
                max = myArray2[c];
            }
        }
        System.out.println(max);
    }

    public void getAverage(int[] myArray3) {
        int sum = 0;
        for(int t = 0; t < myArray3.length; t++) {
            sum += myArray3[t];
        }
        int avg = sum/myArray3.length;
        System.out.println(avg);
    }

    public void arrayOdd() {
    ArrayList<Integer> myArr = new ArrayList<>();
        for(int l = 1; l < 255; l++) {
            if(l % 2 == 1) {
            // ^ Way to find odd numbers!
            myArr.add(l);
            }
        }
        System.out.println(myArr);
    }

    public void greaterY(Integer[] myArray4, int number) {
        int counter = 0;
        for(int b = 0; b < myArray4.length; b++) {
            if(myArray4[b] > number) {
                counter++;
            }
        }
        System.out.println(counter);
    }
    // 'Integer' gives more functionality than just 'int'

    public void squareVal(Integer[] myArray5) {
        ArrayList<Integer> myArr2 = new ArrayList<>();
        for(int d = 0; d < myArray5.length; d++) {
            myArr2.add(myArray5[d] * myArray5[d]);
        }
        System.out.println(myArr2);
    }
    // Arrays are PROBABLY immutable in Java
}
