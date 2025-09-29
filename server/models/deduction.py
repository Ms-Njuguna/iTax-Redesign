from extensions import db

class DeductionType(db.Model):
    __tablename__ = "deduction_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))
    max_limit = db.Column(db.Numeric(12,2))

    # relationships
    return_deductions = db.relationship("ReturnDeduction", backref="deduction_type", lazy=True)


class ReturnDeduction(db.Model):
    __tablename__ = "return_deductions"

    id = db.Column(db.Integer, primary_key=True)
    return_id = db.Column(db.Integer, db.ForeignKey("returns.id"), nullable=False)
    deduction_type_id = db.Column(db.Integer, db.ForeignKey("deduction_types.id"), nullable=False)
    amount = db.Column(db.Numeric(12,2), nullable=False)
