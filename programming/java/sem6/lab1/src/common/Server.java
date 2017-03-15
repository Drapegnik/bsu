/**
 * Created by Drapegnik on 07.03.17.
 */

package common;

import backend.dbDriver;
import config.Options;

import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;

public class Server implements RemoteService {

    private dbDriver db;

    public Server() {
        db = new dbDriver();
    }

    public String sayHello() {
        return "Hello, world!";
    }

    public static void main(String args[]) {
        int port = Integer.parseInt(System.getenv().get(Options.PORT_ENV_NAME));
        String host = System.getenv().get(Options.HOST_ENV_NAME);

        try {
            Server obj = new Server();
            RemoteService stub = (RemoteService) UnicastRemoteObject.exportObject(obj, 0);

            // Bind the remote object's stub in the registry
            Registry registry = LocateRegistry.getRegistry(host, port);
            registry.bind(RemoteService.class.getSimpleName(), stub);

            System.err.println("Server ready");
        } catch (Exception e) {
            System.err.println("Server exception: " + e.toString());
            e.printStackTrace();
        }
    }
}