from extensions import db

class IncomeType(db.Model):
    __tablename__ = "income_types"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255))

    # relationships
    return_incomes = db.relationship("ReturnIncome", backref="income_type", lazy=True)


class ReturnIncome(db.Model):
    __tablename__ = "return_income"

    id = db.Column(db.Integer, primary_key=True)
    return_id = db.Column(db.Integer, db.ForeignKey("returns.id"), nullable=False)
    income_type_id = db.Column(db.Integer, db.ForeignKey("income_types.id"), nullable=False)
    description = db.Column(db.String(255))
    amount = db.Column(db.Numeric(12,2), nullable=False)
