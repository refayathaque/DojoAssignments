public class Samurai extends Human {

    private static int numSamurais = 0;

    public Samurai() {
        this.setHealth(200);
        numSamurais++;
    }

    public Samurai(String name) {
        super(name);
        numSamurais++;
    }

    public void deathBlow(Human human) {
        human.setHealth(0);
        this.setHealth(this.getHealth() / 2);
        System.out.println(this.getName() + " SLAYED " + human.getName());
    }

    public void meditate() {
        int gained = this.getHealth() / 2;
        this.setHealth(this.getHealth() + gained);
        System.out.println(this.getName() + " meditated and his health is now " + gained);
    }

    public static int howMany() {
        return numSamurais;
    }

}
