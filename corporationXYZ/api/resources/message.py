from flask import request, current_app as app
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, decode_token
from corporationXYZ.api.schemas import MessageSchema
from corporationXYZ.models import Message
from corporationXYZ.extensions import db


parser = reqparse.RequestParser()
parser.add_argument('recipient', required=True, help='Recipient phone number is required')
parser.add_argument('body', required=True, help='Cannot send a blank message')

parser.add_argument('Authorization', location='headers')


class MessageResource(Resource):
    method_decorators = [jwt_required]

    def post(self):
        args = parser.parse_args()
        # Get user identity
        encoded_token = args['Authorization'].replace("Bearer", "").replace(" ", "")
        decoded_token = decode_token(encoded_token)
        user_identity = decoded_token[app.config["JWT_IDENTITY_CLAIM"]]

        schema = MessageSchema()

        message = Message(
            user_id=user_identity,
            recipient = args['recipient'],
            body = args['body']
        )

        db.session.add(message)
        db.session.commit()

        return {"msg": "Message sent!!", "message": schema.dump(message)}, 201
