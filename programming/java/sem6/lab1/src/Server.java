/**
 * Created by Drapegnik on 07.03.17.
 */

import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;
import java.util.Map;

public class Server implements Hello {

    public Server() {
    }

    public String sayHello() {
        return "Hello, world!";
    }

    public static void main(String args[]) {
        int port = Integer.parseInt(System.getenv().get("RMI_PORT"));

        try {
            Server obj = new Server();
            Hello stub = (Hello) UnicastRemoteObject.exportObject(obj, 0);

            // Bind the remote object's stub in the registry
            Registry registry = LocateRegistry.getRegistry(port);
            registry.bind("Hello", stub);

            System.err.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}