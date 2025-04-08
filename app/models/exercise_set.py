from app import db

class ExerciseSet(db.Model):
    __tablename__ = 'exercise_set'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.id'), nullable=False)
    set_number = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer)
    weight = db.Column(db.Float)
    notes = db.Column(db.String(500))

    exercise = db.relationship('Exercise', backref=db.backref('sets', lazy=True))

    def __repr__(self):
        return f'<ExerciseSet {self.set_number} for Exercise {self.exercise_id}>' 