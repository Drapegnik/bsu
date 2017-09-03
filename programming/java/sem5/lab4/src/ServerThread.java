import java.io.DataInputStream;
import java.io.DataOutputStream;
import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ServerThread extends Thread {
    Socket clientSocket;
    ServerSocket serverSocket;
    String text;
    private DataInputStream inputStream;
    private DataOutputStream outputStream;
    private int number;
    EventSource eventSource;
    Object objectForTimeout;
    private boolean isListen = true;

    public ServerThread(Socket clientSocket, ServerSocket serverSocket, String text, int number) throws IOException {
        super();
        this.text = text;
        this.clientSocket = clientSocket;
        this.serverSocket = serverSocket;
        this.number = number;

        objectForTimeout = new Object();
        inputStream = new DataInputStream(clientSocket.getInputStream());
        outputStream = new DataOutputStream(clientSocket.getOutputStream());
        eventSource = new EventSource();
        eventSource.addListener(new Listener() {

            @Override
            public void countPercent(Event e) {
                Double p = (e.getCurrentIndex() + 1.0) * 100 / e.getNumberOfSymbols();

                try {
                    outputStream.writeUTF(p.intValue() + "");
                    synchronized (objectForTimeout) {
                        objectForTimeout.wait(300);
                    }
                } catch (Exception err) {
                    System.out.println(err.getMessage());
                }
            }
        });

        outputStream.writeUTF(number + "");
        print("New connection");
    }

    @Override
    public void run() {
        try {
            while (isListen) {
                String message = inputStream.readUTF();
                if (message.equals(Server.START_CODE)) {
                    print("Start sending file");
                    for (int i = 0; i < text.length(); i++) {
                        send(i);
                    }
                    print("File send!");
                } else if (message.equals(Server.CLIENT_DISCONNECT_CODE)) {
                    disconnect();
                }
            }
        } catch (Exception err) {
            System.out.println("Server: Client disconnected.");
        }
    }

    public void send(int i) throws IOException {
        String symbol = text.charAt(i) + "";
        outputStream.writeUTF(symbol);
        eventSource.handleEvent(i, text.length());
    }

    private void print(String message) {
        System.out.println(message + " -> (Client#" + number + ")");
    }

    void disconnect() {
        isListen = false;
        try {
            if (inputStream != null) {
                inputStream.close();
            }
            if (outputStream != null) {
                outputStream.close();
            }
        } catch (IOException err) {
            System.out.println(Server.getErrorMessage(err.toString()));
        } finally {
            this.interrupt();
            print("Disconnect from server");
        }
    }

    void close() throws IOException {
        print("Disconnect from server");
        outputStream.writeUTF(Server.CLOSE_CODE);
    }
}



