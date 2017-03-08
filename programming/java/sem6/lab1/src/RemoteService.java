/**
 * Created by Drapegnik on 07.03.17.
 */

import java.rmi.Remote;
import java.rmi.RemoteException;


public interface RemoteService extends Remote {
    String sayHello() throws RemoteException;
}