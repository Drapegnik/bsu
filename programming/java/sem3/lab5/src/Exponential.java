/**
 * Created by Drapegnik on 27.11.15.
 */
public class Exponential extends Series {
    public Exponential(double first, double step, double n) {
        super(first, step, n);
    }
    @Override
    double solve(int j) {
        return first*Math.pow(step,j);
    }
}
