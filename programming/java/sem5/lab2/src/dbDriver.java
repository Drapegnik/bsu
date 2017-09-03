/**
 * Created by Drapegnik on 21.12.16.
 */
//STEP 1. Import required packages

import java.sql.*;
import java.util.ArrayList;
import java.util.UUID;

public class dbDriver {
    // JDBC driver name and database URL
    static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
    static final String DB_URL = "jdbc:mysql://localhost/";

    //  Database credentials
    static final String DB_NAME = "lab2";
    static final String TABLE_NAME = "student";
    static final String USER = "root";
    static final String PASS = "";

    // Data

    private ArrayList<Student> students;
    private Connection conn = null;
    private Statement stmt = null;
    private String sql;

    public dbDriver() {
        try {
            //STEP 2: Register JDBC driver
            Class.forName("com.mysql.jdbc.Driver");

            //STEP 3: Open a connection
            System.out.println("Connecting to database...");
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
            stmt = conn.createStatement();
        } catch (SQLException se) {
            //Handle errors for JDBC
            se.printStackTrace();
        } catch (Exception e) {
            //Handle errors for Class.forName
            e.printStackTrace();
        } finally {
        }//end try
    }

    public void createDB() {
        try {
            //STEP 4: Create DB
            System.out.println("Drop database...");
            sql = "DROP DATABASE " + DB_NAME;
            stmt.executeUpdate(sql);

            System.out.println("Creating database...");
            sql = "CREATE DATABASE " + DB_NAME;
            stmt.executeUpdate(sql);
            System.out.println("Database '" + DB_NAME + "' created successfully...");

            //STEP 4: Create table
            System.out.println("Creating table...");

            sql = "CREATE TABLE " + DB_NAME + "." + TABLE_NAME +
                    "(id VARCHAR(255) not NULL, " +
                    " name VARCHAR(255), " +
                    " group_num INTEGER, " +
                    " math INTEGER, " +
                    " prog INTEGER, " +
                    " hist INTEGER, " +
                    " PRIMARY KEY ( id ))";

            stmt.executeUpdate(sql);
            System.out.println("Table '" + DB_NAME + "." + TABLE_NAME + "' created successfully...");

            //STEP 5: Init table data
            writeStudents(Student.readFromFile("data.txt"));
        } catch (SQLException se) {
            //Handle errors for JDBC
            se.printStackTrace();
        } catch (Exception e) {
            //Handle errors for Class.forName
            e.printStackTrace();
        } finally {
        }//end try
    }

    public ArrayList<Student> readStudents() {
        students = new ArrayList<>();
        try {
            sql = String.format("SELECT name, group_num, math, prog, hist FROM %s.%s", DB_NAME, TABLE_NAME);
            System.out.println(sql);
            ResultSet rs = stmt.executeQuery(sql);
            //STEP 5: Extract data from result set
            while (rs.next()) {
                students.add(new Student(rs.getString("name"), rs.getInt("group_num"), rs.getInt("math"), rs.getInt("prog"), rs.getInt("hist")));
            }
            rs.close();
        } catch (SQLException se) {
            //Handle errors for JDBC
            se.printStackTrace();
        } catch (Exception e) {
            //Handle errors for Class.forName
            e.printStackTrace();
        } finally {
            return students;
        }
    }

    public void writeStudents(ArrayList<Student> students) {
        try {
            System.out.println("Inserting records into the table...");
            sql = String.format("DELETE FROM %s.%s", DB_NAME, TABLE_NAME);
            stmt.executeUpdate(sql);

            for (Student student : students) {
                sql = String.format("INSERT INTO %s.%s VALUES ('%s', '%s', %d, %d, %d, %d)",
                        DB_NAME,
                        TABLE_NAME,
                        UUID.randomUUID(),
                        student.getName(),
                        student.getGroup(),
                        student.getMarkMath(),
                        student.getMarkProg(),
                        student.getMarkHistory()
                );
                System.out.println(sql);
                stmt.executeUpdate(sql);
            }

        } catch (SQLException se) {
            //Handle errors for JDBC
            se.printStackTrace();
        } catch (Exception e) {
            //Handle errors for Class.forName
            e.printStackTrace();
        } finally {
            System.out.println("Successfully insert " + students.size() + " records.");

        }
    }

    public void close() {
        try {
            if (stmt != null)
                stmt.close();
        } catch (SQLException se2) {
        }// nothing we can do
        try {
            if (conn != null)
                conn.close();
        } catch (SQLException se) {
            se.printStackTrace();
        }//end finally try
        System.out.println("Close db connection... Goodbye!");
    }

    public static void main(String[] args) {
        dbDriver db = new dbDriver();
        db.createDB();
        db.close();
    }//end main


}//end JDBCExample