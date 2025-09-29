from extensions import db
from datetime import datetime, timezone


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    kra_pin = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String, nullable=False)
    phone_number = db.Column(db.String,)
    national_id = db.Column(db.String)
    role = db.Column(db.String, default="taxpayer")
    created_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime(timezone=True), default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))
    
    # relationships
    returns = db.relationship("Return", backref="user", lazy=True)
    login_codes = db.relationship("LoginCode", backref="user", lazy=True)
    audit_logs = db.relationship("AuditLog", backref="user", lazy=True)

    