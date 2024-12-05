from database import db
from sqlalchemy import func


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    date = db.Column(db.DateTime(timezone=True), server_default=func.now(), nullable=False)
    off_diet = db.Column(db.Boolean, nullable=False, server_default="0")
