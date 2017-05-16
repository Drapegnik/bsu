/**
 * Created by Drapegnik on 07.03.17.
 */

package app.models;

import app.config.Options;
import app.models.wrappers.Marks;

import java.io.*;
import java.util.ArrayList;
import java.util.UUID;
import javax.xml.bind.annotation.*;

/**
 * <p>Class for storing info about students</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
@XmlRootElement
public class Student implements Serializable {
    private String name;
    private int group;

    @XmlAttribute
    private String id;

    @XmlElement(name = "marks")
    private Marks marks;

    public Student() {
        this.name = "";
        this.id = UUID.randomUUID().toString();
        this.marks = new Marks();
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
        this.marks = o.marks;
    }

    public String getName() {return name;}

    public void setName(String name) {this.name = name;}

    @XmlElement
    public int getGroup() {return group;}

    public void setGroup(int group) {this.group = group;}

    public String getId() {return id;}

    @XmlElement(name = "marks")
    public Marks getMarksClass() {return marks;}

    @XmlTransient
    public ArrayList<Mark> getMarks() {return marks.getData();}

    public void setMarks(ArrayList<Mark> marks) {this.marks.setData(marks);}

    public void addMark(Mark mark) {this.marks.addElement(mark);}

    @Override
    public String toString() {
        StringBuilder marksString = new StringBuilder();
        for (Mark mark : marks.getData()) {
            marksString.append(mark.shortToString());
        }

        return "Student{" +
                "id='" + id + '\'' +
                ",\tname='" + name + '\'' +
                ",\tgroup=" + group +
                ",\tmarks={" + marksString +
                "} }";
    }

    public String formattedToString() {
        StringBuilder str = new StringBuilder(name + " - " + group + "       |");
        for (Mark mark : marks.getData()) {
            str.append("       ").append(mark.getGrade());
        }

        return str.toString();
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

    /**
     * Method for writing students into binary file
     *
     * @param filename String filename
     * @param data     {@link ArrayList} of {@link Student}s
     * @see Options#STUDENTS_FILE_NAME
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

    /**
     * Method for generate tittle for {@link Student}s table in {@link app.ui}
     * with correct {@link Subject}'s name
     *
     * @return {@link String} tittle
     */
    public static String getTittle() {
        StringBuilder tittle = new StringBuilder("name:   group:   |   ");
        for (Subject subj : Subject.values()) {
            tittle.append(subj.toString().toLowerCase()).append(":   ");
        }
        return tittle.toString();
    }
}

