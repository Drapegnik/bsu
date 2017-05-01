<%--
  Created by IntelliJ IDEA.
  User: Drapegnik
  Date: 4/28/17
  Time: 15:36
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" language="java" %>
<div class="container">
    <h2 class="col-md-8 col-md-offset-2">
        Choose front-end framework for your app:
    </h2>
    <form class="form-horizontal col-md-3 col-md-offset-4" method="POST" action="/controller">
        <div class="form-group">
            <div class="pull-left"><img src="/images/js.png" width="50px">
                <h3 class="pull-right">Native JS</h3></div>
            <div class="pull-right">
                <label class="btn btn-default btn-circle btn-lg">
                    <input type="radio" name="framework" value="js"
                    ${sessionScope.framework == "js" ? 'checked' : ''}
                    >
                    <i class="glyphicon glyphicon-ok"></i>
                </label>
            </div>
        </div>
        <div class="form-group">
            <div class="pull-left"><img src="/images/ng.png" width="60px">
                <h3 class="pull-right">Angular</h3></div>
            <div class="pull-right">
                <label class="btn btn-default btn-circle btn-lg">
                    <input type="radio" name="framework" value="ng"
                    ${sessionScope.framework == "ng" ? 'checked' : ''}
                    ><i class="glyphicon glyphicon-ok"></i>
                </label>
            </div>
        </div>
        <div class="form-group">
            <div class="pull-left"><img src="/images/react.png" width="60px">
                <h3 class="pull-right">React</h3></div>
            <div class="pull-right">
                <label class="btn btn-default btn-circle btn-lg">
                    <input type="radio" name="framework" value="react"
                    ${sessionScope.framework == "react" ? 'checked' : ''}
                    ><i class="glyphicon glyphicon-ok"></i>
                </label>
            </div>
        </div>
        <div class="form-group">
            <div class="pull-left"><img src="/images/vue.png" width="60px">
                <h3 class="pull-right">Vue.js</h3></div>
            <div class="pull-right">
                <label class="btn btn-default btn-circle btn-lg">
                    <input type="radio" name="framework" value="vue"
                    ${sessionScope.framework == "vue" ? 'checked' : ''}
                    ><i class="glyphicon glyphicon-ok"></i>
                </label>
            </div>
        </div>
        <div class="form-group">
            <div class="pull-left"><img src="/images/polymer.png" width="60px">
                <h3 class="pull-right">Polymer</h3></div>
            <div class="pull-right">
                <label class="btn btn-default btn-circle btn-lg">
                    <input type="radio" name="framework" value="polymer"
                    ${sessionScope.framework == "polymer" ? 'checked' : ''}
                    ><i class="glyphicon glyphicon-ok"></i>
                </label>
            </div>
        </div>
        <div class="row">
            <a href="/" class="btn btn-default col-md-4 pull-left">Back</a>
            <button class="btn btn-default col-md-4 pull-right" type="submit">Next</button>
        </div>
        <input type="hidden" name="nextPage" value="style"/>
    </form>
</div>