<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 4/28/17
  Time: 19:46
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="generator.SelectItemModel" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="gen" uri="/WEB-INF/custom.tld" %>
<%
    ArrayList<SelectItemModel> items = new ArrayList<>();
    items.add(new SelectItemModel("Vanilla CSS", "css", "/images/css.png", 70));
    items.add(new SelectItemModel("less", "less", "/images/less.png", 80));
    items.add(new SelectItemModel("Sass", "sass", "/images/sass.png", 80));
    items.add(new SelectItemModel("Stylus", "stylus", "/images/stylus.png", 65));
%>
<div class="container">
    <h2 class="col-md-8 col-md-offset-2">
        Choose css preprocessor for your app:
    </h2>
    <form class="form-horizontal col-md-3 col-md-offset-4" method="POST" action="/controller">
        <c:forEach items="<%=items%>" var="item">
            <gen:SelectItem
                    name="style"
                    value="${item.value}"
                    imagePath="${item.imagePath}"
                    imageSize="${item.imageSize}"
                    isChecked="${sessionScope.style == item.value}"
            >
                ${item.title}
            </gen:SelectItem>
        </c:forEach>
        <div class="row">
            <a href="/?page=front" class="btn btn-default col-md-4 pull-left">Back</a>
            <button class="btn btn-default col-md-4 pull-right" type="submit">Next</button>
        </div>
        <input type="hidden" name="nextPage" value="back"/>
    </form>
</div>