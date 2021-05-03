package com.company.servicii;

import java.io.File;
import java.text.SimpleDateFormat;
import java.util.ArrayList;
import java.util.Date;

public class AuditService {
    // tot singleton si acest service
    private static AuditService instanta = null;
    private String path = "./date/AuditLog.csv";
    private FileWriterService fws = FileWriterService.getInstance();
    // constructor privat
    private AuditService() { }

    public static AuditService getInstance() {
        if (instanta == null)
            instanta = new AuditService();
        return instanta;
    }

    public void log(String numeActiune) {
        String timestamp = new SimpleDateFormat("yyyy.MM.dd.HH.mm.ss").format(new Date());
        ArrayList<String> mesaj =new ArrayList<String>();
        mesaj.add(numeActiune);
        mesaj.add(timestamp);
        fws.write(path,mesaj);
    }

}
