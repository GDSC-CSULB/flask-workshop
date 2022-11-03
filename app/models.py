from app import db


class Course(db.Model):
    department = db.Column(db.String(5), primary_key=True)
    number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    units = db.Column(db.Integer, nullable=False)
    desc = db.Column(db.Text)

    def __repr__(self):
        return f"{self.department} {self.number} {self.name}"
