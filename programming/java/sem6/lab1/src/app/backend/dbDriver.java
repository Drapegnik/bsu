/**
 * Created by Drapegnik on 23.03.17.
 */
package app.backend;


import app.models.Mark;
import app.models.Student;

import java.util.List;

abstract public class dbDriver {
    public abstract List<Student> getStudents();

    public abstract List<String> getBadStudentsIds();

    public abstract void deleteStudent(String id);

    public abstract void createStudent(Student student);

    public abstract void createMark(Mark mark);
}
