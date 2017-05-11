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
                    <td>${student.name}</td>
                    <td>${student.group}</td>
                    <td>
                        <c:forEach items="${student.marks}" var="mark">
                            ${mark.formatted()}
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

<c:if test="${not empty requestScope.response && requestScope.response != '200'}">
    Error! ${requestScope.response}
</c:if>
</body>
</html>
