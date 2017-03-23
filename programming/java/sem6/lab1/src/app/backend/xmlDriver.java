/**
 * Created by Drapegnik on 23.03.17.
 */
package app.backend;

import app.models.Mark;
import app.models.Student;

import java.util.List;

public class xmlDriver extends dbDriver {
    /**
     * Get all {@link Student}'s objects from storage
     *
     * @return <pre>{@code List<Student>}</pre> {@link Student}'s objects
     */
    @Override
    public List<Student> getStudents() {
        return null;
    }

    /**
     * Get all {@link Student}'s objects from storage
     * that have 3 and more bad (1, 2, 3) marks
     *
     * @return <pre>{@code List<String>} students_ids</pre>
     */
    @Override
    public List<String> getBadStudentsIds() {
        return null;
    }

    /**
     * Delete {@link Student} and all his {@link Mark}s from storage
     *
     * @param id {@link Student#id}
     */
    @Override
    public void deleteStudent(String id) {

    }

    /**
     * Create and save {@link Student} object in storage
     *
     * @param student {@link Student} instance
     */
    @Override
    public void createStudent(Student student) {

    }

    /**
     * Create {@link Mark} object in storage
     *
     * @param mark {@link Mark} instance
     */
    @Override
    public void createMark(Mark mark) {

    }
}
