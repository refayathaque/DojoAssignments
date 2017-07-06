import java.util.ArrayList;

public class Portfolio {

    private ArrayList<Project> projects = new ArrayList<>();

    public Portfolio() {

    }

    public void addProject(Project project) {
        projects.add(project);
    }

    public ArrayList<Project> getProjects() {
        return projects;
    }

    public float getPortfolioCost() {
        float sum = 0;
        for(Project project: projects) {
            sum += project.getCost();
        }
        return sum;
    }

    public void showPortfolio() {
        for(int i = 0; i < projects.size(); i++) {
            projects.get(i).elevatorPitch();
        }
        System.out.println("Total Cost: $" + this.getPortfolioCost());
    }

}
