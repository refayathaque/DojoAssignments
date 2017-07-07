public class Wizard extends Human {

    public Wizard() {
        this.setHealth(50);
        this.setIntelligence(8);
    }
    // ^ Where defaults for this class go

    public Wizard(String name) {
        super(name);
    }

    public void heal(Human human) {
        human.setHealth(human.getHealth() + this.getIntelligence());
        System.out.println(this.getName() + " healed " + human.getName() + " for " + this.getIntelligence() + " points ");
    }

    public void fireball(Human human) {
        int damage = this.getIntelligence() * 3;
        human.setHealth(human.getHealth() - damage);
        System.out.println(this.getName() + " launched a fireball at " + human.getName() + " for " + damage + " damage! ");
    }

}
