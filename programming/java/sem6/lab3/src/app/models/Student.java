/**
 * Created by Drapegnik on 07.03.17.
 */

package app.models;

import java.io.*;
import java.util.ArrayList;
import java.util.UUID;

/**
 * <p>Class for storing info about students</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class Student implements Serializable {
    private String name;
    private int group;
    private ArrayList<Mark> marks;

    private String id;

    public Student() {
        this.name = "";
        this.id = UUID.randomUUID().toString();
        this.marks = new ArrayList<>();
    }

    public Student(String name, int group) {
        this();
        this.name = name;
        this.group = group;
    }

    public Student(String id, String name, int group) {
        this(name, group);
        this.id = id;
    }

    public Student(Student o) {
        this.id = o.id;
        this.name = o.name;
        this.group = o.group;
    }

    public String getName() {return name;}

    public void setName(String name) {this.name = name;}

    public int getGroup() {return group;}

    public void setGroup(int group) {this.group = group;}

    public String getId() {return id;}

    public ArrayList<Mark> getMarks() {return marks;}

    public void setMarks(ArrayList<Mark> marks) {this.marks = marks;}

    public void addMark(Mark mark) {this.marks.add(mark);}

    @Override
    public String toString() {
        StringBuilder marksString = new StringBuilder();
        for (Mark mark : marks) {
            marksString.append(mark.shortToString());
        }

        return "Student{" +
                "id='" + id + '\'' +
                ",\tname='" + name + '\'' +
                ",\tgroup=" + group +
                ",\tmarks={" + marksString +
                "} }";
    }

    public String shortToString() {
        return "Student{" +
                "id='" + id + '\'' +
                ",\tname='" + name + '\'' +
                ",\tgroup=" + group +
                "} }";
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {return true;}

        if (o == null || getClass() != o.getClass()) {
            return false;
        }

        Student student = (Student) o;
        return group == student.group && name.equals(student.name);
    }

    /**
     * Method for reading students info from binary file
     *
     * @param filename String filename
     * @return {@link ArrayList} of {@link Student}s
     */
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
        }
        return data;
    }

    /**
     * Method for writing students into binary file
     *
     * @param filename String filename
     * @param data     {@link ArrayList} of {@link Student}s
     */
    public static void writeInFile(String filename, ArrayList<Student> data) {
        try {
            FileOutputStream fos = new FileOutputStream(filename);
            ObjectOutputStream oos = new ObjectOutputStream(fos);

            oos.writeObject(data);
            oos.flush();

            oos.close();
            fos.close();
        } catch (IOException err) {
            System.out.println(err);
            System.err.println("Error while write data!");
        }
    }

    /**
     * Method for init dummy students data
     *
     * @return {@link ArrayList} of {@link Student}s
     */
    public static ArrayList<Student> generateFakeData() {
        ArrayList<Student> data = new ArrayList<>();
        data.add(new Student("Perry Hodges", 1));
        data.add(new Student("Patrick Richardson", 2));
        data.add(new Student("Doug Evans", 3));
        data.add(new Student("Cathy Russell", 4));
        data.add(new Student("Cecil Murphy", 1));
        data.add(new Student("Roberto Ball", 2));
        data.add(new Student("Glenda Romero", 3));
        data.add(new Student("Tomas King", 4));
        data.add(new Student("Sophia Simpson", 1));
        data.add(new Student("Wade Maxwell", 2));
        return data;
    }
}

