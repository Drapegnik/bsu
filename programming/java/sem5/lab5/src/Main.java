/**
 * Created by Drapegnik on 23.12.16.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.lang.reflect.Method;

public class Main extends JFrame implements ActionListener {
    public static void main(String[] args) {
        new Main("Math");
    }

    private JButton calc = new JButton("Calculate");
    private List list = new List();
    private Method[] data;

    public Main(String title) {
        super(title);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Container container = this.getContentPane();
        container.setLayout(new BoxLayout(container, 1));
        Box b = new Box(1);
        calc.addActionListener(this);
        b.add(list);
        b.add(calc);
        container.add(b);
        data = Math.class.getMethods();
        show(list, data);
//        pack();
        setSize(500, 500);
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == calc) {
            int ind = list.getSelectedIndex();
            if (ind != -1) {
                new CalcJDialog(this, "Calculate", data[ind]);
            } else {
                JOptionPane.showMessageDialog(this, "Select element!", "Error!", JOptionPane.PLAIN_MESSAGE);
            }
        }
    }

    private void show(List list, Method[] arr) {
        if (arr != null) {
            list.removeAll();
            for (Method m : arr) {
                if (m.toString().contains("static"))
                    list.add(m.toString());
            }
        } else {
            JOptionPane.showMessageDialog(this, "There are no elements!", "Error!", JOptionPane.PLAIN_MESSAGE);
        }

    }
}
