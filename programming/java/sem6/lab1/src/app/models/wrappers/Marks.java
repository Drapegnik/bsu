/**
 * Created by Drapegnik on 23.03.17.
 */
package app.models.wrappers;

import app.models.Mark;

import javax.xml.bind.annotation.XmlElement;
import javax.xml.bind.annotation.XmlRootElement;
import java.io.Serializable;
import java.util.ArrayList;

@XmlRootElement
public class Marks implements Serializable {
    private ArrayList<Mark> data;

    public Marks() {data = new ArrayList<>();}

    public Marks(ArrayList<Mark> data) {this.data = data;}

    @XmlElement(name = "mark")
    public ArrayList<Mark> getData() {return data;}

    public void setData(ArrayList<Mark> data) {this.data = data;}

    public void addElement(Mark mark) {this.data.add(mark);}
}
