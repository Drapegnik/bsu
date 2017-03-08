/**
 * Created by Drapegnik on 07.03.17.
 */

import java.util.UUID;

/**
 * <p>Class for storing info about students</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class Student {
    private String name;
    private int group;
    private String id;

    public Student() {
        this.name = "";
        this.id = UUID.randomUUID().toString();
    }

    public Student(String name, int group) {
        super();
        this.name = name;
        this.group = group;
    }

    public Student(Student o) {
        this.name = o.name;
        this.group = o.group;
    }

    public String getName() {return name;}

    public void setName(String name) {this.name = name;}

    public int getGroup() {return group;}

    public void setGroup(int group) {this.group = group;}

    public String getId() {return id;}

    @Override
    public String toString() {return "Name: " + name + ", group: " + group;}

    @Override
    public boolean equals(Object o) {
        if (this == o) {return true;}

        if (o == null || getClass() != o.getClass()) {
            return false;
        }

        Student student = (Student) o;
        if (group != student.group) {return false;}

        return name.equals(student.name);
    }
}

