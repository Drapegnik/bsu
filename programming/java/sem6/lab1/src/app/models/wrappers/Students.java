/**
 * Created by Drapegnik on 23.03.17.
 */
package app.models.wrappers;

import app.models.Student;

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import java.util.ArrayList;

@XmlRootElement
public class Students {
    private ArrayList<Student> data;

    public Students() {
        data = null;
    }

    public Students(ArrayList<Student> data) {
        this.data = data;
    }

    @XmlElement(name = "student")
    public ArrayList<Student> getData() {
        return data;
    }

    public void setData(ArrayList<Student> data) {
        this.data = data;
    }
}
