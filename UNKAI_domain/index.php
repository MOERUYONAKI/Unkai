<?php 
    session_start();
    
    if (isset($_POST["id"])) {
        $host = "localhost";
        $dbname = "hesias";
        $user = "root";
        $pass = "";
        $charset = "utf8mb4";
        $dsn = "mysql:host=$host;port=3307;dbname=$dbname;charset=$charset";
    
        try {
            $pdo = new PDO($dsn, $user, $pass);
    
            $stmt = $pdo->query("SELECT * FROM users");
            $user = [];
    
            while ($row = $stmt->fetch()) {
                $user[$row["ID"]] = $row["name"];
            }
    
            $result = $user[$_POST["id"]];
        } catch (\PDOException $e) {
            $result = $e->getMessage();
        }
    }

    if (isset($_COOKIE["passwd"]) === false) {
        setcookie('passwd', 'null', time() + 10);
    }
    
    if (isset($_POST["name"]) && isset($_POST["passwd"])) { 
        $_SESSION['user'] = $_POST['name'];
    
        if ($_COOKIE['passwd'] === 'null') {
            setcookie('passwd', $_POST['passwd'], time() + 3600);
            $result = 'Bienvenue '.$_SESSION['user'].', vous avez désormais accès à votre espace personnel';
        } else {
    
            if ($_POST['passwd'] === $_COOKIE['passwd']) {
                $result = 'Bienvenue '.$_SESSION['user'].', vous avez désormais accès à votre espace personnel';
            } else {
                $result = 'Mot de passe invalide, réessayez';
            }
        }
    }

    if (isset($_GET['logout'])) {
        session_destroy();
        header('Location: index.php');
    }
?>

<!DOCTYPE html>
<html lang="fr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
        <title> Unkai </title>
    </head>
    <body>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
                <a class="navbar-brand" href="index.php">UNKAI</a>
                <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
                <div class="collapse navbar-collapse" id="navbarNav">
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="#">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Serveurs</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="documentation.php">Documentation</a>
                        </li>
                        <!-- Bouton de déconnexion -->
                        <li class="nav-item">
                            <a href="index.php?logout" class="nav-link disabled" aria-disabled="true">Déconnexion</a>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>

        <!-- <p> <?php // if (isset($result)) { echo($result); } ?> </p> -->

        <button type="button" id="liveToastBtn" class="btn btn-dark">Page de connexion</button>

        <!-- Page de connexion -->
        <div class="toast-container position-fixed bottom-0 end-0 p-3">
            <div id="liveToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                <div class="toast-header">
                    <img src="assets\unkai_discord_picture.png" class="rounded me-2" alt="Unkai profil picture" width="24" height="24">
                    <strong class="me-auto">Connexion</strong>
                    <small>Unkai</small>
                    <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body">
                    <form action="index.php" method="post" class="list-group">
                        <input type="text" name="username" class="list-group-item" required>
                        <input type="password" name="password" class="list-group-item" required>
                        <ul class="list-group list-group-horizontal">
                            <input type="submit" value="Sign in" class="list-group-item list-group-item-action" style="border-top-left-radius: 0%;">
                            <input type="submit" value="Sign up" class="list-group-item list-group-item-action" style="border-top-right-radius: 0%;">
                        </ul>
                    </form>
                </div>
            </div>
        </div> 

        <script type="importmap">
            {
                "imports": {
                    "@popperjs/core": "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/esm/popper.min.js",
                    "bootstrap": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.esm.min.js"
                }
            }
        </script>
        <script type="module">
            import * as bootstrap from 'bootstrap'

            const toastTrigger = document.getElementById('liveToastBtn');
            const toastLiveExample = document.getElementById('liveToast');

            if (toastTrigger) {
                const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
                toastTrigger.addEventListener('click', () => {
                    toastBootstrap.show();
                    console.log(1);
                })
            }
        </script>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    </body>
</html>