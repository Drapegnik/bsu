import java.awt.List;
import java.io.*;
import java.awt.event.*;
import java.awt.*;
import java.util.*;
import javax.swing.*;
import javax.swing.event.ListSelectionEvent;
import javax.swing.event.ListSelectionListener;
import javax.swing.filechooser.FileNameExtensionFilter;

/**
 * Created by Drapegnik on 27.11.15.
 */
public class MyJFrame extends JFrame implements ActionListener {
    public static void main(String[] args) {
        new MyJFrame("Students");
    }

    protected static JLabel empty = new JLabel("");
    private JButton show = new JButton("Show");
    private JButton edit = new JButton("Edit");
    private JButton add = new JButton("Add");
    private JLabel label = new JLabel("Students:");
    private List list = new List();
    private List list2 = new List();
    private ArrayList<Student> a;
    private JMenuBar menuBar;
    private JMenu menu;
    private JMenuItem menuItem;

    public MyJFrame(String title) {
        super(title);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //setResizable(false);

        menuBar = new JMenuBar();
        menu = new JMenu("File");

        menuItem = new JMenuItem("Open");
        menuItem.setMnemonic(KeyEvent.VK_O);
        menuItem.addActionListener(this);
        menu.add(menuItem);
        menuBar.add(menu);
        setJMenuBar(menuBar);

        Box b = new Box(2);

        Container container = this.getContentPane();
        container.setLayout(new BoxLayout(container, 1));
        JPanel jPanel = new JPanel();
        jPanel.add(label);

        b.add(jPanel);
        b.add(list);
        b.add(list2);
        container.add(b);

        Box b2 = new Box(2);

        show.addActionListener(this);
        JPanel jPanel1 = new JPanel();
        jPanel1.add(show);
        b2.add(jPanel1);

        edit.addActionListener(this);
        JPanel jPanel2 = new JPanel();
        jPanel2.add(edit);
        b2.add(jPanel2);

        add.addActionListener(this);
        JPanel jPanel3 = new JPanel();
        jPanel3.add(add);
        b2.add(jPanel3);

        container.add(b2);

        read("data.txt");
        show(list, a);
        setSize(450, 180);
        //pack();
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == show) {
            show(list, a);
            TreeSet<Student> set1 = new TreeSet<>(new MyComparator());
            TreeSet<Student> set2 = new TreeSet<>(new MyComparator());

            for (Student el : a)
                if (set1.contains(el))
                    set2.add(el);
                else
                    set1.add(el);

            show(list2, set2);
        } else if (e.getSource() == menuItem) {
            JFileChooser chooser = new JFileChooser();
            FileNameExtensionFilter filter = new FileNameExtensionFilter("Text files", "txt");
            chooser.setFileFilter(filter);
            File workingDirectory = new File(System.getProperty("user.dir"));
            chooser.setCurrentDirectory(workingDirectory);
            if (chooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION) {
                read(chooser.getSelectedFile().getName());
                show(list, a);
                list2.removeAll();
            }

        } else if (e.getSource() == add) {
            Student tempStudent = new Student();
            new EditJDialog(this, "add Student", tempStudent);

            if (!tempStudent.equals(new Student())) {
                a.add(tempStudent);
                show(list, a);
            }
        } else if (e.getSource() == edit) {
            int ind = list.getSelectedIndex();
            if (ind != -1) {
                new EditJDialog(this, "edit Student", a.get(ind));
                show(list, a);
            } else {
                JOptionPane.showMessageDialog(this, "Select element!", "Error!", JOptionPane.PLAIN_MESSAGE);
            }
        }
    }

    private void read(String filename) {
        Scanner sc = null;
        try {
            sc = new Scanner(new FileReader(filename));
            a = new ArrayList<>();
            while (sc.hasNext())
                a.add(new Student(sc.next(), sc.nextInt(), sc.nextInt(), sc.nextInt()));
        } catch (FileNotFoundException err) {
            JOptionPane.showMessageDialog(this, err, "Error!", JOptionPane.PLAIN_MESSAGE);
        } finally {
            if (sc != null)
                sc.close();
        }
    }

    private void show(List list, Collection<Student> a) {
        if (a != null) {
            list.removeAll();
            for (Student el : a)
                list.add(el.toString());
        } else {
            JOptionPane.showMessageDialog(this, "There are no elements!", "Error!", JOptionPane.PLAIN_MESSAGE);
        }

    }
}
