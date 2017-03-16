/**
 * Created by Drapegnik on 15.03.17.
 */

package app.ui;

import app.models.Mark;
import app.models.Student;
import app.models.Subject;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.HashMap;
import java.util.Map;
import java.util.zip.DataFormatException;

public class NewStudentDialog extends JDialog implements ActionListener {
    private JButton add = new JButton("<html><i><font color=\"green\">add</font></i></html>");

    private JTextField inputName = new JTextField("", 5);
    private JTextField inputGroup = new JTextField("", 5);
    private HashMap<Subject, JTextField> marks;
    private Student student;

    public NewStudentDialog(JFrame parent, String title, Student student) {
        super(parent, title, true);
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        marks = new HashMap<>();
        this.student = student;

        Container container = this.getContentPane();
        container.setLayout(new GridLayout(Subject.values().length + 3, 2));

        container.add(new JLabel("  name:"));
        container.add(inputName);

        container.add(new JLabel("  group:"));
        container.add(inputGroup);

        for (Subject sub : Subject.values()) {
            container.add(new JLabel("  " + sub.toString().toLowerCase() + ":"));
            JTextField input = new JTextField();
            marks.put(sub, input);
            container.add(input);
        }
        container.add(new JLabel(""));
        add.addActionListener(this);
        container.add(add);
        pack();
        Double x = parent.getLocation().getX();
        Double y = parent.getLocation().getY();
        setLocation(x.intValue() + 20, y.intValue() + 20);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == add) {
            try {
                if (inputName.getText().equals("")) {
                    throw new DataFormatException("Set name!");
                }
                student.setName(inputName.getText());
                student.setGroup(Integer.parseInt(inputGroup.getText()));
                for (Map.Entry<Subject, JTextField> entry : marks.entrySet()) {
                    int grade = Integer.parseInt(entry.getValue().getText());
                    if (grade < 1 || grade > 10) {
                        throw new DataFormatException("Set grades from [1, 10]!");
                    }
                    student.addMark(new Mark(entry.getKey(), grade, student.getId()));
                }
                System.out.println(student);
                setVisible(false);
            } catch (NumberFormatException err) {
                JOptionPane.showMessageDialog(this, err, "Error!", JOptionPane.PLAIN_MESSAGE);
            } catch (DataFormatException err) {
                JOptionPane.showMessageDialog(this, err.getMessage(), "Error!", JOptionPane.PLAIN_MESSAGE);
            }
        }
    }
}