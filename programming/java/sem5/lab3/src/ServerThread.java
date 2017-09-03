import java.io.*;
import java.net.Socket;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.concurrent.TimeUnit;
import java.util.stream.Stream;

/**
 * Created by Drapegnik on 16.10.16.
 */
public class ServerThread extends Thread {

    private PrintStream res;
    private BufferedReader req;
    private int number;
    private boolean isListen = true;

    public ServerThread(Socket socket, int number) throws IOException {
        this.number = number;
        res = new PrintStream(socket.getOutputStream());
        req = new BufferedReader(new InputStreamReader(socket.getInputStream()));
        res.println(number);
        print("New connection");
    }

    public void run() {
        while (isListen) {
            try {
                String message = req.readLine();
                if (message.equals(Server.GET_CODE)) {
                    String path = req.readLine();
                    print(Server.cyan("GET ") + path);
                    res.println(Server.OK_CODE);

                    print("Start sending file");
                    try (Stream<String> stream = Files.lines(Paths.get(path))) {
                        stream.forEach((string) -> {
                            res.println(string);
                            try {
                                TimeUnit.SECONDS.sleep(1);
                            } catch (InterruptedException e) {
                            }
                        });
                    }
                    res.println(Server.END_CODE);
                    print("File send!");
                } else if (message.equals(Server.CLIENT_DISCONNECT_CODE)) {
                    disconnect();
                }
            } catch (IOException err) {
                System.out.println(Server.getErrorMessage(err.toString()));
                res.println(Server.NOT_FOUND_CODE);
            }
        }
    }

    private void print(String message) {
        System.out.println(message + Server.cyan(" -> ") + "(Client#" + number + ")");
    }

    void disconnect() {
        isListen = false;
        try {
            if (req != null) {
                req.close();
            }
            if (res != null) {
                res.close();
            }
        } catch (IOException err) {
            System.out.println(Server.getErrorMessage(err.toString()));
        } finally {
            this.interrupt();
            print("Disconnect from server");
        }
    }

    void close() {
        print("Disconnect from server");
        res.println(Server.CLOSE_CODE);
    }
}
