from extensions import db
from datetime import datetime, timezone

class Return(db.Model):
    __tablename__ = "returns"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    tax_period_start = db.Column(db.Date, nullable=False)
    tax_period_end = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(50), default="draft")
    total_income = db.Column(db.Numeric(12,2), default=0.00)
    total_deductions = db.Column(db.Numeric(12,2), default=0.00)
    total_tax_due = db.Column(db.Numeric(12,2), default=0.00)
    filed_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))

    # relationsips
    incomes = db.relationship("ReturnIncome", backref="return", lazy=True)
    deductions = db.relationship("ReturnDeduction", backref="return", lazy=True)
    payments = db.relationship("Payment", backref="return", lazy=True)
