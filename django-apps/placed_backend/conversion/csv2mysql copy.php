<?php
    //connect to mysql db
    $con = mysql_connect("127.0.0.1:9092","root","root") or die('Could not connect: ' . mysql_error());
    //connect to the employee database
    mysql_select_db("test", $con);

    
    //insert into mysql table
    $sql = "LOAD DATA LOCAL INFILE '/Users/jessietan/Desktop/var-backend2/django-apps/placed_backend/data/emailvalidation.csv' 
    INTO TABLE EmailValidation
FIELDS TERMINATED BY ',' 
ENCLOSED BY '\"'
LINES TERMINATED BY '\r'";

    if(!mysql_query($sql,$con))
    {
        die('Error : ' . mysql_error());
    }
?>