package app;

import app.backend.dbDriver;
import app.models.Student;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * Created by Drapegnik on 5/11/17.
 */
@MultipartConfig
@WebServlet("/controller")
public class MainController extends HttpServlet {

    private dbDriver db;

    public void init(ServletConfig config) throws ServletException {
        super.init(config);
        System.out.println("[main controller] init");
        db = new dbDriver();
    }

    @Override
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doAction(request, response);
    }

    @Override
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doAction(request, response);
    }

    private void doAction(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String action = request.getParameter("action");
        System.out.println("[main controller] " + action);
        switch (action) {
            case "getStudents":
                request.setAttribute("students", db.getStudents());
                break;
            case "getBadStudents":
                request.setAttribute("students", db.getStudents());
                request.setAttribute("badIds", db.getBadStudentsIds());
                break;
            case "addStudent":
                String name = request.getParameter("name");
                String groupStr = request.getParameter("group");
                if (name == null || groupStr == null) {
                    request.setAttribute("status", "500");
                }
                int group = Integer.parseInt(groupStr);
                Student s = new Student(name, group);
                db.createStudent(s);
                break;
            case "deleteStudent":
                System.out.println("[main controller] im'here");
                String id = request.getParameter("id");
                System.out.println(id);
                if (id == null) {
                    request.setAttribute("status", "500");
                }
                db.deleteStudent(id);
                request.setAttribute("students", db.getStudents());
                request.setAttribute("badIds", db.getBadStudentsIds());
                break;
            default:
                request.setAttribute("status", "404");
                break;
        }
        if (request.getAttribute("status") == null) {
            request.setAttribute("status", "200");
        }
        System.out.println("[main controller] " + request.getAttribute("status"));
        request.getRequestDispatcher("/").forward(request, response);
    }
}