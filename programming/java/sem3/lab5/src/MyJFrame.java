import java.awt.event.*;
import java.awt.*;
import java.io.IOException;
import javax.swing.*;

/**
 * Created by Drapegnik on 27.11.15.
 */
public class MyJFrame extends JFrame implements ActionListener {
    protected static JLabel empty = new JLabel("");
    private JButton show = new JButton("Show series");
    private JButton edit = new JButton("Edit series");
    private JTextField input = new JTextField("output.txt", 5);
    private JLabel label = new JLabel("  FileName:");
    private JRadioButton radio1 = new JRadioButton("Liner");
    private JRadioButton radio2 = new JRadioButton("Exponential");
    private JCheckBox check = new JCheckBox("Write on file", false);
    private Liner a;
    private Exponential b;

    public MyJFrame(String title, Liner a, Exponential b) {
        super(title);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        setVisible(true);
        this.a = a;
        this.b = b;

        Container container = this.getContentPane();
        container.setLayout(new GridLayout(4, 2));
        container.add(label);
        container.add(input);
        ButtonGroup group = new ButtonGroup();
        group.add(radio1);
        group.add(radio2);
        container.add(radio1);
        radio1.setSelected(true);
        container.add(radio2);
        container.add(check);
        container.add(empty);
        show.addActionListener(this);
        container.add(show);
        edit.addActionListener(this);
        container.add(edit);

        pack();
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == show) {
            String title = radio1.isSelected() ? radio1.getText() : radio2.getText();
            String message = radio1.isSelected() ? a.toString() : b.toString();

            try {
                if (check.isSelected())
                    if (radio1.isSelected())
                        a.save(input.getText());
                    else
                        b.save(input.getText());
                    JOptionPane.showMessageDialog(this, message, title, JOptionPane.PLAIN_MESSAGE);
            } catch (IOException ex) {
                JOptionPane.showMessageDialog(this, ex, "Error!", JOptionPane.PLAIN_MESSAGE);
            }
        } else if (e.getSource() == edit)
            new EditJDialog(this, radio1.isSelected() ? radio1.getText() : radio2.getText(), radio1.isSelected() ? a : b);
    }

}
