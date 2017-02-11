/**
 * Created by Drapegnik on 11.12.15.
 */
public class Student {
    private String name;
    private int number;
    private int course;
    private int group;

    public Student() {
        this.name = "";
        this.number = this.course  = this.group = 0;
    }

    public Student(String name, int number, int course, int group) {
        this.name = name;
        this.number = number;
        this.course = course;
        this.group = group;
    }

    public Student(Student o) {
        this.name = o.name;
        this.number = o.number;
        this.course = o.course;
        this.group = o.group;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getNumber() {
        return number;
    }

    public void setNumber(int number) {
        this.number = number;
    }

    public int getCourse() {
        return course;
    }

    public void setCourse(int course) {
        this.course = course;
    }

    public int getGroup() {
        return group;
    }

    public void setGroup(int group) {
        this.group = group;
    }

    @Override
    public String toString() {
        return name + "    " + number + "    " + course + "    " + group;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;

        Student student = (Student) o;

        if (number != student.number) return false;
        if (course != student.course) return false;
        if (group != student.group) return false;
        return name.equals(student.name);

    }
}

