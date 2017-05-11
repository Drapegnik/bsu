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
</head>
<body>
<c:if test="${not empty requestScope.students}">
    <h2>Students:</h2>
    <table>
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

<c:if test="${not empty requestScope.badIds}">
    <h2>Bad Students:</h2>
    <table>
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

<button><a href="/controller?action=getStudents">Load Students!</a></button>
<button><a href="/controller?action=getBadStudents">Get Bad Students!</a></button>

<br>
<h2>Add Student:</h2>
<form method="POST" action="/controller?action=addStudent">
    <label for="name">name: </label>
    <input id="name" type="text" name="name">
    <label for="group">group: </label>
    <input id="group" type="text" name="group">
    <label for="1">algebra: </label>
    <input id="1" type="text" name="ALGEBRA">
    <label for="2">geometry: </label>
    <input id="2" type="text" name="GEOMETRY">
    <label for="3">java: </label>
    <input id="3" type="text" name="JAVA">
    <label for="4">cpp: </label>
    <input id="4" type="text" name="CPP">
    <label for="5">history: </label>
    <input id="5" type="text" name="HISTORY">
    <input type="submit">
</form>
<c:if test="${not empty requestScope.response && requestScope.response != '200'}">
    Error! <c:out value="${requestScope.response}"/>
</c:if>
</body>
</html>
