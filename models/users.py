import marshmallow as ma
import uuid
from sqlalchemy.dialects.postgresql import UUID
from models.organizations import OrganizationsSchema
from db import db


class Users(db.Model):
    __tablename__ = "Users"

    user_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String())
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    phone = db.Column(db.String())
    city = db.Column(db.String())
    state = db.Column(db.String())

    org_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Organizations.org_id"), nullable=False)

    active = db.Column(db.Boolean(), default=True)

    def __init__(self, first_name, last_name, email, password, phone, city, state, org_id, active):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.phone = phone
        self.city = city
        self.state = state
        self.org_id = org_id
        self.active = active

    def new_user():
        return Users("", "", "", "", "", "", "", "",True)


class UsersSchema(ma.Schema):
    class Meta:
        fields = ['user_id', 'first_name', 'last_name', 'email', 'city', 'state', 'phone', "organization", 'active']
    organization = ma.fields.Nested(OrganizationsSchema())


user_schema = UsersSchema()
users_schema = UsersSchema(many=True)
