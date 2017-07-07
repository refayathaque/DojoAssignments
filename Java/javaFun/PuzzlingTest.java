import java.util.*;
import java.util.Collections;
import java.lang.Math;

class PuzzlingTest {
    public static void main(String[] args) {
        Puzzling iD = new Puzzling();

        int[] sumarray = {'3','5',1,2,7,9,8,13,25,32};

        System.out.println(iD.getSum(sumarray));

        ArrayList<String> japanesePeople = new ArrayList<>();

        japanesePeople.add("Nancy");
        japanesePeople.add("Jinichi");
        japanesePeople.add("Fujibayashi");
        japanesePeople.add("Momochi");
        japanesePeople.add("Ishikawa");

        System.out.println(iD.japaneseFolks(japanesePeople));

        char[] alphabet_array = {'a',	'b',	'c',	'd',	'e',	'f',	'g',	'h',	'i',	'j',	'k',	'l',	'm',	'n',	'o',	'p',	'q',	'r',	's',	't',	'u',	'v',	'w',	'x',	'y',	'z'};

        iD.alphabet(alphabet_array);
        
    }
}
