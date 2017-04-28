<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 4/28/17
  Time: 13:53
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<div class="container">
    <h1 class="col-md-8 col-md-offset-2">Choose best web stack for your app!</h1>
    <h2 class="col-md-8 col-md-offset-2">First type your app name:</h2>
    <form class="col-md-6 col-md-offset-3" method="POST" action="/controller">
        <div class="input-group input-group-lg">
            <span class="input-group-addon" id="sizing-addon1">@</span>
            <input
                    id="appName"
                    name="appName"
                    type="text"
                    class="form-control"
                    placeholder="app name..."
                    aria-describedby="sizing-addon1"
                    value="${empty sessionScope.appName ? '' : sessionScope.appName}"
            >
            <span class="input-group-btn">
                <button type="submit" class="btn btn-default">Next</button>
            </span>
        </div>
        <input type="hidden" name="nextPage" value="front"/>
    </form>
</div>