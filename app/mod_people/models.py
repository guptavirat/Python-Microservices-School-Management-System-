from app.base_model import BaseModel
from app import db


class Person(BaseModel):
    __tablename__ = 'people'

    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(30), nullable=False, name="e-mail")
    phone = db.Column(db.String(30), nullable=False)
    eid = db.Column(db.String(30), nullable=False)
    gen = db.Column(db.String(30), nullable=False)
    cls = db.Column(db.String(30), nullable=False)
    Adr = db.Column(db.String(30), nullable=False)
    bgr = db.Column(db.String(30), nullable=False)
    fname = db.Column(db.String(30), nullable=False)
    mname = db.Column(db.String(30), nullable=False)
    dob = db.Column(db.String(30), nullable=False)

    @property
    def full_name(self):
        """
        :return: Full name of person (first and last name)
        """
        return "{} {}".format(self.first_name, self.last_name)
