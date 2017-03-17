/**
 * Created by Drapegnik on 07.03.17.
 */

package app;

import app.models.Student;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.ArrayList;

/**
 * <p>Interface for RMI</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public interface RemoteService extends Remote {
    String sayHello() throws RemoteException;

    /**
     * SELECT ALL
     * @return <pre> {@code ArrayList<Student>}</pre> {@link Student}s list
     * @throws RemoteException rmi exception
     */
    ArrayList<Student> getStudents() throws RemoteException;

    /**
     * SELECT WHERE
     * @return <pre> {@code ArrayList<String>}</pre> {@link Student}s ids list
     * @throws RemoteException rmi exception
     */
    ArrayList<String> getBadStudentsIds() throws RemoteException;

    /**
     * DELETE
     * @param id {@link Student} id
     * @throws RemoteException rmi exception
     */
    void deleteStudent(String id) throws RemoteException;

    /**
     * CREATE
     * @param student {@link Student} object
     * @throws RemoteException rmi exception
     */
    void addStudent(Student student) throws RemoteException;
}