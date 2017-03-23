/**
 * Created by Drapegnik on 08.03.17.
 */
package app.backend;

import app.models.*;
import app.config.Options;

import java.sql.*;
import java.text.MessageFormat;
import java.util.*;

/**
 * <p>Class for connecting to sql database</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class sqlDriver extends dbDriver {
    private Connection conn = null;
    private Statement stmt = null;
    private PreparedStatement pstmt = null;
    private ResultSet res = null;
    private String sql;

    private static String StudentsTable = Student.class.getSimpleName();
    private static String MarksTable = Mark.class.getSimpleName();
    /**
     * SQL requests
     */
    private static final String CREATE_STUDENT = MessageFormat.format(
            "INSERT INTO {0} (id, s_name, s_group) VALUES(?, ?, ?);", StudentsTable);

    private static final String CREATE_MARK = MessageFormat.format(
            "INSERT INTO {0} (id, subject, grade, studentId) VALUES(?, ?, ?, ?);", MarksTable);

    private static final String GET_STUDENTS = MessageFormat.format(
            "SELECT * FROM {0} INNER JOIN {1} ON {1}.studentId={0}.id;", StudentsTable, MarksTable);

    private static final String GET_BAD_STUDENTS = MessageFormat.format(
            "SELECT {0}.id, {0}.s_name, COUNT(*) as bad_marks_count FROM {0}" +
                    " INNER JOIN {1} ON {0}.id={1}.studentId" +
                    " WHERE {1}.grade < 4 GROUP BY {0}.id" +
                    " HAVING COUNT(*) > 2;", StudentsTable, MarksTable);

    private static final String DELETE_STUDENT = MessageFormat.format(
            "DELETE st, mrk FROM {0} st" +
                    " INNER JOIN {1} mrk ON st.id=mrk.studentId" +
                    " WHERE st.id=?;", StudentsTable, MarksTable);

    /**
     * Wrapper on {@link sqlDriver#connect()}
     *
     * @see sqlDriver#connect()
     */
    public sqlDriver() {
        connect();
    }

    /**
     * Create new database connection
     *
     * @see Options#JDBC_DRIVER
     * @see Options#DB_URL
     * @see Options#DB_USER
     * @see Options#DB_PASS
     */
    private void connect() {
        try {
            Class.forName(Options.JDBC_DRIVER);
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(Options.DB_URL + Options.DB_NAME, Options.DB_USER, Options.DB_PASS);
            stmt = conn.createStatement();
            System.out.println("Successfully connect to " + conn.getMetaData().getURL());
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
     * @see sqlDriver#createTable(String, String)
     * @see Options#DB_NAME
     */
    private void createStudentsTable() {
        String sql = "CREATE TABLE " + StudentsTable +
                "(id VARCHAR(255) not NULL, " +
                " s_name VARCHAR(255), " +
                " s_group INTEGER, " +
                " PRIMARY KEY ( id ))";
        createTable(Student.class.getSimpleName(), sql);
    }

    /**
     * Create {@link Mark}s table
     *
     * @see sqlDriver#createTable(String, String)
     * @see Options#DB_NAME
     */
    private void createMarkTable() {
        String sql = "CREATE TABLE " + MarksTable +
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
    @Override
    public void createStudent(Student student) {
        try {
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
     * Remove {@link Student} and all his {@link Mark}s from db
     *
     * @param id {@link Student#id}
     */
    @Override
    public void deleteStudent(String id) {
        try {
            System.out.println("Delete student...");
            pstmt = conn.prepareStatement(DELETE_STUDENT);
            pstmt.setString(1, id);
            pstmt.executeUpdate();
            System.out.println("Successfully delete student with id=" + id);
        } catch (Exception se) {
            se.printStackTrace();
        }
    }

    /**
     * Select all {@link Student}'s objects from db
     *
     * @return <pre>{@code ArrayList<Student>}</pre> {@link Student}'s objects
     */
    @Override
    public ArrayList<Student> getStudents() {
        System.out.println("Select students...");
        ArrayList<Student> data = new ArrayList<>();
        try {
            res = stmt.executeQuery(GET_STUDENTS);
            HashMap<String, Student> map = new HashMap<>();
            while (res.next()) {
                String id = res.getString("id");
                Student st = map.get(id);
                if (st == null) {
                    st = new Student(id, res.getString("s_name"), Integer.parseInt(res.getString("s_group")));
                }

                st.addMark(new Mark(res.getString("subject"), Integer.parseInt(res.getString("grade")), id));
                map.put(id, st);
                if (Options.DEBUG) {
                    System.out.println("\t#" + res.getRow()
                            + "\t" + res.getString("s_name")
                            + "\t" + res.getString("subject")
                            + "\t" + res.getString("grade")
                            + "\t" + res.getString("id"));
                }
            }

            for (Map.Entry<String, Student> entry : map.entrySet()) {
                Student st = entry.getValue();
                data.add(st);
                if (Options.DEBUG) {
                    System.out.println(st);
                }
            }
            System.out.println("Successfully select " + data.size() + " students.");

        } catch (Exception se) {
            se.printStackTrace();
        }
        return data;
    }

    /**
     * Select all {@link Student}'s objects from db
     * that have 3 and more bad (1, 2, 3) marks
     *
     * @return <pre>{@code ArrayList<String>} students_ids</pre>
     */
    @Override
    public ArrayList<String> getBadStudentsIds() {
        System.out.println("Select bad students...");
        ArrayList<String> data = new ArrayList<>();
        try {
            res = stmt.executeQuery(GET_BAD_STUDENTS);
            while (res.next()) {
                data.add(res.getString("id"));
                if (Options.DEBUG) {
                    System.out.println("\t#" + res.getRow()
                            + "\t" + res.getString("s_name")
                            + "\t" + res.getString("bad_marks_count")
                            + "\t" + res.getString("id"));
                }
            }
            System.out.println("Successfully select " + data.size() + " bad students.");
        } catch (Exception se) {
            se.printStackTrace();
        }
        return data;
    }

    /**
     * Insert {@link Mark} object into table
     *
     * @param mark {@link Mark} instance
     */
    @Override
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
     * @see sqlDriver#createMark(Mark)
     * @see sqlDriver#createStudent(Student)
     * @see Options#STUDENTS_FILE_NAME
     */
    private void initDB() {
        System.out.println("Init database...");
        ArrayList<Student> data = Student.readFromFile(Options.STUDENTS_FILE_NAME);
        Random random = new Random();

        for (Student student : data) {
            System.out.println('\t' + student.shortToString());
            createStudent(student);

            for (Subject subject : Subject.values()) {
                Mark mark = new Mark(subject, random.nextInt(10) + 1, student.getId());
                System.out.println('\t' + mark.toString());
                createMark(mark);
            }
            System.out.println();
        }
    }

    private void dumpStudentsIntoFule() {
        Student.writeInFile(Options.STUDENTS_FILE_NAME, getStudents());
    }

    /**
     * Drop database if exist, and create new
     * Create all tables
     *
     * @see sqlDriver#dropDB()
     * @see sqlDriver#createStudentsTable()
     * @see sqlDriver#createMarkTable()
     * @see Options#DB_NAME
     */
    private void createDB() {
        dropDB();
        connect();
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
            if (pstmt != null)
                pstmt.close();
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
        sqlDriver db = new sqlDriver();
        db.createDB();
        db.initDB();
        db.getStudents();
        db.close();
//        Student.writeInFile(app.config.Options.STUDENTS_FILE_NAME, Student.generateFakeData());
    }
}