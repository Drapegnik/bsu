import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.*;

/**
 * Created by Drapegnik on 9/12/16.
 */
public class Main extends JFrame implements ActionListener {
    public static void main(String[] args) {
        new Main("Notepad");
    }

    private final static String newline = "\n";
    private final static String WARNING_TEXT = "Current changes doesn't save. Are you want to continue?";
    private final static String PUNCT_MARKS = ",.:;«»?!—()'\" \n";
    private JButton fix = new JButton("Fix");
    private JButton save = new JButton("Save");
    private JButton undo = new JButton("Undo");
    private JTextArea textArea = new JTextArea(20, 80);
    private JMenuBar menuBar;
    private JMenu menu;
    private JMenuItem menuOpen;
    private JMenuItem menuSave;
    private String text;

    public Main(String title) {
        super(title);
//        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent ev) {
                boolean isSave = checkChanges();
                int warning = checkWarning(isSave);

                if (isSave || warning == 0) {
                    System.out.println("closing");
                    dispose();
                }
            }
        });
        setResizable(false);

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

        menuBar.add(menu);
        setJMenuBar(menuBar);

        Container container = this.getContentPane();
        container.setLayout(new BoxLayout(container, 1));
        Box b = new Box(1);

        JPanel jPanel1 = new JPanel();
        jPanel1.add(textArea);
        b.add(jPanel1);
        b.add(new JScrollPane(textArea, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED));


        fix.addActionListener(this);
        save.addActionListener(this);
        undo.addActionListener(this);
        JPanel jPanel2 = new JPanel();
        jPanel2.add(fix);
        jPanel2.add(save);
        jPanel2.add(undo);
        b.add(jPanel2);
        container.add(b);

        read(new File("data.txt"));
//        setSize(1000, 500);
        pack();
        setVisible(true);
    }


    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == fix) {
            fix();
        } else if (e.getSource() == undo) {
            undo();
        } else if (e.getSource() == menuOpen) {

            boolean isSave = checkChanges();
            int warning = checkWarning(isSave);

            if (isSave || warning == 0) {
                read(getFile("Text files (.txt)", "txt", true));
                pack();
            }
        } else if (e.getSource() == menuSave || e.getSource() == save) {
            write(getFile("Text files (.txt)", "txt", false));
        }
    }

    private void undo() {
        textArea.setText(text);
    }

    private void fix() {
        textArea.setText(normalizePunctuation(removeExtraSpaces(textArea.getText())));
    }

    private String removeExtraSpaces(String text) {
        StringBuffer sb = new StringBuffer(text);
        int start = sb.indexOf("  ");
        while (start > -1) {

            int end = start;
            while (sb.charAt(end) == ' ') {
                end++;
            }

            sb.replace(start, end, " ");
            start = sb.indexOf("  ", end);
        }
        return sb.toString();
    }

    private String normalizePunctuation(String text) {
        StringTokenizer st = new StringTokenizer(text, PUNCT_MARKS, true);
        StringBuffer sb = new StringBuffer();
        String openBrackets = "«(";

        String prevToken = "";
        while (st.hasMoreTokens()) {
            String token = st.nextToken();

            if (token.equals(" ")) {
                if (!openBrackets.contains(prevToken) && !prevToken.equals(" ")) {
                    sb.append(token);
                }
            } else if (openBrackets.contains(token)) {
                if (!prevToken.equals(" ") && !prevToken.equals("\n")) {
                    sb.append(" ");
                }
                sb.append(token);
            } else if (token.equals("—")) {
                if (!prevToken.equals(" "))
                    sb.append(" ");
                sb.append(token).append(" ");
                token = " ";
            } else if (token.equals("\n")) {
                sb.append(token);
            } else if (PUNCT_MARKS.contains(token)) {
                if (prevToken.equals(" ")) {
                    sb.deleteCharAt(sb.length() - 1);
                }
                sb.append(token).append(" ");
                token = " ";
            } else {
                sb.append(token);
            }
            prevToken = token;
        }
        return sb.toString();

    }

    private void read(File file) {
        Scanner sc = null;
        try {
            sc = new Scanner(file);
            textArea.setText("");
            while (sc.hasNextLine())
                textArea.append(sc.nextLine() + newline);

            text = textArea.getText();
        } catch (FileNotFoundException err) {
            JOptionPane.showMessageDialog(this, err, "Error!", JOptionPane.PLAIN_MESSAGE);
        } catch (NullPointerException ex) {
        } finally {
            if (sc != null)
                sc.close();
        }
    }

    private void write(File file) {
        PrintWriter wr = null;
        try {
            wr = new PrintWriter(file);
            wr.write(textArea.getText());
            text = textArea.getText();
        } catch (IOException ex) {
            JOptionPane.showMessageDialog(this, ex, "Error!", JOptionPane.PLAIN_MESSAGE);
        } catch (NullPointerException ex) {
        } finally {
            if (wr != null)
                wr.close();
        }
    }

    private boolean checkChanges() {
        return text.equals(textArea.getText());
    }

    private int checkWarning(boolean isSave) {
        int warning = 1;
        if (!isSave)
            warning = JOptionPane.showConfirmDialog(this, WARNING_TEXT, "Warning!!!", JOptionPane.YES_NO_CANCEL_OPTION);
        return warning;
    }

    private File getFile(String filterName, String fileExt, Boolean ifOpen) {
        JFileChooser chooser = new JFileChooser();
        File workingDirectory = new File(System.getProperty("user.dir"));
        chooser.setCurrentDirectory(workingDirectory);
        FileNameExtensionFilter filter = new FileNameExtensionFilter(filterName, fileExt);
        chooser.setFileFilter(filter);
        if (ifOpen) {
            if (chooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION)
                return chooser.getSelectedFile();
            else
                return null;
        } else {
            if (chooser.showSaveDialog(this) == JFileChooser.APPROVE_OPTION)
                return chooser.getSelectedFile();
            else
                return null;
        }
    }
}
