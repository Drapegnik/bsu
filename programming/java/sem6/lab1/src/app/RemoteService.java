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

    ArrayList<Student> getStudents() throws RemoteException;

    ArrayList<String> getBadStudentsIds() throws RemoteException;

    void deleteStudent(String id) throws RemoteException;

    void addStudent(Student student) throws RemoteException;
}