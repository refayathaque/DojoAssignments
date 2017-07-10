<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Checkerboard</title>
<link href="${pageContext.request.contextPath}/style.css" type="text/css" rel="stylesheet"></link>
</head>

<body>
<h1>Checkerboard</h1>
	<% int w = Integer.parseInt(request.getParameter("w")); %>
	<% int h = Integer.parseInt(request.getParameter("h")); %>
	
	<% for(int y = 0; y < h; y++) { %>
		<% for(int x = 0; x < w; x++) { %>
			<% if(x % 2 == 1) { %>
				<div class = "red"></div>
			<% } else if(x % 2 == 0) { %>
				<div class = "blue"></div>
			<% } %>
		<% } %>
	<% } %>
	
<h1><%=request.getParameter("w")%>w X <%=request.getParameter("h")%>h </h1>
</body>
</html>