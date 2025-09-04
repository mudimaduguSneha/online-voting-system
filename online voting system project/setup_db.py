from app import app
from models import db, Candidate

with app.app_context():
    db.create_all()

    if Candidate.query.count() == 0:
        candidates = [
            Candidate(name='Candidate A'),
            Candidate(name='Candidate B'),
            Candidate(name='Candidate C')
        ]
        db.session.add_all(candidates)
        db.session.commit()
        print("Database initialized and candidates added.")
    else:
        print("Candidates already exist.")
