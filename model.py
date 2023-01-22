from portfolio import db

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(120))
    message = db.Column(db.Text)