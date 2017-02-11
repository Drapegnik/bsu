/**
 * Created by Drapegnik on 04.12.15.
 */
public class ForestTree extends Tree {
    public ForestTree() {
        super();
    }

    public ForestTree(String name, int old, String type, int count) {
        super(name, type, old);
        this.count = count;
    }

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = count;
    }

    private int count;

    @Override
    public String toString() {
        return super.toString() + '\t' + count + "] ";
    }

    @Override
    public boolean equals(Object o) {
        ForestTree temp = (ForestTree) o;
        return super.equals(o) && count == temp.count;
    }
}
