import java.awt.event.*;
import java.io.*;
import java.awt.*;
import java.net.*;
import javax.swing.*;

/**
 * Created by Drapegnik on 12.12.16.
 */
class Client extends JFrame implements Runnable {

    public static void main(String[] args) throws ClassNotFoundException, IOException {
        new Thread(new Client()).start();
    }

    private static final long serialVersionUID = 1L;
    private Font font = new Font("Verdana", Font.PLAIN, 20);
    private JTextArea textArea;
    private JProgressBar progressBar = new JProgressBar();
    private JButton button;
    private Socket socket = new Socket(InetAddress.getLocalHost(), Server.PORT);
    private DataOutputStream outputStream = new DataOutputStream(socket.getOutputStream());
    private DataInputStream inputStream = new DataInputStream(socket.getInputStream());
    private int number;
    private Component client;
    private boolean isListen = true;

    public Client() throws ClassNotFoundException, IOException {
        super();

        client = this;

        setDefaultCloseOperation(WindowConstants.DO_NOTHING_ON_CLOSE);
        addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent ev) {
                close();
            }
        });

        Container container = this.getContentPane();
        container.setLayout(new BoxLayout(container, BoxLayout.Y_AXIS));
        Box b = new Box(1);

        JPanel jPanel1 = new JPanel();
        textArea = new JTextArea();
        textArea.setFont(font);
        textArea.setPreferredSize(new Dimension(400, 400));
        textArea.setLineWrap(true);
        jPanel1.add(textArea);
        b.add(jPanel1);
        b.add(new JScrollPane(textArea, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS, JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS));

        progressBar.setStringPainted(true);
        progressBar.setMinimum(0);
        progressBar.setMaximum(100);
        progressBar.setStringPainted(true);

        JPanel jPanel2 = new JPanel();
        jPanel2.add(progressBar);
        b.add(jPanel2);

        button = new JButton("Run");
        button.setFont(font);

        button.addActionListener(new ActionListener() {

            public void actionPerformed(ActionEvent arg0) {
                try {
                    textArea.setText("");
                    progressBar.setValue(0);
                    outputStream.writeUTF(Server.START_CODE);
                } catch (IOException e) {
                    System.out.println(e.getMessage());
                    JOptionPane.showMessageDialog(client, "Server was closed", "Error!", JOptionPane.PLAIN_MESSAGE);
                    close();
                }
            }
        });

        JPanel jPanel3 = new JPanel();
        jPanel3.add(button);
        b.add(jPanel3);

        container.add(b);
        pack();

        ShutdownClientHook shutdownHook = new ShutdownClientHook(this);
        Runtime.getRuntime().addShutdownHook(shutdownHook);

        this.number = Integer.parseInt(inputStream.readUTF());
        print("successfully connect to " + InetAddress.getLocalHost() + ":" + Server.PORT + '\n');
        this.setTitle("Client#" + number);

        this.setVisible(true);
        closeWindow();
    }

    public void closeWindow() {
        this.setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
        this.addWindowListener(new java.awt.event.WindowAdapter() {
            public void windowClosing(java.awt.event.WindowEvent windowEvent) {
                try {
                    outputStream.writeUTF("Socket closed");
                    inputStream.close();
                    outputStream.close();
                    socket.close();
                } catch (Exception err) {
                    System.out.println(err.getMessage());
                    JOptionPane.showMessageDialog(client, "Socket closed", "Error!", JOptionPane.PLAIN_MESSAGE);
                    close();
                } finally {
                    System.exit(0);
                }
            }
        });
    }

    void print(String message) {
        System.out.print("Client#" + number + ": " + message);
    }

    void close() {
        try {
            outputStream.writeUTF(Server.CLIENT_DISCONNECT_CODE);
            inputStream.close();
            outputStream.close();
            isListen = false;
            socket.close();
            setVisible(false);
            dispose();
        } catch (IOException err) {
            System.out.println(Server.getErrorMessage(err.toString()));
        }
    }

    @Override
    public void run() {
        while (isListen) {
            try {
                if (inputStream.available() > 0) {
                    String symbol = inputStream.readUTF();
                    textArea.append(symbol);
                    String percent = inputStream.readUTF();
                    progressBar.setValue(Integer.parseInt(percent));
                }
            } catch (Exception err) {
                System.out.println(err.getClass());
                JOptionPane.showMessageDialog(client, "Socket closed", "Error!", JOptionPane.PLAIN_MESSAGE);
                close();
                break;
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
            client.print("disconnect from server");
        }
    }
}


