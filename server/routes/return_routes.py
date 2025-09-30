from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from extensions import db
from datetime import datetime
from decimal import Decimal

from models.tax_return import Return
from models.income import ReturnIncome
from models.deduction import ReturnDeduction


# 1️⃣ Create a tax return
class CreateReturnResource(Resource):
    @jwt_required()
    def post(self):
        user_id = get_jwt_identity()
        data = request.get_json()

        try:

            # Convert strings like "2025-01-01" into Python date objects
            start_date = datetime.strptime(data.get("tax_period_start"), "%Y-%m-%d").date()
            end_date = datetime.strptime(data.get("tax_period_end"), "%Y-%m-%d").date()

            new_return = Return(
                user_id=user_id,
                tax_period_start=start_date,
                tax_period_end=end_date,
                status="draft"
            )
            db.session.add(new_return)
            db.session.commit()

            return {
                "message": "Return created successfully",
                "return_id": new_return.id
            }
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400


# 2️⃣ Add income to a return
class AddIncomeResource(Resource):
    @jwt_required()
    def post(self, return_id):
        user_id = get_jwt_identity()
        data = request.get_json()

        tax_return = Return.query.filter_by(id=return_id, user_id=user_id).first()
        if not tax_return:
            return {"error": "Return not found"}, 404

        try:
            income = ReturnIncome(
                return_id=return_id,
                income_type_id=data.get("income_type_id"),
                description=data.get("description"),
                amount=data.get("amount")
            )
            db.session.add(income)

            # Update total income
            tax_return.total_income += Decimal(str(data.get("amount", "0")))
            db.session.commit()

            return {
                "message": "Income added successfully",
                "return_id": return_id,
                "income_id": income.id
            }
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400


# 3️⃣ Add deduction to a return
class AddDeductionResource(Resource):
    @jwt_required()
    def post(self, return_id):
        user_id = get_jwt_identity()
        data = request.get_json()

        tax_return = Return.query.filter_by(id=return_id, user_id=user_id).first()
        if not tax_return:
            return {"error": "Return not found"}, 404

        try:
            deduction = ReturnDeduction(
                return_id=return_id,
                deduction_type_id=data.get("deduction_type_id"),
                amount=data.get("amount")
            )
            db.session.add(deduction)

            # Update total deductions
            tax_return.total_deductions += Decimal(str(data.get("amount", "0")))
            db.session.commit()

            return {
                "message": "Deduction added successfully",
                "return_id": return_id,
                "deduction_id": deduction.id
            }
        except Exception as e:
            db.session.rollback()
            return {"error": str(e)}, 400
