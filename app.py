from flask import Flask

app = Flask(_name_)


@app.route('/')
def index():
  html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Perfil de Usuario</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f8f8f8;
            margin: 0;
            padding: 0;
        }
        .container {
            max-width: 600px;
            margin: 20px auto;
            background-color: #fff;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
        }
        .profile-card {
            text-align: center;
        }
        .profile-card img {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            margin-bottom: 20px;
            border: 4px solid #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .profile-card h1 {
            color: #333;
        }
        .profile-card p {
            color: #666;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="profile-card">
            <img src="https://hips.hearstapps.com/hmg-prod/images/hechos-reales-insipiraron-la-monja2-1537099184.jpg?crop=0.564xw:1.00xh;0.219xw,0&resize=1200:*" alt="Mi imagen" width="200" height="150" title="Esta es una imagen">
            <h1>Stefany Campos</h1>
            <p>CEO y fundador, Ejemplo</p>
            <p>Universidad de Harvard</p>
        </div>
    </div>
</body>
</html>

"""
  return html_content


if _name_ == '_main_':
  app.run(host='0.0.0.0', port=8080)