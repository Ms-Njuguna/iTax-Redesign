from flask_restful import Resource

class HelloResource(Resource):
    def get(self):
        return {"message": "Backend is running!"}, 200
