from flask import Flask
from flask_restful import Api
from extensions import db, migrate
from config import Config
from extensions import db, migrate, bcrypt, jwt

# Import resources
# from routes.auth_routes import RegisterResource, LoginResource
# from routes.return_routes import ReturnResource
from routes import HelloResource
from routes.return_routes import CreateReturnResource, AddIncomeResource, AddDeductionResource

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt.init_app(app)

    # Register routes
    from routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    # Setup API
    api = Api(app)
    # api.add_resource(RegisterResource, "/api/auth/register")
    # api.add_resource(LoginResource, "/api/auth/login")
    # api.add_resource(ReturnResource, "/api/returns")

    api.add_resource(HelloResource, "/api/hello")

    from routes.test_routes import test_bp
    app.register_blueprint(test_bp, url_prefix="/api/test")

    api.add_resource(CreateReturnResource, "/api/returns")
    api.add_resource(AddIncomeResource, "/api/returns/<int:return_id>/income")
    api.add_resource(AddDeductionResource, "/api/returns/<int:return_id>/deductions")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)