/**
 * Created by Drapegnik on 04.12.15.
 */
public class FruiteTree extends Tree {
    public FruiteTree() {
        super();
    }

    public FruiteTree(String name, int old, String type, int mass, int average) {
        super(name, type, old);
        this.mass = mass;
        this.average = average;
    }

    private int mass;
    private int average;

    @Override
    public String toString() {
        return super.toString() + '\t' + mass + '\t' + mass + "] ";
    }

    @Override
    public boolean equals(Object o) {
        FruiteTree temp = (FruiteTree) o;
        return super.equals(o) && mass == temp.mass && average == temp.average;
    }
}
