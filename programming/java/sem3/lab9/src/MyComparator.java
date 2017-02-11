import java.util.Comparator;

/**
 * Created by Drapegnik on 11.12.15.
 */
public class MyComparator implements Comparator<Student> {
    public int compare(Student o1, Student o2) {
        if (o1.getCourse() != o2.getCourse()) return o1.getCourse() - o2.getCourse();
        else if (o1.getGroup() != o2.getGroup()) return o1.getGroup() - o2.getGroup();
        else return o1.getName().compareTo(o2.getName());
    }
}
