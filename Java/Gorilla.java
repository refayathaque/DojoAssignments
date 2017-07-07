public class Gorilla extends Mammal {

    public void throwThings() {
        System.out.println("Gorilla has thrown things!");
        this.setEnergy(this.getEnergy() - 5);
    }

    public void eatBananas() {
        System.out.println("Gorilla is satisfied!");
        this.setEnergy(this.getEnergy() + 10);
    }

    public void climb() {
        System.out.println("Gorilla has climbed a tree!");
        this.setEnergy(this.getEnergy() - 10);
    }

}
