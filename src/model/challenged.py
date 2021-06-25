from src.app.server import db


class Challenged(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45))
    area = db.Column(db.String(45))
    hard_skills = db.Column(db.String(45))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "area": self.area,
            "hard_skills": self.hard_skills
        }
