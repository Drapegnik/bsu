import java.util.ArrayList;
import java.util.Collections;

/**
 * Created by Drapegnik on 30.11.15.
 */
public class MyContainer<T extends Tree> extends ArrayList<T> {
    public MyContainer() {
        super();
    }

    public T minimum() throws MyException {

        if (this.isEmpty())
            throw new MyException("There is no elements in MyCountainer!");

        return Collections.min(this);
    }

    public void print() {
        for (T e : this) {
            System.out.print(e);
        }
        System.out.println();
    }

    public int count(T o) {
        return Collections.frequency(this, o);
    }

    public int search(T o) {
        MyContainer<T> temp = (MyContainer) this.clone();
        temp.sort(null);
        int index = Collections.binarySearch(temp, o);
        if (index != -1)
            return this.indexOf(temp.get(index));
        else
            return -1;
    }
}
