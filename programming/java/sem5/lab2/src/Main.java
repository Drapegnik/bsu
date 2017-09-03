import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.ArrayList;
import java.util.Collection;
import java.util.TreeSet;

/**
 * Created by Drapegnik on 12/21/16.
 */
public class Main extends JFrame implements ActionListener {
    public static void main(String[] args) {
        new Main("Students");
    }

    protected static JLabel empty = new JLabel("");
    private JButton show = new JButton("Show");
    private JButton edit = new JButton("Edit");
    private JButton add = new JButton("Add");
    private JButton save = new JButton("Save");
    private JButton saveDb = new JButton("Save to DB");
    private JLabel label = new JLabel("Students:");
    private List list = new List();
    private List list2 = new List();
    private ArrayList<Student> data;
    private JMenuBar menuBar;
    private JMenu menu;
    private JMenuItem menuOpen;
    private JMenuItem menuSave;
    private JMenuItem menuAdd;
    private dbDriver db;

    public Main(String title) {
        super(title);
        setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent ev) {
                close();
            }
        });

        menuBar = new JMenuBar();
        menu = new JMenu("File");

        menuOpen = new JMenuItem("Open");
        menuOpen.setMnemonic(KeyEvent.VK_O);
        menuOpen.addActionListener(this);
        menu.add(menuOpen);

        menuSave = new JMenuItem("Save");
        menuSave.setMnemonic(KeyEvent.VK_S);
        menuSave.addActionListener(this);
        menu.add(menuSave);

        menuAdd = new JMenuItem("Add");
        menuAdd.setMnemonic(KeyEvent.VK_A);
        menuAdd.addActionListener(this);
        menu.add(menuAdd);

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

        edit.addActionListener(this);
        JPanel jPanel2 = new JPanel();
        jPanel2.add(edit);
        b2.add(jPanel2);

        add.addActionListener(this);
        JPanel jPanel3 = new JPanel();
        jPanel3.add(add);
        b2.add(jPanel3);

        save.addActionListener(this);
        JPanel jPanel4 = new JPanel();
        jPanel4.add(save);
        b2.add(jPanel4);

        saveDb.addActionListener(this);
        JPanel jPanel5 = new JPanel();
        jPanel4.add(saveDb);
        b2.add(jPanel5);

        show.addActionListener(this);
        JPanel jPanel1 = new JPanel();
        jPanel1.add(show);
        b2.add(jPanel1);

        container.add(b2);

        db = new dbDriver();
        data = db.readStudents();
        show(list, data);
        setSize(500, 200);
        //pack();
        setVisible(true);
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == show) {
            show(list, data);
            TreeSet<Student> set = new TreeSet<>(new MyComparator());

            for (Student student : data)
                if (checkDebt(student))
                    set.add(student);

            show(list2, set);
        } else if (e.getSource() == menuOpen) {

            data = Student.readFromFile(getFileName("Text files (.txt)", "txt", true));
            show(list, data);
            list2.removeAll();

        } else if (e.getSource() == menuSave || e.getSource() == save) {
            write(getFileName("Text files (.txt)", "txt", false));
        } else if (e.getSource() == saveDb) {
            db.writeStudents(data);
        } else if (e.getSource() == add || e.getSource() == menuAdd) {
            Student tempStudent = new Student();
            new EditJDialog(this, "add Student", tempStudent);

            if (!tempStudent.equals(new Student())) {
                data.add(tempStudent);
                show(list, data);
            }
        } else if (e.getSource() == edit) {
            int ind = list.getSelectedIndex();
            if (ind != -1) {
                new EditJDialog(this, "edit Student", data.get(ind));
                show(list, data);
            } else {
                JOptionPane.showMessageDialog(this, "Select element!", "Error!", JOptionPane.PLAIN_MESSAGE);
            }
        }
    }

    private void write(String filename) {
        try {
            FileOutputStream fos = new FileOutputStream(filename);
            ObjectOutputStream oos = new ObjectOutputStream(fos);

            oos.writeObject(data);
            oos.flush();

            oos.close();
            fos.close();
        } catch (IOException err) {
            JOptionPane.showMessageDialog(this, err, "Error!", JOptionPane.PLAIN_MESSAGE);
        } catch (NullPointerException err) {
        }
    }

    private void show(List list, Collection<Student> col) {
        if (col != null) {
            list.removeAll();
            for (Student el : col)
                list.add(el.toString());
        } else {
            JOptionPane.showMessageDialog(this, "There are no elements!", "Error!", JOptionPane.PLAIN_MESSAGE);
        }

    }

    private boolean checkDebt(Student student) {
        return (student.getMarkProg() < 4 || student.getMarkMath() < 4 || student.getMarkHistory() < 4);
    }

    private String getFileName(String filterName, String fileExt, Boolean ifOpen) {
        JFileChooser chooser = new JFileChooser();
        File workingDirectory = new File(System.getProperty("user.dir"));
        chooser.setCurrentDirectory(workingDirectory);
        FileNameExtensionFilter filter = new FileNameExtensionFilter(filterName, fileExt);
        chooser.setFileFilter(filter);
        if (ifOpen) {
            if (chooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION)
                return chooser.getSelectedFile().toString();
            else
                return null;
        } else {
            if (chooser.showSaveDialog(this) == JFileChooser.APPROVE_OPTION)
                return chooser.getSelectedFile().toString();
            else
                return null;
        }
    }

    void close() {
        setVisible(false);
        dispose();
        db.close();
    }

}
