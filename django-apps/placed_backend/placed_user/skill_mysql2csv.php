<?php
    //connect to mysql db
    $con = mysql_connect("127.0.0.1:9092","root","root") or die('Could not connect: ' . mysql_error());
    //connect to the employee database
    mysql_select_db("test", $con);

    
    //insert into mysql table
    $sql = "SELECT * INTO OUTFILE '/Users/jessietan/Desktop/4/django_social_app/skill.csv'
FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"'
LINES TERMINATED BY '\r\n'
FROM Skill";

    if(!mysql_query($sql,$con))
    {
        die('Error : ' . mysql_error());
    }
?>

