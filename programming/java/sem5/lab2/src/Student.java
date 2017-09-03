import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.Serializable;
import java.util.ArrayList;


/**
 * Created by Drapegnik on 11.12.15.
 */
public class Student implements Serializable {
    private String name;
    private int group;
    private int markMath;
    private int markProg;
    private int markHistory;

    public Student() {
        this.name = "";
        this.markMath = this.markHistory = this.markProg = this.group = 0;
    }

    public Student(String name, int group, int markMath, int markProg, int markHistory) {
        this.name = name;
        this.group = group;
        this.markMath = markMath;
        this.markHistory = markHistory;
        this.markProg = markProg;
    }

    public Student(Student o) {
        this.name = o.name;
        this.group = o.group;
        this.markMath = o.markMath;
        this.markHistory = o.markHistory;
        this.markProg = o.markProg;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getGroup() {
        return group;
    }

    public void setGroup(int group) {
        this.group = group;
    }

    public int getMarkMath() {
        return markMath;
    }

    public void setMarkMath(int markMath) {
        this.markMath = markMath;
    }

    public int getMarkProg() {
        return markProg;
    }

    public void setMarkProg(int markProg) {
        this.markProg = markProg;
    }

    public int getMarkHistory() {
        return markHistory;
    }

    public void setMarkHistory(int markHistory) {
        this.markHistory = markHistory;
    }

    @Override
    public String toString() {
        return name + "    " + group + ":    " + markMath + "    " + markProg + "    " + markHistory;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Student student = (Student) o;

        if (group != student.group) return false;
        return name.equals(student.name);

    }

    public static ArrayList<Student> readFromFile(String filename) {
        ArrayList<Student> data = new ArrayList<>();
        try {
            FileInputStream fis = new FileInputStream(filename);
            ObjectInputStream ois = new ObjectInputStream(fis);

            data = new ArrayList<>((ArrayList<Student>) ois.readObject());

            ois.close();
            fis.close();
        } catch (IOException | ClassNotFoundException err) {
            System.out.println(err);
            System.err.println("Error while read data!");
        } finally {
            return data;
        }
    }
}

