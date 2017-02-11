/**
 * Created by Drapegnik on 27.11.15.
 */
public class Liner extends Series {
    public Liner(double first, double step, double n) {
        super(first, step, n);
    }

    @Override
    double solve(int j) {
        return first + j * step;
    }
}
