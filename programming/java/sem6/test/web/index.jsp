<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 5/25/17
  Time: 15:21
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>Test</title>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8"/>
    <link rel="stylesheet" href="https://bootswatch.com/solar/bootstrap.min.css">
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

    <div class="row col-md-12">
        <div class="form-group">
            <a class="btn btn-default" href="/controller?action=getStudents">Load Students!</a>
            <a class="btn btn-default" href="/controller?action=getStudentsCount">Get Count!</a>
        </div>
    </div>

    <div class="col-md-10 col-md-offset-1">
        <c:if test="${not empty requestScope.students}">
            <h2>Students:</h2>
            <table class="table table-striped">
                <tr>
                    <th>name</th>
                    <th>group</th>
                    <th>average</th>
                    <th>villager</th>
                </tr>
                <c:forEach items="${requestScope.students}" var="student">
                    <tr>
                        <td>${student.name}</td>
                        <td>${student.group}</td>
                        <td>${student.averageGrade}</td>
                        <td>
                            <c:if test="${student.isVillager}">
                                <input type="checkbox" checked disabled>
                            </c:if>
                            <c:if test="${not student.isVillager}">
                                <input type="checkbox" disabled>
                            </c:if>
                        </td>
                    </tr>
                </c:forEach>
            </table>
        </c:if>
        <c:if test="${not empty requestScope.count}">
            <p class="text">Student count: <c:out value="${requestScope.count}"/></p>
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
