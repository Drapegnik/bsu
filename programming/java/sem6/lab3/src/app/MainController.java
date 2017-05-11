package app;


import app.backend.dbDriver;
import app.models.Mark;
import app.models.Student;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Map;

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
        switch (action) {
            case "getStudents":
                request.setAttribute("response", db.getStudents());
                break;
            case "getBadStudents":
                request.setAttribute("response", db.getBadStudentsIds());
                break;
            case "addStudent":
                String name = request.getParameter("name");
                String groupStr = request.getParameter("group");
                if (name == null || groupStr == null) {
                    request.setAttribute("response", "500");
                }
                int group = Integer.parseInt(groupStr);
                Student s = new Student(name, group);
                db.createStudent(s);
                request.setAttribute("response", "200");
                break;
            case "deleteStudent":
                String id = request.getParameter("id");
                if (id == null) {
                    request.setAttribute("response", "500");
                }
                db.deleteStudent(id);
                request.setAttribute("response", "200");
                break;
        }
        request.getRequestDispatcher("/").forward(request, response);
    }
}