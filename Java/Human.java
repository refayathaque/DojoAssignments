public class Human {

    private String name = "";
    private int strength = 3;
    private int stealth = 3;
    private int intelligence = 3;
    private int health = 100;

    public Human() {}
    // ^ Need another blank constructor in case we don't pass in any names

    public Human(String name) {this.name = name;}

    public String getName() {
        return name;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public void setIntelligence(int intelligence) {
        this.intelligence = intelligence;
    }

    public void setStealth(int stealth) {
        this.stealth = stealth;
    }

    public int getStealth() {
        return stealth;
    }

    public int getHealth() {
        return health;
    }

    public int getIntelligence() {
        return intelligence;
    }

    public void attack(Human human) {
        human.setHealth(human.getHealth() - strength);
        System.out.println(this.getName() + " dealt " + strength + " damage to " + human.getName());
    }

    public static void main(String[] args) {
        Wizard tim = new Wizard("Tim");
        Human will = new Human("Will");
        Ninja marco = new Ninja("Marco");
        Samurai minh = new Samurai("Minh");

        tim.attack(will);
        tim.fireball(will);
        tim.heal(will);

        marco.steal(tim);

        minh.deathBlow(tim);

        minh.meditate();
    }

}
