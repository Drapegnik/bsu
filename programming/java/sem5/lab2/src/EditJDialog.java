import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.zip.DataFormatException;

/**
 * Created by Drapegnik on 27.11.15.
 */

public class EditJDialog extends JDialog implements ActionListener {
    private JButton ok = new JButton("<html><i><font color=\"green\">ok</font></i></html>");
    private JLabel labelName = new JLabel("  Name:");
    private JLabel labelGroup = new JLabel("  Group:");
    private JLabel labelMath = new JLabel("  Math:");
    private JLabel labelProg = new JLabel("  Prog:");
    private JLabel labelHistory = new JLabel("  History:");

    private JTextField inputName = new JTextField("", 5);
    private JTextField inputGroup = new JTextField("", 5);
    private JTextField inputMath = new JTextField("", 5);
    private JTextField inputProg = new JTextField("", 5);
    private JTextField inputHistory = new JTextField("", 5);
    private Student student;

    public EditJDialog(JFrame parent, String title, Student o) {
        super(parent, title, true);
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        //setResizable(false);
        this.student = o;

        Container container = this.getContentPane();
        container.setLayout(new GridLayout(6, 2));

        container.add(labelName);
        inputName.setText(student.getName());
        container.add(inputName);

        container.add(labelGroup);
        inputGroup.setText(student.getGroup() + "");
        container.add(inputGroup);

        container.add(labelMath);
        inputMath.setText(student.getMarkMath() + "");
        container.add(inputMath);

        container.add(labelProg);
        inputProg.setText(student.getMarkProg() + "");
        container.add(inputProg);

        container.add(labelHistory);
        inputHistory.setText(student.getMarkHistory() + "");
        container.add(inputHistory);

        container.add(Main.empty);
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
                student.setGroup(Integer.parseInt(inputGroup.getText()));
                student.setMarkMath(Integer.parseInt(inputMath.getText()));
                student.setMarkProg(Integer.parseInt(inputProg.getText()));
                student.setMarkHistory(Integer.parseInt(inputHistory.getText()));
                setVisible(false);
            } catch (NumberFormatException err) {
                JOptionPane.showMessageDialog(this, err, "Error!", JOptionPane.PLAIN_MESSAGE);
            } catch (DataFormatException err) {
                JOptionPane.showMessageDialog(this, err.getMessage(), "Error!", JOptionPane.PLAIN_MESSAGE);
            }
        }
    }
}