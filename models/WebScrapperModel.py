from database.db import db


class WebScrapper(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(2000), nullable=False)
    author = db.Column(db.String(2000), nullable=False)
    creationDate= db.Column(db.String(2000), nullable=False)
    description = db.Column(db.String(2000), nullable=False)  
    


