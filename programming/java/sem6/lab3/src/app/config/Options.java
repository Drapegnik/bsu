/**
 * Created by Drapegnik on 08.03.17.
 */

package app.config;

/**
 * <p>Class for storing setting and constants</p>
 *
 * @author Ivan Pazhitnykh
 * @version 1.0
 */
public class Options {
    public static final String JDBC_DRIVER = "com.mysql.jdbc.Driver";
    public static final String DB_URL = "jdbc:mysql://localhost/";
    public static final String DB_NAME = "sem6lab1";
    public static final String DB_USER = "root";
    public static final String DB_PASS = "";
    public static final String PORT_ENV_NAME = "RMI_PORT";
    public static final String HOST_ENV_NAME = "RMI_HOST";
    public static final String DB_TYPE_ENV_NAME = "DB_TYPE";
    public static final String STUDENTS_FILE_NAME = "students.binary";
    public static final Boolean DEBUG = false;
    public static final String XML_DIR = "data/";
}