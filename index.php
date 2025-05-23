<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Redirection par l'équipe Cupcake</title>
    <style>
        body {
            font-family: sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f4f4f4;
            margin: 0;
        }
        .message-container {
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        .message {
            color: #333;
            font-size: 1.2em;
            margin-bottom: 20px;
        }
        .redirect-text {
            color: #777;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <div class="message-container">
        <p class="message">
            🧁 Un petit message de l'équipe Cupcake :<br>
            Nous vous redirigeons vers notre nouvelle interface !
        </p>
        <p class="redirect-text">
            Vous allez être automatiquement redirigé dans quelques instants...<br>
            Si la redirection ne fonctionne pas, <a href="/front">cliquez ici</a>.
        </p>
    </div>

    <script>
        setTimeout(function() {
            window.location.href = "/front";
        }, 3000); // Redirection après 3 secondes (3000 millisecondes)
    </script>
</body>
</html>