/**
 * Created by Drapegnik on 27.11.15.
 */
public class Main {

    public static void main(String[] args) {
        Liner a = new Liner(1, 2, 10);
        Exponential b = new Exponential(1, 2, 10);
        System.out.println(a.toString());
        System.out.println(b.toString());

        new MyJFrame("Series", a, b);
    }
}
