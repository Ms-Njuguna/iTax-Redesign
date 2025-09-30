# routes/test_routes.py
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity

test_bp = Blueprint("test_bp", __name__)

@test_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user_id = int(get_jwt_identity())
    return jsonify(message="You accessed a protected route!", user_id=user_id)

