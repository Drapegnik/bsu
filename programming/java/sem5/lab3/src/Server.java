import java.net.InetAddress;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Drapegnik on 16.10.16.
 */
public class Server {

    public static void main(String[] args) {
        Server server = new Server();
        try {
            server.serverSocket = new ServerSocket(PORT);
            System.out.println("Server start at " + InetAddress.getLocalHost() + " and listen " + PORT + " port");
            while (true) {
                Socket socket = server.serverSocket.accept();
                ServerThread thread;
                int number = -1;

                for (int i = 0; i < server.serverThreads.size(); i++)
                    if (server.serverThreads.get(i).getState().toString().equals("TERMINATED")) {
                        number = i;
                        break;
                    }

                if (number != -1) {
                    thread = new ServerThread(socket, number + 1);
                    server.serverThreads.set(number, thread);
                } else {
                    number = server.serverThreads.size();
                    thread = new ServerThread(socket, number + 1);
                    server.serverThreads.add(thread);
                }
                thread.start();
            }
        } catch (Exception err) {
            System.out.println(getErrorMessage(err.toString()));
        }
    }

    public Server() {
        serverThreads = new ArrayList<>();
        ShutdownServerHook shutdownHook = new ShutdownServerHook(this);
        Runtime.getRuntime().addShutdownHook(shutdownHook);
    }

    final static int PORT = 8000;
    final static int OK_CODE = 200;
    final static int NOT_FOUND_CODE = 404;
    final static int SERVER_ERROR = 500;
    final static String CLIENT_DISCONNECT_CODE = "#%%EXIT%%#";
    final static String CLOSE_CODE = "#%%CLOSE%%#";
    final static String GET_CODE = "#%%GET%%#";
    final static String END_CODE = "#%%END%%#";
    static final String ANSI_RESET = "\u001B[0m";
    static final String ANSI_CYAN = "\u001B[36m";
    static final String ANSI_GREEN = "\u001B[32m";
    static final String ANSI_RED = "\u001B[31m";
    private List<ServerThread> serverThreads;
    private ServerSocket serverSocket;

    static String getErrorMessage(String err) {
        return ANSI_RED + err + ANSI_RESET;
    }

    static String cyan(String text) {
        return ANSI_CYAN + text + ANSI_RESET;
    }

    void close() {
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
        server.close();
        System.out.println(Server.getErrorMessage("Server is shutting down"));

    }
}
