/**
 * Created by Drapegnik on 07.03.17.
 */

package common;

import models.Student;

import java.rmi.Remote;
import java.rmi.RemoteException;
import java.util.ArrayList;


public interface RemoteService extends Remote {
    String sayHello() throws RemoteException;

    ArrayList<Student> getStudents() throws RemoteException;

    ArrayList<String> getBadStudentsIds() throws RemoteException;

    void deleteStudent(String id) throws RemoteException;

    void addStudent(Student student) throws RemoteException;
}