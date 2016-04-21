<?php
    //connect to mysql db
    $con = mysql_connect("127.0.0.1:9092","root","root") or die('Could not connect: ' . mysql_error());
    //connect to the employee database
    mysql_select_db("test", $con);

    //read the json file contents
    $jsondata = file_get_contents('/Users/jessietan/Desktop/linkedindata.json');
    
    //convert json object to php associative array
    $data = json_decode($jsondata, true);
    
    //get the employee details
    $lastname = $data['lastName'];
    $emailaddress = $data['emailAddress'];
    $firstname = $data['firstName'];
    
    $location = $data['location']['name'];
    $industry = $data['industry'];
    
    //insert into mysql table
    $sql = "INSERT INTO PlacedUser(first_name, last_name, email, location, industry)
    VALUES('$firstname', '$lastname', '$emailaddress', '$location', '$industry')
    ON DUPLICATE KEY UPDATE 
       first_name = VALUES(first_name),
       last_name = VALUES(last_name),
       location = VALUES(location),
       industry = VALUES(industry)";
    if(!mysql_query($sql,$con))
    {
        die('Error : ' . mysql_error());
    }
?>