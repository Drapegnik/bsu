<%--
 Created by IntelliJ IDEA.
 User: Drapegnik
 Date: 5/11/17
 Time: 12:20
 To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Students table</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" href="https://bootswatch.com/solar/bootstrap.min.css">
    <script type="text/javascript">
        function validate() {
            var name = document.getElementById("name");
            var group = document.getElementById("group");
            var sub1 = document.getElementById("1");
            var sub2 = document.getElementById("2");
            var sub3 = document.getElementById("3");
            var sub4 = document.getElementById("4");
            var sub5 = document.getElementById("5");
            if (name.value.length <= 0) {
                alert("Name field can't be empty!");
                return false;
            }
            if (parseInt(group.value, 10) &&
                parseInt(sub1.value, 10) &&
                parseInt(sub2.value, 10) &&
                parseInt(sub3.value, 10) &&
                parseInt(sub4.value, 10) &&
                parseInt(sub5.value, 10)) {
                return true;
            }
            alert("Group and subjects fields must be numbers!");
            return false;
        }
    </script>
</head>
<body>
<div class="container">
    <div class="row col-md-12">
        <c:if test="${not empty requestScope.status && requestScope.status != '200'}">
            <div class="col-md-4 alert alert-danger alert-dismissible error-block" role="alert">
                <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
                <strong>Error!</strong><br>
                <code><c:out value="${requestScope.status}"/></code>
            </div>
        </c:if>
    </div>

    <div class="col-md-4">
        <h2>Add Student:</h2>
        <form method="POST" action="/controller?action=addStudent" onsubmit="return validate();">
            <div class="form-group">
                <label for="name">name: </label>
                <input class="form-control" id="name" type="text" name="name">
                <label for="group">group: </label>
                <input class="form-control" id="group" type="text" name="group">
            </div>
            <div class="form-group">
                <label for="1">algebra: </label>
                <input class="form-control" id="1" type="text" name="ALGEBRA">
                <label for="2">geometry: </label>
                <input class="form-control" id="2" type="text" name="GEOMETRY">
                <label for="3">java: </label>
                <input class="form-control" id="3" type="text" name="JAVA">
                <label for="4">cpp: </label>
                <input class="form-control" id="4" type="text" name="CPP">
                <label for="5">history: </label>
                <input class="form-control" id="5" type="text" name="HISTORY">
            </div>
            <div class="form-group pull-right">
                <button class="btn btn-default" type="submit">Add Student</button>
            </div>
            <div class="form-group">
                <a class="btn btn-default" href="/controller?action=getStudents">Load Students!</a>
                <a class="btn btn-default" href="/controller?action=getBadStudents">Get Bad Students!</a>
            </div>
        </form>
    </div>

    <div class="col-md-4">
        <c:if test="${not empty requestScope.students}">
            <h2>Students:</h2>
            <table class="table">
                <tr>
                    <th>name</th>
                    <th>group</th>
                    <th>marks</th>
                </tr>
                <c:forEach items="${requestScope.students}" var="student">
                    <tr>
                        <td>${student.name}</td>
                        <td>${student.group}</td>
                        <td>
                            <c:forEach items="${student.marks}" var="mark">
                                ${mark.formatted()}
                            </c:forEach>
                        </td>
                    </tr>
                </c:forEach>
            </table>
        </c:if>
    </div>

    <div class="col-md-4">
        <c:if test="${not empty requestScope.badIds}">
            <h2>Bad Students:</h2>
            <table class="table">
                <tr>
                    <th>name</th>
                    <th>group</th>
                    <th>marks</th>
                    <th>delete!</th>
                </tr>
                <c:forEach items="${requestScope.students}" var="student">
                    <c:if test="${requestScope.badIds.contains(student.id)}">
                        <tr>
                            <td><c:out value="${student.name}"/></td>
                            <td><c:out value="${student.group}"/></td>
                            <td>
                                <c:forEach items="${student.marks}" var="mark">
                                    <c:out value="${mark.formatted()}"/>
                                </c:forEach>
                            </td>
                            <td><a href="/controller?action=deleteStudent&id=${student.id}">x</a></td>
                        </tr>
                    </c:if>
                </c:forEach>
            </table>
        </c:if>
    </div>
</div>
</body>
<script src="https://code.jquery.com/jquery-3.2.1.min.js"
        integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
        crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
        integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
        crossorigin="anonymous"></script>
</html>
