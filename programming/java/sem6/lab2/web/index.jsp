<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 4/28/17
  Time: 13:15
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<html>
<head>
    <title>Web app Generator</title>
    <link rel="stylesheet" href="https://bootswatch.com/solar/bootstrap.min.css">
    <link rel="stylesheet" href="/style.css">
    <meta http-equiv="Content-Type"  content="text/html; charset=UTF-8" />
</head>
<body>
<%
    String currentPage = request.getParameter("page");
    if (currentPage == null) {
        currentPage = (String) request.getAttribute("page");
    }

    if (currentPage == null) {
        currentPage = "main";
    }

    String includePage = "/jsp/" + currentPage + ".jsp";
%>

<jsp:include page="/jsp/navbar.jsp">
    <jsp:param name="currentPage" value="<%=currentPage%>"/>
</jsp:include>
<jsp:include page="<%=includePage%>"/>
</body>

<script src="https://code.jquery.com/jquery-3.2.1.min.js"
        integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4="
        crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"
        integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa"
        crossorigin="anonymous"></script>
</html>
