/**
 * Created by Drapegnik on 07.03.17.
 */

package app;

import app.backend.dbDriver;
import app.backend.sqlDriver;
import app.backend.xmlDriver;
import app.config.Options;
import app.models.Mark;
import app.models.Student;

import javax.xml.bind.ValidationException;
import java.rmi.RemoteException;
import java.rmi.registry.Registry;
import java.rmi.registry.LocateRegistry;
import java.rmi.server.UnicastRemoteObject;
import java.util.List;

/**
 * <p>Class wrapper on backend functional</p>
 * implements {@link RemoteService}
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class Server implements RemoteService {

    private dbDriver db;

    public Server(dbDriver db) {this.db = db;}

    @Override
    public String sayHello() throws RemoteException {
        return "Hello, world!";
    }

    @Override
    public List<Student> getStudents() throws RemoteException {
        return db.getStudents();
    }

    @Override
    public List<String> getBadStudentsIds() throws RemoteException {
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

    /**
     * <b>Main method</b>
     * <pre style="background-color: lightgray">{@code
     * Server obj = new Server();
     * RemoteService stub = (RemoteService) UnicastRemoteObject.exportObject(obj, 0);
     * Registry registry = LocateRegistry.getRegistry(host, port);
     * registry.bind(RemoteService.class.getSimpleName(), stub);
     * }</pre>
     *
     * @param args args
     */
    public static void main(String args[]) {
        int port = Integer.parseInt(System.getenv().get(Options.PORT_ENV_NAME));
        String host = System.getenv().get(Options.HOST_ENV_NAME);
        String dbType = System.getenv().get(Options.DB_TYPE_ENV_NAME);

        try {
            Server server;
            switch (dbType) {
                case Options.DB_SQL:
                    server = new Server(new sqlDriver());
                    break;
                case Options.DB_XML:
                    server = new Server(new xmlDriver());
                    break;
                default:
                    throw new ValidationException("Incorrect db type! Please set " + Options.DB_TYPE_ENV_NAME +
                            " env var to '" + Options.DB_SQL + "' or '" + Options.DB_XML + "'");
            }

            RemoteService stub = (RemoteService) UnicastRemoteObject.exportObject(server, 0);

            Registry registry = LocateRegistry.getRegistry(host, port);
            registry.bind(RemoteService.class.getSimpleName(), stub);

            System.err.println(dbType + " server ready");
        } catch (Exception ex) {
            System.err.println("Server exception: " + ex.toString());
            ex.printStackTrace();
        }
    }
}