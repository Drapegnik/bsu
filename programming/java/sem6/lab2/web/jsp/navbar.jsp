<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 4/28/17
  Time: 13:50
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<nav class="navbar navbar-default">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">WebApp Generator</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="${param.currentPage == "main" ? "active" : ""}">
                    <a href="/">App name</a>
                </li>
                <li class="${param.currentPage == "front" ? "active" : ""}">
                    <a href="/?page=front">Front-end</a>
                </li>
                <li class="${param.currentPage == "style" ? "active" : ""}">
                    <a href="/?page=style">Styles</a>
                </li>
                <li class="${param.currentPage == "back" ? "active" : ""}">
                    <a href="/?page=back">Back-end</a>
                </li>
            </ul>
            <ul class="nav navbar-nav navbar-right">
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">Step <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="/">App name</a></li>
                        <li><a href="/?page=front">Front-end</a></li>
                        <li><a href="/?page=style">Styles</a></li>
                        <li><a href="/?page=back">Back-end</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Results</a></li>
                    </ul>
                </li>
                <li><a href="/">Reset</a></li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>
