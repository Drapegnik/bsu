import java.awt.event.*;
import java.awt.*;
import java.util.zip.DataFormatException;
import javax.swing.*;

/**
 * Created by Drapegnik on 27.11.15.
 */
public class EditJDialog extends JDialog implements ActionListener {
    private JButton ok = new JButton("<html><i><font color=\"green\">ok</font></i></html>");
    private JLabel labelName = new JLabel("  Name:");
    private JLabel labelCourse = new JLabel("  Course:");
    private JLabel labelGroup = new JLabel("  Group:");
    private JLabel labelNumber = new JLabel("  Number:");
    private JTextField inputName = new JTextField("", 5);
    private JTextField inputCourse = new JTextField("", 5);
    private JTextField inputGroup = new JTextField("", 5);
    private JTextField inputNumber = new JTextField("", 5);
    private Student student;

    public EditJDialog(JFrame parent, String title, Student o) {
        super(parent, title, true);
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        //setResizable(false);
        this.student = o;

        Container container = this.getContentPane();
        container.setLayout(new GridLayout(5, 2));

        container.add(labelName);
        inputName.setText(student.getName());
        container.add(inputName);

        container.add(labelNumber);
        inputNumber.setText(student.getNumber() + "");
        container.add(inputNumber);

        container.add(labelCourse);
        inputCourse.setText(student.getCourse() + "");
        container.add(inputCourse);

        container.add(labelGroup);
        inputGroup.setText(student.getGroup() + "");
        container.add(inputGroup);

        container.add(MyJFrame.empty);
        ok.addActionListener(this);
        container.add(ok);
        pack();
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == ok) {
            try {
                if (inputName.getText().equals(""))
                    throw new DataFormatException("Set name!");
                student.setName(inputName.getText());
                student.setNumber(Integer.parseInt(inputNumber.getText()));
                student.setCourse(Integer.parseInt(inputCourse.getText()));
                student.setGroup(Integer.parseInt(inputGroup.getText()));
                setVisible(false);   // это норма?
            } catch (NumberFormatException err) {
                JOptionPane.showMessageDialog(this, err, "Error!", JOptionPane.PLAIN_MESSAGE);
            } catch (DataFormatException err) {
                JOptionPane.showMessageDialog(this, err.getMessage(), "Error!", JOptionPane.PLAIN_MESSAGE);
            }
        }
    }
}