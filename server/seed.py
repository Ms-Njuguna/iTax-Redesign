from faker import Faker
from app import create_app, db
from config import TestingConfig
from models.user import User
from models.income import IncomeType, ReturnIncome
from models.deduction import DeductionType, ReturnDeduction
from models.tax_return import Return   # make sure you actually have this file
from models.payment import Payment
from models.login_code import LoginCode
from models.audit import AuditLog
import random

# Initialize app with Testing config (uses test.db)
app = create_app(TestingConfig)
fake = Faker()

def seed_users(n=10):
    users = []
    for _ in range(n):
        user = User(
            full_name=fake.name(),
            email=fake.unique.email(),
            kra_pin=fake.unique.bothify(text="A#########X"),  # like A123456789X
            password_hash="hashed_password",  # replace later with actual hashing
            phone_number=fake.phone_number(),
            national_id=fake.unique.random_number(digits=8),
            role=random.choice(["taxpayer", "admin"])
        )
        users.append(user)
        db.session.add(user)
    db.session.commit()
    print(f"✅ Seeded {n} users")


def seed_income_types():
    income_types = [
        {"name": "Employment", "description": "Salary, wages, bonuses"},
        {"name": "Business", "description": "Business income"},
        {"name": "Rental", "description": "Rental income"},
        {"name": "Investments", "description": "Dividends, interest"}
    ]
    for it in income_types:
        db.session.add(IncomeType(**it))
    db.session.commit()
    print("✅ Seeded income types")


def seed_deduction_types():
    deduction_types = [
        {"name": "NHIF", "description": "Health insurance contribution", "max_limit": 1700.00},
        {"name": "NSSF", "description": "Retirement savings contribution", "max_limit": 2000.00},
        {"name": "Mortgage Interest", "description": "Interest on mortgage loans", "max_limit": 300000.00}
    ]
    for dt in deduction_types:
        db.session.add(DeductionType(**dt))
    db.session.commit()
    print("✅ Seeded deduction types")


# --- Main Seeder Runner ---

if __name__ == "__main__":
    with app.app_context():
        db.drop_all()
        db.create_all()
        print("⚡ Reset DB (dropped & recreated tables)")

        seed_users(20)
        seed_income_types()
        seed_deduction_types()

        print("🎉 Seeding complete! Data saved in test.db")

