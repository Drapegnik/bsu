import java.io.IOException;
import java.io.PrintWriter;
import java.io.File;

/**
 * Created by Drapegnik on 27.11.15.
 */
public abstract class Series {
    protected double first;
    protected double step;
    protected double n;

    public Series() {
        this.first = 0;

        this.step = 0;
        this.n = 0;
    }

    public double getFirst() {
        return first;
    }

    public double getStep() {
        return step;
    }

    public double getN() {
        return n;
    }

    public void setFirst(double first) {
        this.first = first;
    }

    public void setStep(double step) {
        this.step = step;
    }

    public void setN(double n) {
        this.n = n;
    }

    public Series(double first, double step, double n) {
        this.first = first;
        this.step = step;
        this.n = n;
    }

    abstract double solve(int j);

    double sum() {
        double sum = 0;
        for (int i = 0; i < n; i++)
            sum += solve(i);
        return sum;
    }

    @Override
    public String toString() {
        StringBuffer s = new StringBuffer();
        for (int i = 0; i < n; i++)
            s.append(solve(i) + " ");
        return s.toString();
    }

    void save(String filename) throws IOException{
        PrintWriter wr = new PrintWriter(new File(filename));
        wr.close();
//        wr.println(this.toString());
//        } catch (IOException e) {
//            System.out.println(e);
//        } finally {
    }
}


