from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Candidate

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('candidates'))
        else:
            return "Invalid credentials"
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if User.query.filter_by(username=username).first():
            return "Username already exists!"

        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/candidates')
def candidates():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if user.has_voted:
        return redirect(url_for('results'))

    all_candidates = Candidate.query.all()
    return render_template('candidates.html', candidates=all_candidates)

@app.route('/vote', methods=['POST'])
def vote():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])
    if user.has_voted:
        return redirect(url_for('results'))

    candidate_id = request.form.get('candidate_id')
    candidate = Candidate.query.get(candidate_id)
    if candidate:
        candidate.votes += 1
        user.has_voted = True
        db.session.commit()
        return redirect(url_for('results'))

    return "Candidate not found"

@app.route('/results')
def results():
    candidates = Candidate.query.all()
    results = {candidate.name: candidate.votes for candidate in candidates}
    return render_template('result.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)
