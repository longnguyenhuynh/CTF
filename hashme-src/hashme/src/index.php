<?php
    require_once('./user.class.php');

    if (!isset($_COOKIE['user'])){
        $user = new User("efienser");
        setcookie('user',base64_encode(serialize($user)));
    } else {
        $user = @unserialize(base64_decode($_COOKIE['user']));
    }
?>
<!DOCTYPE html>
<html lang="en">
<head>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <title>Home</title>
</head>
<body>
Get flag:<br>
<input id="name" type="text" placeholder="Name..."/><br>
<input id="sig" type="text" placeholder="Signature..."/><br>
<button>FLAG</button><br>

<script>
    $("button").click(function() {
        $.get("view.php",
        {
            user:$("#name").val(),
            sig:$("#sig").val()
        }, function(result){
            alert(result);
        });
    });
    
</script>
</body>
</html>
