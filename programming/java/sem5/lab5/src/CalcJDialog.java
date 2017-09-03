/**
 * Created by Drapegnik on 23.12.16.
 */

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.lang.reflect.Method;
import java.lang.reflect.Parameter;
import java.util.ArrayList;
import java.util.zip.DataFormatException;

public class CalcJDialog extends JDialog implements ActionListener {

    private JButton exec = new JButton("<html><i><font color=\"green\">execute</font></i></html>");
    private Method method;
    private ArrayList<JTextField> args = new ArrayList<>();
    private JTextField result = new JTextField("");


    public CalcJDialog(JFrame parent, String title, Method m) {
        super(parent, title, true);
        setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        //setResizable(false);
        this.method = m;
        exec.addActionListener(this);

        Container container = this.getContentPane();
        container.setLayout(new GridLayout(method.getParameterCount() + 2, 2));

        for (Parameter arg : method.getParameters()) {
            JTextField text = new JTextField();
            args.add(text);
            container.add(new Label("   " + arg.toString()));
            container.add(text);
        }
        container.add(new Label("   result:"));
        container.add(result);
        container.add(new Label(""));
        container.add(exec);

        pack();
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == exec) {
            try {
                Object[] arguments = new Object[args.size()];
                int id = 0;
                String temp;

                for (JTextField jtf : args) {
                    if (jtf.getText().equals(""))
                        throw new DataFormatException("Set arguments!");

                    temp = method.getParameters()[id].getType().toString();
                    if (temp.equals("int") || temp.equals("class java.lang.Integer"))
                        arguments[id] = Integer.parseInt(jtf.getText());
                    else if (temp.equals("long") || temp.equals("class java.lang.Long"))
                        arguments[id] = Long.parseLong(jtf.getText());
                    else if (temp.equals("double") || temp.equals("class java.lang.Double"))
                        arguments[id] = Double.parseDouble(jtf.getText());
                    else if (temp.equals("float") || temp.equals("class java.lang.Float"))
                        arguments[id] = Float.parseFloat(jtf.getText());
                    else arguments[id] = jtf.getText();
                    id++;
                }

                Object res = method.invoke(null, arguments);
                result.setText(res.toString());

            } catch (NumberFormatException err) {
                JOptionPane.showMessageDialog(this, err, "Error!", JOptionPane.PLAIN_MESSAGE);
            } catch (Exception err) {
                JOptionPane.showMessageDialog(this, err.getMessage(), "Error!", JOptionPane.PLAIN_MESSAGE);
            }
        }
    }
}