package com.refayathaque.randomword.controllers;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.util.Date;
import java.util.Random;
import java.text.SimpleDateFormat;

public class Index extends HttpServlet {
	private static final long serialVersionUID = 1L;
	
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    
	HttpSession session = request.getSession();
	String count = (String) session.getAttribute("count");
	Integer num = 0;
	char[] chars = {'1', '2', '3', '4', '5', 'a', 'b', 'c', 'd', 'e'};
	Random rand = new Random();
	int rndIndex = 0;
	String str = "";
	
	if(count != null) {
		num = Integer.parseInt(count);
		num += 1;
		count = num.toString(); 
		session.setAttribute("count", count);
		
		Date date = new Date();
		SimpleDateFormat formatter = new SimpleDateFormat("MMMM dd, yyyy - hh:mm:ss a");
		request.setAttribute("time", formatter.format(date));
	} else {
		session.setAttribute("count", "0");
		request.setAttribute("time", "This is your first time so no time brah!");
	}
	
	for(int i = 0; i < 14; i++) {
		rndIndex = rand.nextInt(chars.length);
		str += chars[rndIndex];
	}
	request.setAttribute("str", str);
	
	RequestDispatcher view = request.getRequestDispatcher("/WEB-INF/views/index.jsp");
    view.forward(request, response);
}

protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
	doGet(request, response);
}

}
