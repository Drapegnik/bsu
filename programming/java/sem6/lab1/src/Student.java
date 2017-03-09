/**
 * Created by Drapegnik on 07.03.17.
 */

import java.io.FileInputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.Serializable;
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
    private String id;

    public Student() {
        this.name = "";
        this.id = UUID.randomUUID().toString();
    }

    public Student(String name, int group) {
        this();
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
    public String toString() {
        return "Student{" +
                "id='" + id + '\'' +
                ",\tname='" + name + '\'' +
                ",\tgroup=" + group +
                '}';
    }

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

    /**
     * Method for reading students info from binary file
     *
     * @param filename String filename
     * @return {@link ArrayList} of {@link Student}s
     * @see Options#STUDENTS_FILE_NAME
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
}

