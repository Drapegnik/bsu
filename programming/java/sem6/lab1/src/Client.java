/**
 * Created by Drapegnik on 07.03.17.
 */

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.ObjectOutputStream;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.util.ArrayList;

public class Client {

    private Client() {
    }

    public static void main(String[] args) {
        int port = Integer.parseInt(System.getenv().get(Options.PORT_ENV_NAME));
        String host = System.getenv().get(Options.HOST_ENV_NAME);

        try {
            Registry registry = LocateRegistry.getRegistry(host, port);
            RemoteService stub = (RemoteService) registry.lookup(RemoteService.class.getSimpleName());
            String response = stub.sayHello();
            System.out.println("response: " + response);
        } catch (Exception e) {
            System.err.println("Client exception: " + e.toString());
            e.printStackTrace();
        }
    }
}