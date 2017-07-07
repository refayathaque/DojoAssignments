public class Mammal {

    private int energyLevel = 100;

    public Mammal(){}

    public void setEnergy(int energyLevel) {this.energyLevel = energyLevel;}

    public int getEnergy() {return energyLevel;}

    public int displayEnergy() {
        System.out.println("Energy Level is " + energyLevel);
        return energyLevel;
    }

}
