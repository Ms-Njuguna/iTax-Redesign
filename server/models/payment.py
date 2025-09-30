from extensions import db
from datetime import datetime, timezone

class Payment(db.Model):
    __tablename__ = "payments"

    id = db.Column(db.Integer, primary_key=True)
    return_id = db.Column(db.Integer, db.ForeignKey("returns.id"), nullable=False)
    payment_reference = db.Column(db.String(100), nullable=False)
    amount = db.Column(db.Numeric(12,2), nullable=False)
    method = db.Column(db.String(50))
    paid_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))
