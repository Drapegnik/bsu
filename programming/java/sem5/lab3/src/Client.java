import javax.swing.*;
import javax.swing.filechooser.FileNameExtensionFilter;
import java.awt.*;
import java.awt.event.*;
import java.io.File;
import java.io.*;
import java.net.InetAddress;
import java.net.Socket;
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReadWriteLock;
import java.util.concurrent.locks.ReentrantReadWriteLock;

/**
 * Created by Drapegnik on 16.10.16.
 */
public class Client extends JFrame implements ActionListener {

    public static void main(String[] args) {

        Client client = new Client();
        while (client.listen) {
            client.readLock.lock();
            try {
                if (!client.listen)
                    break;
                client.message = client.res.readLine();
                if (client.message.equals(Server.CLOSE_CODE)) {
                    JOptionPane.showMessageDialog(client, "Server is shutting down", "Warning!", JOptionPane.PLAIN_MESSAGE);
                    client.close();
                }
            } catch (IOException err) {
                System.out.println(Server.getErrorMessage(err.toString()));
                JOptionPane.showMessageDialog(client, err, "Error!", JOptionPane.PLAIN_MESSAGE);
                client.close();
            } finally {
                client.readLock.unlock();
            }
        }
    }

    private final ReadWriteLock readWriteLock = new ReentrantReadWriteLock();
    private final Lock readLock = readWriteLock.readLock();
    private final Lock writeLock = readWriteLock.writeLock();
    private String message;
    private boolean listen;


    private final static String newline = "\n";
    private JButton browse = new JButton("browse");
    private JTextArea textArea = new JTextArea(20, 40);
    private JMenuBar menuBar;
    private JMenu menu;
    private JMenuItem menuOpen;

    private Socket socket;
    private BufferedReader res;
    private PrintStream req;
    private int number;

    public Client() {
        super();
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
        menuBar.add(menu);
        setJMenuBar(menuBar);

        Container container = this.getContentPane();
        container.setLayout(new BoxLayout(container, BoxLayout.Y_AXIS));
        Box b = new Box(1);

        JPanel jPanel1 = new JPanel();
        jPanel1.add(textArea);
        b.add(jPanel1);
        b.add(new JScrollPane(textArea, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS));


        browse.addActionListener(this);
        JPanel jPanel2 = new JPanel();
        jPanel2.add(browse);
        b.add(jPanel2);
        container.add(b);

        ShutdownClientHook shutdownHook = new ShutdownClientHook(this);
        Runtime.getRuntime().addShutdownHook(shutdownHook);
        listen = true;
        try {
            socket = new Socket(InetAddress.getLocalHost(), Server.PORT);
            req = new PrintStream(socket.getOutputStream());
            res = new BufferedReader(new InputStreamReader(socket.getInputStream()));

            this.number = Integer.parseInt(res.readLine());
            print("successfully " + Server.cyan("connect") + " to " + InetAddress.getLocalHost() + ":" + Server.PORT + newline);
            this.setTitle("Client#" + number);
            pack();
            setVisible(true);
        } catch (Exception err) {
            JOptionPane.showMessageDialog(this, err, "Error!", JOptionPane.PLAIN_MESSAGE);
        }
    }

    public void actionPerformed(ActionEvent e) {
        if (e.getSource() == menuOpen || e.getSource() == browse) {
            String path = getFilePath("Text files (.txt)", "txt", true);
            print(Server.cyan("GET ") + path);
            req.println(Server.GET_CODE);
            req.println(path);
            int code;
            writeLock.lock();
            try {
                code = Integer.parseInt(message);
                print(code);
            } finally {
                writeLock.unlock();
            }

            if (code == Server.OK_CODE) {
                String line= message;

                while (!line.equals(Server.END_CODE)) {
                    if (!line.equals(code + "")) {
                        print(Server.cyan("receive ") + "'" + line + "'" + newline);
                        textArea.append(line + newline);
                        textArea.update(textArea.getGraphics());
                    }

                    writeLock.lock();
                    try {
                        line = message;
                    } finally {
                        writeLock.unlock();
                    }
                }
            }
        }
    }

    private String getFilePath(String filterName, String fileExt, Boolean ifOpen) {
        JFileChooser chooser = new JFileChooser();
        File workingDirectory = new File(System.getProperty("user.dir"));
        chooser.setCurrentDirectory(workingDirectory);
        FileNameExtensionFilter filter = new FileNameExtensionFilter(filterName, fileExt);
        chooser.setFileFilter(filter);
        if (ifOpen) {
            if (chooser.showOpenDialog(this) == JFileChooser.APPROVE_OPTION)
                return chooser.getSelectedFile().getAbsolutePath();
            else
                return null;
        } else {
            if (chooser.showSaveDialog(this) == JFileChooser.APPROVE_OPTION)
                return chooser.getSelectedFile().getAbsolutePath();
            else
                return null;
        }
    }

    void print(String message) {
        System.out.print("Client#" + number + ": " + message);
    }

    private void print(Integer code) {
        String col = (code == Server.OK_CODE) ? Server.ANSI_GREEN : Server.ANSI_RED;
        System.out.println(" " + col + code + Server.ANSI_RESET);
    }

    void close() {
        try {
            req.println(Server.CLIENT_DISCONNECT_CODE);
            req.close();
            res.close();
            listen = false;
            socket.close();
            setVisible(false);
            dispose();
        } catch (IOException err) {
            System.out.println(Server.getErrorMessage(err.toString()));
        }
    }
}

class ShutdownClientHook extends Thread {
    private Client client;

    public ShutdownClientHook(Client client) {
        this.client = client;
    }

    public void run() {
        client.close();
        client.print(Server.cyan("disconnect ") + "from server");
    }
}
