import enum
from . import db
import sqlalchemy as sa
from datetime import datetime, timezone


# for the datatime field with timezones UTC format
class TimeStamp(sa.types.TypeDecorator):
    impl = sa.types.DateTime
    LOCAL_TIMEZONE = datetime.utcnow().astimezone().tzinfo

    def process_bind_param(self, value: datetime, dialect):
        if value.tzinfo is None:
            value = value.astimezone(self.LOCAL_TIMEZONE)

        return value.astimezone(timezone.utc)

    def process_result_value(self, value, dialect):
        if value.tzinfo is None:
            return value.replace(tzinfo=timezone.utc)

        return value.astimezone(timezone.utc)


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
    created = db.Column(TimeStamp(), default=datetime.now(timezone.utc))