<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 5/2/17
  Time: 03:47
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<div class="container">
    <div class="row">
        <div class="col-md-6 col-md-offset-2">
            <h1>Your awesome ${empty sessionScope.appName ? 'MyApp' : sessionScope.appName} app:</h1>
        </div>
        <a class="btn btn-info btn-lg col-md-2" style="margin-top: 20px"
           href="https://www.google.by/search?q=yeoman+${sessionScope.front}+${sessionScope.style}+${sessionScope.back}"
        >Find generator!</a>
    </div>
    <div class="row" style="margin-top: 40px">
        <div class="col-md-3">
            <c:if test="${not empty sessionScope.front}">
                <img src="/images/${sessionScope.front}.png" width="200px">
            </c:if>
            <c:if test="${empty sessionScope.front}">
                <a class="btn btn-primary btn-lg" style="margin-top: 80px" href="/?page=front">Choose front!</a>
            </c:if>
        </div>
        <i class="col-md-1 glyphicon glyphicon-plus" style="margin-top: 100px"></i>
        <div class="col-md-3">
            <c:if test="${not empty sessionScope.style}">
                <img src="/images/${sessionScope.style}.png" width="200px">
            </c:if>
            <c:if test="${empty sessionScope.style}">
                <a class="btn btn-success btn-lg" style="margin-top: 80px" href="/?page=style">Choose style!</a>
            </c:if>
        </div>
        <i class="col-md-1 glyphicon glyphicon-plus" style="margin-top: 100px"></i>
        <div class="col-md-4">
            <c:if test="${not empty sessionScope.back}">
                <img src="/images/${sessionScope.back}.png" width="200px">
            </c:if>
            <c:if test="${empty sessionScope.back}">
                <a class="btn btn-warning btn-lg" style="margin-top: 80px" href="/?page=back">Choose back!</a>
            </c:if>
        </div>
    </div>
</div>
