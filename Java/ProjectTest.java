public class ProjectTest {
    public static void main(String[] args) {

        Project p = new Project();
        p.setName("Test");
        p.setDescription("Here's a description");
        p.setCost(3.20f);
        // p.elevatorPitch();

        Project q = new Project("Test 2");
        q.setCost(43.30f);
        // q.elevatorPitch();

        Project r = new Project("Test 3", "Adfdaslkfjad");
        r.setCost(1.44f);
        // r.elevatorPitch();

        Portfolio portfolio = new Portfolio();
        portfolio.addProject(p);
        portfolio.addProject(q);
        portfolio.addProject(r);
        portfolio.showPortfolio();
    }
}
