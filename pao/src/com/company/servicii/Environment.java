package com.company.servicii;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

// schimba aici pentru mutatul in alta parte!
public class Environment {
    static final String DB_URL = "jdbc:mysql://localhost:3306/magazin";
    static final String USER = "root";
    static final String PASS = "";
    // am zis ca ajunge un connection pe toata aplicatia
    // mergea facut singleton si clasa asta dar am considerat ca e mai clean asa
    static Connection conn;
//    static Statement stmt;

    static {
        try {
            conn = DriverManager.getConnection(DB_URL, USER, PASS);
//            stmt = conn.createStatement();
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }


}
