from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from extensions import db, bcrypt
from models.user import User
from models.login_code import LoginCode
from flask_jwt_extended import create_access_token
from datetime import datetime, timedelta, timezone
import random

auth_bp = Blueprint("auth", __name__)
api = Api(auth_bp)

# 👉 Register
class RegisterResource(Resource):
    def post(self):
        data = request.get_json()
        full_name = data.get("full_name")
        email = data.get("email")
        password = data.get("password")
        phone_number = data.get("phone_number")
        national_id = data.get("national_id")

        if User.query.filter_by(email=email).first():
            return {"message": "Email already registered"}, 400

        # Hash password
        pw_hash = bcrypt.generate_password_hash(password).decode("utf-8")

        # Generate KRA PIN (just call your kra_generator here if you want)
        kra_pin = f"A{random.randint(100000000,999999999)}X"

        user = User(
            full_name=full_name,
            email=email,
            password_hash=pw_hash,
            phone_number=phone_number,
            national_id=national_id,
            kra_pin=kra_pin,
            role="taxpayer"
        )
        db.session.add(user)
        db.session.commit()

        return {"message": "User registered successfully", "kra_pin": kra_pin}, 201


# 👉 Login
class LoginResource(Resource):
    def post(self):
        data = request.get_json()
        kra_pin = data.get("kra_pin")
        password = data.get("password")

        user = User.query.filter_by(kra_pin=kra_pin).first()
        if not user or not bcrypt.check_password_hash(user.password_hash, password):
            return {"message": "Invalid KRA PIN or password"}, 401

        # Generate 6-digit confirmation code
        code = str(random.randint(100000, 999999))
        expires = datetime.now(timezone.utc) + timedelta(minutes=5)

        login_code = LoginCode(user_id=user.id, code=code, expires_at=expires, used=False)
        db.session.add(login_code)
        db.session.commit()

        # TODO: send code to email (mock now)
        print(f"Confirmation code for {user.email}: {code}")

        return {"message": "Confirmation code sent to email"}, 200


# 👉 Confirm code
class ConfirmCodeResource(Resource):
    def post(self):
        data = request.get_json()
        kra_pin = data.get("kra_pin")
        code = data.get("code")

        user = User.query.filter_by(kra_pin=kra_pin).first()
        if not user:
            return {"message": "Invalid user"}, 404

        login_code = LoginCode.query.filter_by(user_id=user.id, code=code, used=False).first()
        now = datetime.now(timezone.utc)
        if not login_code or login_code.expires_at.replace(tzinfo=timezone.utc) < now:
            return {"message": "Invalid or expired code"}, 400

        # Mark code as used
        login_code.used = True
        db.session.commit()

        # Generate JWT
        access_token = create_access_token(identity=str(user.id))

        return {
            "message": "Login successful",
            "access_token": access_token,
            "user": {
                "id": user.id,
                "full_name": user.full_name,
                "email": user.email,
                "kra_pin": user.kra_pin,
                "role": user.role
            }
        }, 200


class UsersResource(Resource):
    def get(self):
        users = User.query.all()
        return {
            "users": [
                {
                    "id": u.id,
                    "full_name": u.full_name,
                    "email": u.email,
                    "kra_pin": u.kra_pin,
                    "role": u.role
                } for u in users
            ]
        }, 200



# Register resources
api.add_resource(RegisterResource, "/register")
api.add_resource(LoginResource, "/login")
api.add_resource(ConfirmCodeResource, "/confirm")

api.add_resource(UsersResource, "/user")
