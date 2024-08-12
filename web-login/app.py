from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "pass"

# Configuración de MySQL
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_DB'] = "users"
app.config['MYSQL_PASSWORD'] = "---"
mysql = MySQL(app)

@app.route("/")

def home():
    return render_template("home.html")

@app.route('/error-pop-up')
def error():
    return render_template("error-pop-up.html")

@app.route('/inicio')
def inicio():
    return render_template("inicio.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        user = cursor.fetchone()
        cursor.close()
        if user and user[2] == password:
            flash('Inicio de sesión exitoso', 'success')
            return redirect(url_for('inicio'))
        else:
            return redirect(url_for('error'))
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
