/**
 * Created by Drapegnik on 08.03.17.
 */

import java.sql.*;
import java.util.ArrayList;
import java.util.Random;

/**
 * <p>Class for connecting to database</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class dbDriver {
    private Connection conn = null;
    private Statement stmt = null;
    private PreparedStatement pstmt = null;
    private String sql;

    /**
     * SQL requests
     */
    private static final String CREATE_STUDENT = "INSERT INTO " +
            Options.DB_NAME + "." + Student.class.getSimpleName() +
            " (id, s_name, s_group) VALUES(?, ?, ?)";

    private static final String CREATE_MARK = "INSERT INTO " +
            Options.DB_NAME + "." + Mark.class.getSimpleName() +
            " (id, subject, grade, studentId) VALUES(?, ?, ?, ?)";

    /**
     * Create new database connection
     *
     * @see Options#JDBC_DRIVER
     * @see Options#DB_URL
     * @see Options#DB_USER
     * @see Options#DB_PASS
     */
    public dbDriver() {
        try {
            Class.forName(Options.JDBC_DRIVER);
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(Options.DB_URL, Options.DB_USER, Options.DB_PASS);
            stmt = conn.createStatement();
            System.out.println("Successfully connect to " + Options.DB_URL);
        } catch (Exception se) {
            System.out.println("Some problem with db connection");
            se.printStackTrace();
            System.exit(1);
        }
    }

    /**
     * Create table
     *
     * @see Options#DB_NAME
     */
    private void createTable(String tableName, String sql) {
        System.out.println("Creating table...");

        try {
            stmt.executeUpdate(sql);
            System.out.println("Table '" + Options.DB_NAME + "." + tableName + "' created successfully.");
        } catch (Exception se) {
            se.printStackTrace();
        }
    }

    /**
     * Create {@link Student}s table
     *
     * @see dbDriver#createTable(String, String)
     * @see Options#DB_NAME
     */
    public void createStudentsTable() {
        String sql = "CREATE TABLE " + Options.DB_NAME + "." + Student.class.getSimpleName() +
                "(id VARCHAR(255) not NULL, " +
                " s_name VARCHAR(255), " +
                " s_group INTEGER, " +
                " PRIMARY KEY ( id ))";
        createTable(Student.class.getSimpleName(), sql);
    }

    /**
     * Create {@link Mark}s table
     *
     * @see dbDriver#createTable(String, String)
     * @see Options#DB_NAME
     */
    private void createMarkTable() {
        String sql = "CREATE TABLE " + Options.DB_NAME + "." + Mark.class.getSimpleName() +
                "(id VARCHAR(255) not NULL, " +
                " subject VARCHAR(255), " +
                " grade INTEGER, " +
                " studentId VARCHAR(255) not NULL, " +
                " PRIMARY KEY ( id ))";
        createTable(Mark.class.getSimpleName(), sql);
    }

    /**
     * Drop database if exist, and create new
     *
     * @see Options#DB_NAME
     */
    private void dropDB() {
        try {
            System.out.println("Drop database...");
            sql = "DROP DATABASE IF EXISTS " + Options.DB_NAME;
            stmt.executeUpdate(sql);

            System.out.println("Creating database...");
            sql = "CREATE DATABASE " + Options.DB_NAME;
            stmt.executeUpdate(sql);
            System.out.println("Database '" + Options.DB_NAME + "' created successfully.");
        } catch (Exception se) {
            se.printStackTrace();
        }
    }

    /**
     * Insert {@link Student} object into table
     *
     * @param student {@link Student} instance
     */
    public void createStudent(Student student) {
        try {
            stmt = conn.createStatement();
            pstmt = conn.prepareStatement(CREATE_STUDENT);
            pstmt.setString(1, student.getId());
            pstmt.setString(2, student.getName());
            pstmt.setInt(3, student.getGroup());
            pstmt.executeUpdate();
        } catch (Exception se) {
            se.printStackTrace();
        }
    }

    /**
     * Insert {@link Mark} object into table
     *
     * @param mark {@link Mark} instance
     */
    public void createMark(Mark mark) {
        try {
            stmt = conn.createStatement();
            pstmt = conn.prepareStatement(CREATE_MARK);
            pstmt.setString(1, mark.getId());
            pstmt.setString(2, mark.getSubject().toString());
            pstmt.setInt(3, mark.getGrade());
            pstmt.setString(4, mark.getStudentId());
            pstmt.executeUpdate();
        } catch (Exception se) {
            se.printStackTrace();
        }
    }

    /**
     * Fetch {@link Student}s data from {@link Options#STUDENTS_FILE_NAME}
     * Generate random {@link Mark}s with {@link Subject}s
     * Save all data into db
     *
     * @see dbDriver#createMark(Mark)
     * @see dbDriver#createStudent(Student)
     * @see Options#STUDENTS_FILE_NAME
     */
    public void initDB() {
        System.out.println("Init database...");
        ArrayList<Student> data = Student.readFromFile(Options.STUDENTS_FILE_NAME);
        Random random = new Random();

        for (Student student : data) {
            System.out.println('\t' + student.toString());
            createStudent(student);

            for (Subject subject : Subject.values()) {
                Mark mark = new Mark(subject, random.nextInt(10) + 1, student.getId());
                System.out.println('\t' + mark.toString());
                createMark(mark);
            }
            System.out.println();
        }
    }

    /**
     * Drop database if exist, and create new
     * Create all tables
     *
     * @see dbDriver#dropDB()
     * @see dbDriver#createStudentsTable()
     * @see dbDriver#createMarkTable()
     * @see Options#DB_NAME
     */
    public void createDB() {
        dropDB();
        createStudentsTable();
        createMarkTable();
    }

    private void close() {
        try {
            if (stmt != null)
                stmt.close();
        } catch (SQLException se2) {
            System.out.println(se2.getMessage());
        }

        try {
            if (conn != null)
                conn.close();
        } catch (SQLException se) {
            se.printStackTrace();
        }

        System.out.println("Close db connection... Goodbye!");
    }

    public static void main(String[] args) {
        dbDriver db = new dbDriver();
        db.createDB();
        db.initDB();
        db.close();
    }
}