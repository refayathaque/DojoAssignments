package com.refayathaque.web;
import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/Home")
public class User extends HttpServlet {
    private static final long serialVersionUID = 1L;
   
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        String fname = request.getParameter("fname");
        String lname = request.getParameter("lname");
        String lang = request.getParameter("lang");
        String hometown = request.getParameter("hometown");

        response.setContentType("text/html");
        
        if(fname == null) {
        	fname = "Unknown";
        }
        if(lname == null) {
        	lname = "Unknown";
        }
        if(lang == null) {
        	lang = "Unknown";
        }
        if(hometown == null) {
        	hometown = "Unknown";
        }
        else {
        	fname = fname;
        	lname = lname;
        	lang = lang;
        	hometown = hometown;
        }
        
        PrintWriter out = response.getWriter();
        out.write("<h1>Welcome, " + fname + " " + lname + "</h1>");
        out.write("<h2>Favorite Language : " + lang + "</h2>");
        out.write("<h2>Hometown : " + hometown + "</h2>");
        
    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doGet(request, response);
    }
}
