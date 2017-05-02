<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 4/28/17
  Time: 18:30
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<%@ page import="java.util.ArrayList" %>
<%@ page import="generator.SelectItemModel" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="gen" uri="/WEB-INF/custom.tld" %>
<%
    ArrayList<SelectItemModel> items = new ArrayList<>();
    items.add(new SelectItemModel("Python/Django", "dj", "/images/dj.png"));
    items.add(new SelectItemModel("Node.js/Express", "node", "/images/node.png"));
    items.add(new SelectItemModel("Ruby on Rails", "ror", "/images/ror.png"));
    items.add(new SelectItemModel("Java/Spring", "spring", "/images/spring.png", 70));
%>
<div class="container">
    <h2 class="col-md-8 col-md-offset-2">
        Choose back-end framework for your app:
    </h2>
    <form class="form-horizontal col-md-3 col-md-offset-4" method="POST" action="/controller">
        <c:forEach items="<%=items%>" var="item">
            <gen:SelectItem
                    name="back"
                    value="${item.value}"
                    imagePath="${item.imagePath}"
                    imageSize="${item.imageSize}"
                    isChecked="${sessionScope.back == item.value}"
            >
                ${item.title}
            </gen:SelectItem>
        </c:forEach>
        <div class="row">
            <a href="/?page=style" class="btn btn-default col-md-4 pull-left">Back</a>
            <button class="btn btn-default col-md-4 pull-right" type="results">Next</button>
        </div>
        <input type="hidden" name="nextPage" value="results"/>
    </form>
</div>