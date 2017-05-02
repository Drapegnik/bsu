<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 4/28/17
  Time: 15:36
  To change this template use File | Settings | File Templates.
--%>
<%@ page import="java.util.ArrayList" %>
<%@ page import="generator.SelectItemModel" %>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<%@ taglib prefix="gen" uri="/WEB-INF/custom.tld" %>
<%
    ArrayList<SelectItemModel> items = new ArrayList<>();
    items.add(new SelectItemModel("Native JS", "js", "/images/js.png", 50));
    items.add(new SelectItemModel("Angular", "ng", "/images/ng.png", 65));
    items.add(new SelectItemModel("React", "react", "/images/react.png", 65));
    items.add(new SelectItemModel("Vue.js", "vue", "/images/vue.png"));
    items.add(new SelectItemModel("Polymer", "polymer", "/images/polymer.png"));
%>
<div class="container">
    <h2 class="col-md-8 col-md-offset-2">
        Choose front-end framework for your app:
    </h2>
    <form class="form-horizontal col-md-3 col-md-offset-4" method="POST" action="/controller">
        <c:forEach items="<%=items%>" var="item">
            <gen:SelectItem
                    name="framework"
                    value="${item.value}"
                    imagePath="${item.imagePath}"
                    imageSize="${item.imageSize}"
                    isChecked="${sessionScope.framework == item.value}"
            >
                ${item.title}
            </gen:SelectItem>
        </c:forEach>
        <div class="row">
            <a href="/" class="btn btn-default col-md-4 pull-left">Back</a>
            <button class="btn btn-default col-md-4 pull-right" type="submit">Next</button>
        </div>
        <input type="hidden" name="nextPage" value="style"/>
    </form>
</div>