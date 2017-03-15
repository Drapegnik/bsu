/**
 * Created by Drapegnik on 07.03.17.
 */

package common;

import backend.dbDriver;
import config.Options;
import models.Mark;
import models.Student;

import java.rmi.RemoteException;
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
import java.util.ArrayList;

public class Server implements RemoteService {

    private dbDriver db;

    public Server() {
        db = new dbDriver();
    }

    @Override
    public String sayHello() throws RemoteException {
        return "Hello, world!";
    }

    @Override
    public ArrayList<Student> getStudents() throws RemoteException {
        return db.getStudents();
    }

    @Override
    public ArrayList<String> getBadStudentsIds() throws RemoteException {
        return db.getBadStudentsIds();
    }

    @Override
    public void deleteStudent(String id) throws RemoteException {
        db.deleteStudent(id);
    }

    @Override
    public void addStudent(Student student) throws RemoteException {
        db.createStudent(student);
        for (Mark mark : student.getMarks()) {
            db.createMark(mark);
        }
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
        } catch (Exception ex) {
            System.err.println("Server exception: " + ex.toString());
            ex.printStackTrace();
        }
    }
}