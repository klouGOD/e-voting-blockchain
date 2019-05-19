from flask_restful import Resource


class TransactionVC(Resource):
    def get(self):
        return {"message": "Hello, World!"}