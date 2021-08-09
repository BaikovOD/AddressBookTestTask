import enum
from . import db
from sqlalchemy.sql import func



class AddressValue(enum.Enum):
    low = 'low'
    medium = 'medium'
    high = 'high'


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    address = db.Column(db.String(500))
    city = db.Column(db.String(50))
    state = db.Column(db.String(30))
    postal_code = db.Column(db.String(20))
    value = db.Column(db.Enum(AddressValue))
    created = db.Column(db.DateTime(timezone=True),  default=func.now())