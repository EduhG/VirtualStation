from .. import db


class ReportedCase(db.Model):
    __tablename__ = 'reported_cases'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name
