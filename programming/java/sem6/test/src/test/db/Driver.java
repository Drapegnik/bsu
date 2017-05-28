package test.db;

/**
 * Created by Drapegnik on 5/25/17.
 */

import test.config.Options;
import test.models.Student;

import java.sql.*;
import java.text.MessageFormat;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;
import java.util.Random;

/**
 * <p>Class for connecting to database</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class Driver {
    private Connection conn = null;
    private Statement stmt = null;
    private PreparedStatement pstmt = null;
    private ResultSet res = null;
    private String sql;

    private static String StudentsTable = Student.class.getSimpleName();

    /**
     * SQL requests
     */
    private static final String CREATE_STUDENT = MessageFormat.format(
            "INSERT INTO {0} (id, s_name, s_group, s_average, s_is_villager) VALUES(?, ?, ?, ?, ?);", StudentsTable);
    private static final String GET_STUDENTS = MessageFormat.format(
            "SELECT * FROM {0}", StudentsTable);
    private static final String GET_STUDENTS_COUNT = MessageFormat.format(
            "SELECT COUNT(id) as size FROM {0}", StudentsTable);

    /**
     * Wrapper on {@link Driver#connect()}
     *
     * @see Driver#connect()
     */
    public Driver() {
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
            System.out.println("[dbDriver] Connecting to database...");
            conn = DriverManager.getConnection(Options.DB_URL + Options.DB_NAME, Options.DB_USER, Options.DB_PASS);
            stmt = conn.createStatement();
            System.out.println("[dbDriver] Successfully connect to " + conn.getMetaData().getURL());
        } catch (Exception se) {
            System.out.println("[dbDriver] Some problem with test.db connection");
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
        System.out.println("[dbDriver] Creating table...");

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
     * @see Driver#createTable(String, String)
     * @see Options#DB_NAME
     */
    public void createStudentsTable() {
        String sql = "CREATE TABLE " + StudentsTable +
                "(id VARCHAR(255) not NULL, " +
                " s_name VARCHAR(255), " +
                " s_group INTEGER, " +
                " s_average DOUBLE, " +
                " s_is_villager BOOL, " +
                " PRIMARY KEY ( id ))";
        createTable(Student.class.getSimpleName(), sql);
    }

    /**
     * Drop database if exist, and create new
     *
     * @see Options#DB_NAME
     */
    private void dropDB() {
        try {
            System.out.println("[dbDriver] Drop database...");
            sql = "DROP DATABASE IF EXISTS " + Options.DB_NAME;
            stmt.executeUpdate(sql);

            System.out.println("[dbDriver] Creating database...");
            sql = "CREATE DATABASE " + Options.DB_NAME;
            stmt.executeUpdate(sql);
            System.out.println("[dbDriver] Database '" + Options.DB_NAME + "' created successfully.");
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
            pstmt = conn.prepareStatement(CREATE_STUDENT);
            pstmt.setString(1, student.getId());
            pstmt.setString(2, student.getName());
            pstmt.setInt(3, student.getGroup());
            pstmt.setDouble(4, student.getAverageGrade());
            pstmt.setBoolean(5, student.getIsVillager());
            pstmt.executeUpdate();
        } catch (Exception se) {
            se.printStackTrace();
        }
    }


    /**
     * Select all {@link Student}'s objects from test.db
     *
     * @return <pre>{@code ArrayList<Student>}</pre> {@link Student}'s objects
     */
    public ArrayList<Student> getStudents() {
        System.out.println("[dbDriver] Select students...");
        ArrayList<Student> data = new ArrayList<>();
        try {
            res = stmt.executeQuery(GET_STUDENTS);
            HashMap<String, Student> map = new HashMap<>();
            while (res.next()) {
                String id = res.getString("id");
                Student st = map.get(id);
                if (st == null) {
                    st = new Student(
                            id,
                            res.getString("s_name"),
                            res.getInt("s_group"),
                            res.getDouble("s_average"),
                            res.getBoolean("s_is_villager")
                    );
                }

                if (Options.DEBUG) {
                    System.out.println("\t#" + res.getRow()
                            + "\t" + st.getName()
                            + "\t" + st.getAverageGrade()
                            + "\t" + st.getGroup()
                            + "\t" + st.getId());
                }
                data.add(st);
            }

            System.out.println("[dbDriver] Successfully select " + data.size() + " students.");

        } catch (Exception se) {
            se.printStackTrace();
        }
        return data;
    }

    public int getStudentCount() {
        int size = 0;
        System.out.println("[dbDriver] Get students count...");
        try {
            res = stmt.executeQuery(GET_STUDENTS_COUNT);
            while (res.next()) {
                size = res.getInt("size");
            }
            System.out.println("[dbDriver] " + size);
            return size;
        } catch (Exception se) {
            se.printStackTrace();
        }

        return 1;
    }

    public void initDB(ArrayList<Student> data) {
        System.out.println("[dbDriver] Init database...");

        for (Student student : data) {
            System.out.println('\t' + student.toString());
            createStudent(student);
        }
    }

    /**
     * Drop database if exist, and create new
     * Create all tables
     *
     * @see Driver#dropDB()
     * @see Driver#createStudentsTable()
     * @see Driver#createMarkTable()
     * @see Options#DB_NAME
     */
    public void createDB() {
        dropDB();
        connect();
        createStudentsTable();
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

        System.out.println("[dbDriver] Close test.db connection... Goodbye!");
    }

    public static void main(String[] args) {
        Driver db = new Driver();
        db.createDB();
        db.initDB(Student.generateFakeData());
        db.getStudents();
        db.getStudentCount();
        db.close();
    }
}