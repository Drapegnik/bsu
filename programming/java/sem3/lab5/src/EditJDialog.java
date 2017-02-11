import java.awt.event.*;
import java.awt.*;
import javax.swing.*;

/**
 * Created by Drapegnik on 27.11.15.
 */
public class EditJDialog extends JDialog implements ActionListener {
    private JButton ok = new JButton("<html><i><font color=\"green\">ok</font></i></html>");
    private JLabel labelN = new JLabel("  n:");
    private JLabel labelFirst = new JLabel("  First:");
    private JLabel labelStep = new JLabel("  Step:");
    private JTextField inputN = new JTextField("", 5);
    private JTextField inputFirst = new JTextField("", 5);
    private JTextField inputStep = new JTextField("", 5);
    private Series q;

    public EditJDialog(JFrame parent, String title, Series q) {
        super(parent, title);
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        setResizable(false);
        setVisible(true);
        this.q = q;

        Container container = this.getContentPane();
        container.setLayout(new GridLayout(4, 2));
        container.add(labelN);
        inputN.setText(Double.toString(q.getN()));
        container.add(inputN);
        container.add(labelFirst);
        inputFirst.setText(Double.toString(q.getFirst()));
        container.add(inputFirst);
        container.add(labelStep);
        inputStep.setText(Double.toString(q.getStep()));
        container.add(inputStep);
        container.add(MyJFrame.empty);
        ok.addActionListener(this);
        container.add(ok);
        pack();
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == ok) {
            q.setFirst(Double.parseDouble(inputFirst.getText()));
            q.setStep(Double.parseDouble(inputStep.getText()));
            q.setN(Double.parseDouble(inputN.getText()));
            setVisible(false);   // это норма?
        }
    }
}