import java.util.Comparator;

/**
 * Created by Drapegnik on 21.12.15.
 */
public class MyComparator implements Comparator<Cleaner> {
    public int compare(Cleaner o1, Cleaner o2) {
        if (!o1.getFirm().equals(o2.getFirm()))
            return o1.getFirm().compareTo(o2.getFirm());
        else if (o1.getPower() != o2.getPower())
            return o2.getPower() - o1.getPower();
        else
            return o1.getColor().compareTo(o2.getColor());
    }
}

