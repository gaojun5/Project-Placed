<?php
    //open connection to mysql db
    $connection = mysqli_connect("127.0.0.1:9092","root","root","test") or die("Error " . mysqli_error($connection));

    //fetch table rows from mysql db
    $sql = "select * from Company";
    $result = mysqli_query($connection, $sql) or die("Error in Selecting " . mysqli_error($connection));

    //create an array
    $emparray = array();
    while($row =mysqli_fetch_assoc($result))
    {
        $emparray[] = $row;
    }
   

    $json_data = json_encode($emparray);
file_put_contents('company/company.json', $json_data);

    //close the db connection
    mysqli_close($connection);
?>