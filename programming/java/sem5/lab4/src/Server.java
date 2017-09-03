import java.io.*;
import java.net.*;
import java.util.*;

/**
 * Created by Drapegnik on 12.12.16.
 */
public class Server {

    public Server() {
        serverThreads = new ArrayList<>();
        ShutdownServerHook shutdownHook = new ShutdownServerHook(this);
        Runtime.getRuntime().addShutdownHook(shutdownHook);
    }

    public static void main(String[] args) throws FileNotFoundException {
        Server server = new Server();

        StringBuilder text = new StringBuilder();

        Scanner scanner = new Scanner(new File(INPUT_FILE_NAME));
        while (scanner.hasNext()) {
            text.append(scanner.next()).append(" ");
        }
        scanner.close();

        try {
            server.serverSocket = new ServerSocket(PORT);
            System.out.println("Server: start at " + InetAddress.getLocalHost() + " and listen " + PORT + " port");
            System.out.println("Server: read text '" + text + "'");
            int i = 0;

            while (!server.serverSocket.isClosed()) {
                ServerThread thread = new ServerThread(server.serverSocket.accept(), server.serverSocket, text.toString(), i++);
                synchronized (server.serverThreads) {
                    server.serverThreads.add(thread);
                }
                thread.start();
            }
        } catch (Exception err) {
            System.out.println(getErrorMessage(err.toString()));
        }
    }

    final static int PORT = 8000;
    private final static String INPUT_FILE_NAME = "input.txt";
    private static final String ANSI_RESET = "\u001B[0m";
    private static final String ANSI_RED = "\u001B[31m";
    private List<ServerThread> serverThreads;
    private ServerSocket serverSocket;
    final static String CLIENT_DISCONNECT_CODE = "#%%EXIT%%#";
    final static String CLOSE_CODE = "#%%CLOSE%%#";
    final static String START_CODE = "#%%START%%#";

    static String getErrorMessage(String err) {
        return ANSI_RED + err + ANSI_RESET;
    }

    void close() throws IOException {
        for (int i = 0; i < serverThreads.size(); i++) {
            if (!serverThreads.get(i).getState().toString().equals("TERMINATED")) {
                serverThreads.get(i).close();
            }
        }
    }

}

class ShutdownServerHook extends Thread {
    private Server server;

    public ShutdownServerHook(Server server) {
        this.server = server;
    }

    public void run() {
        try {
            server.close();
            System.out.println(Server.getErrorMessage("Server is shutting down"));
        } catch (IOException err) {
            System.out.println(err.getMessage());
        }

    }
}
