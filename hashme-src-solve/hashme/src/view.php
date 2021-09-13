<?php
    include("secret.php");#contain $flag and $secret
    ksort($_GET);
    $message = "";
    foreach ($_GET as $key => $value) {
        if ($key != "sig") {
            $message.= $value;
        }
    }
    $hashed = $secret.$message;
    $hash_string = md5($hashed);
    $sig = @$_GET['sig'];
    if ($sig === $hash_string){
        if($_GET['user'] === "admin"){
            echo "Hello Admin. Here is your flag: $flag";
        } else {
            echo "Hello {$_GET['user']}. Good signature but no flag xD";
        }
    } else {
        echo "Wrong signature! :(";
    }
?>