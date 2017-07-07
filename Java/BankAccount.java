import java.util.Random;

public class BankAccount {
    private String accountNumber;
    private long checkingBal;
    private long savingsBal;

    private static int numAccounts = 0; // Static so they can be accessed anywhere wo instantiation
    private static long totalRevenue = 0;
    private static Random rand = new Random();

    public BankAccount(long checking, long savings) { // Constructor
        accountNumber = BankAccount.genAccountNum();
        checkingBal = checking;
        savingsBal = savings;
        totalRevenue =+ checkingBal + savingsBal;
        numAccounts++;
    }

    public BankAccount(long checking) {this(checking ,0);}
    public BankAccount() {this(0,0);}

    private static String genAccountNum() { // Private bc we dont want anyone else to access and static bc we want to be able to call it anywhere wo having to instantiate
        return Integer.toString(rand.nextInt(1000000000) + 1000000000);
    }

    // Getters and Setters
    public void setCheckingBalance(long checking) {
        checkingBal += checking;
    }

    public long getCheckingBalance() {
        return checkingBal;
    }

    public void setSavingsBalance(long savings) {
        savingsBal += savings;
    }

    public long getSavingsBalance() {
        return savingsBal;
    }
    //

    public void deposit(long checking, long savings) {
        this.setCheckingBalance(this.getCheckingBalance() + checking);
        this.setSavingsBalance(this.getSavingsBalance() + savings);
        totalRevenue += checking + savings;
    }

    public void deposit(long checking) {
        this.setCheckingBalance(this.getCheckingBalance() + checking);
        totalRevenue += checking;
    }

    public void withdrawal(long checking, long savings) {
        if(this.getCheckingBalance() < 1 && this.getSavingsBalance() < 1){
            return;
        }

        long total = this.getSavingsBalance() + this.getCheckingBalance();

        this.setSavingsBalance(this.getSavingsBalance() - checking);
        this.setCheckingBalance(this.getCheckingBalance() - savings);

        totalRevenue -= total;
    }

    public void show() {
        long total = this.getCheckingBalance() + this.getSavingsBalance();
        System.out.println("Total Balance : " + total);
    }

    public static void main(String[] args) {
        BankAccount raf = new BankAccount(111);
        BankAccount tony = new BankAccount(111);
        BankAccount cheryl = new BankAccount(111);
        BankAccount jenny = new BankAccount(111);

        raf.show();
        tony.show();
        cheryl.show();
        jenny.show();

        raf.deposit(12345);
        cheryl.withdrawal(34, 34);
        raf.show();
        cheryl.show();

    }

}
