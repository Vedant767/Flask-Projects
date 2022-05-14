from enum import unique
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key = True)
    emp_id = db.Column(db.Integer(), unique = True)
    name = db.Column(db.String())
    age = db.Column(db.Integer())
    position = db.Column(db.String(80))


    def __init__(self, emp_id, name, age, position):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.position = position
    
    def __repr__(self) -> str:
        return f"{self.name}:{self.emp_id}"
        