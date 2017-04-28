<%@ page import="generator.Main" %>
<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 4/28/17
  Time: 13:53
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<div class="container">
    <h1 class="col-md-8 col-md-offset-2">
        <%=Main.getTittle()%>
    </h1>
    <form class="col-md-6 col-md-offset-3" method="POST">
        <div class="input-group input-group-lg">
            <span class="input-group-addon" id="sizing-addon1">@</span>
            <input type="text" class="form-control" placeholder="first type your app name..."
                   aria-describedby="sizing-addon1">
            <span class="input-group-btn">
                <button class="btn btn-default" type="button">Next</button>
            </span>
        </div>
    </form>
</div>