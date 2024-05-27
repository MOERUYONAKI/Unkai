<?php 

session_start();

if (!isset($_SESSION['mode'])) {
    $_SESSION['mode'] = 'dark';
}

if (isset($_GET['light'])) {
    $_SESSION['mode'] = 'light';
}

if (isset($_GET['dark'])) {
    $_SESSION['mode'] = 'dark';
}

?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Unkai - Serveurs </title>
</head>
<body>
    
</body>
</html>