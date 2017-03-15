/**
 * Created by Drapegnik on 15.03.17.
 */
package ui;

import models.Student;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

/**
 * <p>Main ui window for client</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class MainWindow extends JFrame implements ActionListener {
    public static void main(String[] args) {new MainWindow("Students");}

    private JLabel allLabel = new JLabel("All students:");
    private JLabel badLabel = new JLabel("Bad students:");
    private JLabel separator = new JLabel("                                            ");
    private List studentsList = new List();
    private List badStudentsList = new List();
    private JButton getAll = new JButton("Get All");
    private JButton getBad = new JButton("Get Bad");
    private JButton addStudent = new JButton("Add Student");
    private JButton deleteStudent = new JButton("Delete Student");

    public MainWindow(String title) {
        super(title);
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);

        Container container = this.getContentPane();
        container.setLayout(new BoxLayout(container, 1));

        Box labelsBox = new Box(2);
        labelsBox.add(allLabel);
        labelsBox.add(separator);
        labelsBox.add(badLabel);
        container.add(labelsBox);

        Box listsBox = new Box(2);
        listsBox.add(studentsList);
        listsBox.add(badStudentsList);
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

        setSize(800, 500);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
    }
}
