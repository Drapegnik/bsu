import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.zip.DataFormatException;

/**
 * Created by Drapegnik on 21.12.15.
 */
public class ModalDialog extends JDialog {
    private JButton ok = new JButton("<html><i><font color=\"green\">ok</font></i></html>");
    private JLabel label1 = new JLabel("  Color:");
    private JLabel label2 = new JLabel("  2:");
    private JLabel label3 = new JLabel("  3:");
    private JLabel label4 = new JLabel("  4:");
    private JTextField input1 = new JTextField("", 5);
    private JTextField input2 = new JTextField("", 5);
    private JTextField input3 = new JTextField("", 5);
    private JTextField input4 = new JTextField("", 5);
    private static final JLabel EMPTY = new JLabel("");

    private boolean isOk;
    private String color;

    public String getColor() {
        return color;
    }

    public boolean isOk() {
        return isOk;
    }

    public ModalDialog(JFrame parent, String title) {
        super(parent, title, true);
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);

        isOk = false;

        Container container = this.getContentPane();
        container.setLayout(new GridLayout(2, 2));

        container.add(label1);
        input1.setText("blueва");
        container.add(input1);

        container.add(EMPTY);
        ok.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                if (e.getSource() == ok) {
                    try {
                        if (input1.getText().equals(""))
                            throw new DataFormatException("Set color!");
                        isOk = true;
                        color = input1.getText();
                        setVisible(false);
                    } catch (NumberFormatException err) {
                        JOptionPane.showMessageDialog(ModalDialog.this, err, "Error!",
                                JOptionPane.PLAIN_MESSAGE);
                    } catch (DataFormatException err) {
                        JOptionPane.showMessageDialog(ModalDialog.this, err.getMessage(), "Error!",
                                JOptionPane.PLAIN_MESSAGE);
                    }
                }
            }
        });
        container.add(ok);
        pack();
        setVisible(true);
    }
}
