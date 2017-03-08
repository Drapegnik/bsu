/**
 * Created by Drapegnik on 08.03.17.
 */

import java.sql.*;

/**
 * <p>Class for connecting to database</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class dbDriver {
    private Connection conn = null;
    private Statement stmt = null;
    private String sql;

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
        db.close();
    }
}