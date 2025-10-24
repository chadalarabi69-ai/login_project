from flask import Flask, render_template, request, redirect
from database import get_db_connection 

app = Flask(__name__)

@app.route('/')
def home():
    
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
       
        username = request.form['username']
        password = request.form['password']

        
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
        user = cursor.fetchone()
        conn.close()

        
        if user:
            return f"<h2>Welcome, {username}!</h2>"
        else:
            return "<h3>❌ Incorrect username or password.</h3>"

   
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        conn.close()

        
        return redirect('/login')

    return render_template('register.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)

