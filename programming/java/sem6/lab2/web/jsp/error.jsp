<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 5/1/17
  Time: 20:31
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<html>
<head>
    <title>Web app Generator</title>
    <link rel="stylesheet" href="https://bootswatch.com/solar/bootstrap.min.css">
    <meta http-equiv="Content-Type"  content="text/html; charset=UTF-8" />
</head>
<body>
<div class="container">
    <div style="margin: 50px;" class="alert alert-danger alert-dismissible error-block" role="alert">
        <a type="button" href="/" class="close" data-dismiss="alert" aria-label="Close"><span
                aria-hidden="true">&times;</span></a>
        <strong>Error! ${pageContext.errorData.statusCode}</strong> from: ${pageContext.errorData.requestURI}
        ${pageContext.errorData.throwable.message}
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
