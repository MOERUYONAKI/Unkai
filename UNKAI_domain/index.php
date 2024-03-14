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
        <link href="asset\css\index.css" rel="stylesheet">
        <title> Unkai </title>
    </head>
    <body>
        <div data-bs-theme="light" id="light-mode">
            <nav class="navbar navbar-expand-lg bg-body-tertiary p-2">
                <div class="container-fluid user-select-none">
                    <div class="mode-trigger">
                        <a class="navbar-brand fw-bold" id="dark-mode-trigger" role="button">UNKAI</a>
                    </div>
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="index.php">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Serveurs</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="documentation.php">Documentation</a>
                        </li>
                        <li class="nav-item">
                            <button type="button" id="lightToastTrigger" class="nav-link">Connexion</button>
                        </li>
                    </ul>
                </div>
            </nav>

            <!-- Page de connexion -->
            <div class="toast-container position-fixed bottom-0 end-0 p-3">
                <div id="lightToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                    <div class="toast-header">
                        <img src="assets\unkai_discord_picture.png" class="rounded me-2" alt="Unkai profil picture" width="24" height="24">
                        <strong class="me-auto">Connexion</strong>
                        <small>Powered by Unkai</small>
                        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                    </div>
                    <div class="toast-body">
                        <form action="index.php" method="post" class="list-group p-2">
                            <div class="input-group mb-2">
                                <span class="input-group-text" id="basic-addon1">@</span>
                                <div class="form-floating">
                                    <input type="text" id="floatingUsername" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" required>
                                    <label for="floatingUsername" style="color: grey;">Username</label>
                                </div>
                            </div>
                            <div class="input-group mb-2">
                                <div class="form-floating">
                                    <input type="password" id="floatingPassword" class="form-control" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1" required>
                                    <label for="floatingPassword" style="color: grey;">Password</label>
                                </div>
                            </div>
                            <div class="form-check mb-3">
                                <input class="form-check-input" type="checkbox" id="autoSizingCheck">
                                <label class="form-check-label" for="autoSizingCheck">Remember me</label>
                            </div>
                            <ul class="list-group list-group-horizontal">
                                <input type="submit" value="Sign in" class="list-group-item list-group-item-action">
                                <input type="submit" value="Sign up" class="list-group-item list-group-item-action">
                            </ul>
                        </form>
                    </div>
                </div>
            </div> 
        </div>
        
        <div data-bs-theme="dark" id="dark-mode" style="display: none;">
            <nav class="navbar navbar-expand-lg bg-body-tertiary p-2">
                <div class="container-fluid user-select-none">
                    <div class="mode-trigger">
                        <a class="navbar-brand fw-bold" id="light-mode-trigger" role="button">UNKAI</a>
                    </div>
                    <ul class="navbar-nav">
                        <li class="nav-item">
                            <a class="nav-link active" aria-current="page" href="index.php">Home</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="#">Serveurs</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="documentation.php">Documentation</a>
                        </li>
                        <li class="nav-item">
                            <button type="button" id="darkToastTrigger" class="nav-link">Connexion</button>
                        </li>
                    </ul>
                </div>
            </nav>

            <!-- Page de connexion -->
            <div class="toast-container position-fixed bottom-0 end-0 p-3">
                <div id="darkToast" class="toast" role="alert" aria-live="assertive" aria-atomic="true">
                    <div class="toast-header">
                        <img src="assets\unkai_discord_picture.png" class="rounded me-2" alt="Unkai profil picture" width="24" height="24">
                        <strong class="me-auto">Connexion</strong>
                        <small>Powered by Unkai</small>
                        <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                    </div>
                    <div class="toast-body">
                        <form action="index.php" method="post" class="list-group p-2">
                            <div class="input-group mb-2">
                                <span class="input-group-text" id="basic-addon1">@</span>
                                <div class="form-floating">
                                    <input type="text" id="floatingUsername" class="form-control" placeholder="Username" aria-label="Username" aria-describedby="basic-addon1" required>
                                    <label for="floatingUsername" style="color: grey;">Username</label>
                                </div>
                            </div>
                            <div class="input-group mb-2">
                                <div class="form-floating">
                                    <input type="password" id="floatingPassword" class="form-control" placeholder="Password" aria-label="Password" aria-describedby="basic-addon1" required>
                                    <label for="floatingPassword" style="color: grey;">Password</label>
                                </div>
                            </div>
                            <div class="form-check mb-3">
                                <input class="form-check-input" type="checkbox" id="autoSizingCheck">
                                <label class="form-check-label" for="autoSizingCheck" style="color: lightgrey;">Remember me</label>
                            </div>
                            <ul class="list-group list-group-horizontal">
                                <input type="submit" value="Sign in" class="list-group-item list-group-item-action">
                                <input type="submit" value="Sign up" class="list-group-item list-group-item-action">
                            </ul>
                        </form>
                    </div>
                </div>
            </div> 
        </div>

        <!-- <p> <?php // if (isset($result)) { echo($result); } ?> </p> -->

        <script type="importmap">{"imports": {"@popperjs/core": "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/esm/popper.min.js", "bootstrap": "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.esm.min.js"}}</script>
        <script src="assets\js\index.js" type="module"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.min.js" integrity="sha384-0pUGZvbkm6XF6gxjEnlmuGrJXVbNuzT9qBBavbLwCsOGabYfZo0T0to5eqruptLy" crossorigin="anonymous"></script>
    </body>
</html>