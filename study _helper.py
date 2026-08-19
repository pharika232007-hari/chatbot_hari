
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "secret123"

# Dummy user (you can later connect database)
USER = {"username": "student", "password": "1234"}

subjects = {
    "Physics": "Mechanics, Thermodynamics, Optics",
    "Chemistry": "Organic, Inorganic, Physical",
    "Mathematics": "Algebra, Calculus, Trigonometry",
    "Biology": "Botany, Zoology, Genetics"
}

# Home -> Redirect to login
@app.route('/')
def home():
    if "user" in session:
        return redirect('/dashboard')
    return redirect('/login')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == USER["username"] and password == USER["password"]:
            session["user"] = username
            return redirect('/dashboard')
        else:
            return "Invalid Credentials"

    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if "user" not in session:
        return redirect('/login')
    return render_template('dashboard.html', subjects=subjects)

# Subject page
@app.route('/subject/<name>')
def subject(name):
    if "user" not in session:
        return redirect('/login')

    info = subjects.get(name, "No data available")
    return render_template('subject.html', name=name, info=info)

# Logout
@app.route('/logout')
def logout():
    session.pop("user", None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(debug=True)
    
