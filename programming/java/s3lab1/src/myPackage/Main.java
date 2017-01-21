package myPackage;
/**
 * Created by Drapegnik on 30.10.15.
 */
public class Main {

    public static void main(String[] args) {
        try {
            if (args.length != 2)
                throw new MyException("Exactly 2 parameters required");
        }catch (MyException e)
        {
            System.out.println(e);
            return;
        }

        double eps=0, x=0;

        try {
            x = Double.parseDouble(args[0]);
        } catch (NumberFormatException ex) {
            throw new IllegalArgumentException(ex.getMessage() + " First arg (x) must be a double!");
        }

        try {
            eps = Double.parseDouble(args[1]);
        } catch (IllegalArgumentException ex) {
            System.out.println("Converting failed: " + ex.getMessage());
            return;
        }

        if (Math.abs(x) > 1)
            throw new IllegalArgumentException("Bad x value. Series diverges!");

        System.out.println(sum(x,eps));

    }

    private static double sum(double x, double eps) {
        double k=1,a=1,ans=0;
        do {
            a*=((-x*(k+1))/(k*3));
            ans+=a;
            k++;
        } while (Math.abs(a) > eps);

        return ans;
    }
}