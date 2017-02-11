import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.image.BufferedImage;
import java.io.*;
import java.util.*;

/**
 * Created by Drapegnik on 21.12.15.
 */
public class MainFrame extends JFrame implements ActionListener {
    public static void main(String[] args) {
        new MainFrame("exam");
    }

    //private JPanel central;
    private JButton show = new JButton("Show firms!");
    //private JButton edit = new JButton("Edit");
    private JButton add = new JButton("Color");
    private ArrayList<Cleaner> a;
    private DefaultListModel rightlistModel;
    private DefaultListModel leftlistModel;
    private TreeSet<Cleaner> set;

    public MainFrame(String title) {
        super(title);
        try {
            UIManager.setLookAndFeel(UIManager.getSystemLookAndFeelClassName());
            //UIManager.setLookAndFeel(UIManager.getCrossPlatformLookAndFeelClassName());
        } catch (Exception e) {
            JOptionPane.showMessageDialog(this, "Setting appropriate Look and Feel failed.");
        }
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());
        menuInit();
        pictInit();
        listInit();
        buttInit();
        pack();
        setVisible(true);
    }

    void menuInit() {
        JMenuBar menuBar;
        JMenu menu;
        JMenuItem menuItem;

        menuBar = new JMenuBar();
        menu = new JMenu("File");

        menuItem = new JMenuItem("Open");
        menuItem.setMnemonic(KeyEvent.VK_O);
        menuItem.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                JFileChooser chooser = new JFileChooser();
                FileNameExtensionFilter filter = new FileNameExtensionFilter("Text files", "txt");
                chooser.setFileFilter(filter);
                File workingDirectory = new File(System.getProperty("user.dir"));
                chooser.setCurrentDirectory(workingDirectory);
                if (chooser.showOpenDialog(MainFrame.this) == JFileChooser.APPROVE_OPTION) {
                    read(chooser.getSelectedFile());
                }
            }
        });
        menu.add(menuItem);
        menuBar.add(menu);
        setJMenuBar(menuBar);
    }

    void pictInit() {
        JPanel central = new JPanel();
        // central.setLayout(new BorderLayout());
        JLabel img = new JLabel(new ImageIcon("img/space.jpeg"));
        central.add(img);
        add(central, BorderLayout.CENTER);
    }

    void listInit() {
        JLabel leftlabel = new JLabel("Input list:");
        JLabel rightlabel = new JLabel("Sorted list:");

        leftlistModel = new DefaultListModel();
        JList leftlist = new JList(leftlistModel);
        leftlist.setFont(new Font("ITALIC", Font.ITALIC, 15));
        rightlistModel = new DefaultListModel();
        JList rightlist = new JList(rightlistModel);
        rightlist.setFont(new Font("ITALIC", Font.ITALIC, 15));

//        for (String el : DATA1)
//            leftlistModel.addElement(el);
//
//        for (String el : DATA2)
//            rightlistModel.addElement(el);

        Box left = new Box(1);
        left.add(leftlabel);
        left.add(leftlist);
        left.add(new JScrollPane(leftlist, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED),
                BorderLayout.WEST);
        add(left, BorderLayout.WEST);

        Box right = new Box(1);
        right.add(rightlabel);
        right.add(rightlist);
        right.add(new JScrollPane(rightlist, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED),
                BorderLayout.EAST);
        add(right, BorderLayout.EAST);
    }

    void buttInit() {
        show.addActionListener(this);
        add.addActionListener(this);
        //edit.addActionListener(this);
        Box horizontal = new Box(2);
        horizontal.add(show);
        //  horizontal.add(edit);
        horizontal.add(add);
        add(horizontal, BorderLayout.SOUTH);
    }

    private void read(File file) {
        Scanner sc = null;
        try {
            sc = new Scanner(file);
            a = new ArrayList<>();
            if (sc.nextInt() == 1) {
                while (sc.hasNext()) {
                    a.add(new RobotCleaner(sc.next(), sc.next(), sc.next(), sc.nextInt(),
                            sc.nextInt() == 1 ? true : false));
                }
                show(leftlistModel, a);
                Collections.sort(a, new MyComparator());
                show(rightlistModel, a);
            } else {
                while (sc.hasNext()) {
                    a.add(new WashCleaner(sc.next(), sc.next(), sc.next(), sc.nextInt(),
                            sc.nextInt()));
                }
                show(leftlistModel, a);
                Collections.sort(a, new MyComparator());
                show(rightlistModel, a);
            }
        } catch (FileNotFoundException err) {
            JOptionPane.showMessageDialog(this, err, "Error!", JOptionPane.PLAIN_MESSAGE);
        } finally {
            if (sc != null)
                sc.close();
        }
    }

    private void show(DefaultListModel model, Collection<Cleaner> a) {
        if (a != null) {
            model.removeAllElements();
            for (Cleaner el : a)
                model.addElement(el);
        } else {
            JOptionPane.showMessageDialog(this, "There are no elements!", "Error!", JOptionPane.PLAIN_MESSAGE);
        }

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == add) {
            ModalDialog dlg = (new ModalDialog(this, "add"));
            if (dlg.isOk()) {
                String color = dlg.getColor();
                System.out.println(color);
                ArrayList <String> b = new ArrayList<>();
                for (Cleaner el : a)
                    if (el.getColor().equals(color))
                        b.add(el.getFirm());

                rightlistModel.removeAllElements();
                for (String el : b)
                    rightlistModel.addElement(el);

            }
        } else if (e.getSource() == show) {
            set = new TreeSet<>(new Comparator() {
                @Override
                public int compare(Object o1, Object o2) {
                    Cleaner to1 = (Cleaner) o1;
                    Cleaner to2 = (Cleaner) o2;
                    return to1.getFirm().compareTo(to2.getFirm());
                }
            });
            set.addAll(a);
            ArrayList<String> b = new ArrayList<>();
            rightlistModel.removeAllElements();
            for (Cleaner el : set)
                rightlistModel.addElement(el.getFirm());
        }
    }
}
