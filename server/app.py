from flask import Flask
from flask_restful import Api
from extensions import db, migrate
from config import Config

# Import resources
# from routes.auth_routes import RegisterResource, LoginResource
# from routes.return_routes import ReturnResource
from routes import HelloResource

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Setup API
    api = Api(app)
    # api.add_resource(RegisterResource, "/api/auth/register")
    # api.add_resource(LoginResource, "/api/auth/login")
    # api.add_resource(ReturnResource, "/api/returns")

    api.add_resource(HelloResource, "/api/hello")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)