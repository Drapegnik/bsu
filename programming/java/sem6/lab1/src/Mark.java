/**
 * Created by Drapegnik on 08.03.17.
 */

/**
 * <p>Class for storing info about {@link Student}'s marks</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class Mark {
    private String subject;
    /**
     * Link with student {@link Student#id}
     */
    private String studentId;

    public Mark(String subject, String studentId) {
        this.subject = subject;
        this.studentId = studentId;
    }

    public String getSubject() {
        return subject;
    }

    public String getStudentId() {
        return studentId;
    }
}
