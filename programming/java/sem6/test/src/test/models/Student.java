package test.models;

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
    private String id;
    private double averageGrade;
    private boolean isVillager;


    public Student() {
        this.name = "";
        this.id = UUID.randomUUID().toString();
        this.isVillager = false;
    }

    public Student(String name, int group, double averageGrade) {
        this();
        this.name = name;
        this.group = group;
        this.averageGrade = averageGrade;
    }

    public Student(String id, String name, int group, double averageGrade, boolean isVillager) {
        this(name, group, averageGrade, isVillager);
        this.id = id;
    }

    public Student(String name, int group, double averageGrade, boolean isVillager) {
        this(name, group, averageGrade);
        this.isVillager = isVillager;
    }

    public Student(Student o) {
        this.id = o.id;
        this.name = o.name;
        this.group = o.group;
        this.isVillager = o.isVillager;
        this.averageGrade = o.averageGrade;
    }

    public String getName() {return name;}

    public void setName(String name) {this.name = name;}

    public int getGroup() {return group;}

    public void setGroup(int group) {this.group = group;}

    public String getId() {return id;}

    public double getAverageGrade() {return averageGrade;}

    public void setAverageGrade(double averageGrade) {this.averageGrade = averageGrade;}

    public boolean getIsVillager() {return isVillager;}

    public void setIsVillager(boolean villager) {isVillager = villager;}

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
     * Method for init dummy students data
     *
     * @return {@link ArrayList} of {@link Student}s
     */
    public static ArrayList<Student> generateFakeData() {
        ArrayList<Student> data = new ArrayList<>();
        data.add(new Student("Perry Hodges", 1, 4.0));
        data.add(new Student("Patrick Richardson", 2, 5.0, true));
        data.add(new Student("Doug Evans", 3, 9.0));
        data.add(new Student("Cathy Russell", 4, 8.5));
        data.add(new Student("Cecil Murphy", 1, 10.0, true));
        data.add(new Student("Roberto Ball", 2, 6.7, true));
        data.add(new Student("Glenda Romero", 3, 2.1));
        data.add(new Student("Tomas King", 4, 4.5));
        data.add(new Student("Sophia Simpson", 1, 7.6));
        data.add(new Student("Wade Maxwell", 2, 4.3));
        return data;
    }
}

