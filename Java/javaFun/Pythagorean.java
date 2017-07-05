import java.lang.Math;
class Pythagorean {
    public double calculateHypotenuse(int legA, int legB) {
        int legASq = legA * legA;
        int legBSq = legB * legB;
        int legSum = legASq + legBSq;
        double squareRoot = Math.sqrt(legSum);
        return squareRoot;
    }
}
