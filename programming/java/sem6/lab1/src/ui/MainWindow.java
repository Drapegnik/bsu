/**
 * Created by Drapegnik on 15.03.17.
 */
package ui;

import backend.dbDriver;
import common.RemoteService;
import models.Student;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.Collection;

/**
 * <p>Main ui window for client</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class MainWindow extends JFrame implements ActionListener {
    private JLabel separator = new JLabel("                                                         ");
    private List studentsList = new List();
    private List badStudentsList = new List();
    private JButton getAll = new JButton("Get All");
    private JButton getBad = new JButton("Get Bad");
    private JButton addStudent = new JButton("Add Student");
    private JButton deleteStudent = new JButton("Delete Student");
    private ArrayList<Student> data = new ArrayList<>();
    private RemoteService rmi;

    public MainWindow(String title, RemoteService rmi) {
        super(title);
        this.rmi = rmi;
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);

        Container container = this.getContentPane();
        container.setLayout(new BoxLayout(container, 1));

        Box labelsBox = new Box(2);
        labelsBox.add(new JLabel("All students"));
        labelsBox.add(separator);
        labelsBox.add(new JLabel("Bad students"));
        container.add(labelsBox);

        Box listsBox = new Box(2);
        Box leftListBox = new Box(1);
        leftListBox.add(new JLabel(Student.getTittle()));
        leftListBox.add(studentsList);
        listsBox.add(leftListBox);
        Box rightListBox = new Box(1);
        rightListBox.add(new JLabel(Student.getTittle()));
        rightListBox.add(badStudentsList);
        listsBox.add(leftListBox);
        listsBox.add(rightListBox);
        container.add(listsBox);

        Box buttonsBox = new Box(2);
        getAll.addActionListener(this);
        buttonsBox.add(getAll);
        getBad.addActionListener(this);
        buttonsBox.add(getBad);
        addStudent.addActionListener(this);
        buttonsBox.add(addStudent);
        deleteStudent.addActionListener(this);
        buttonsBox.add(deleteStudent);
        container.add(buttonsBox);

        checkConnection();
        pack();
        setSize(getWidth(), 500);
        setLocation(200, 200);
        setVisible(true);
    }

    private void checkConnection() {
        try {
            System.out.println(rmi.sayHello());
        } catch (Exception e) {
            System.err.println("RMI exception: " + e.toString());
            e.printStackTrace();
        }
    }

    public void actionPerformed(ActionEvent e) {
    }

    /**
     * Method for render {@link Student}s data into {@link java.awt.List}
     *
     * @param studentsList {@link java.awt.List} output
     * @param collection   <pre>{@code Collection<Student>}</pre> {@link Student}'s objects
     */
    private void render(List studentsList, Collection<Student> collection) {
        if (collection == null) {
            JOptionPane.showMessageDialog(this, "There are no elements!", "Error!", JOptionPane.PLAIN_MESSAGE);
            return;
        }
        studentsList.removeAll();
        for (Student st : collection) {
            studentsList.add(st.formattedToString());
        }
    }
}
