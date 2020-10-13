from flask import request, current_app as app
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, decode_token
from corporationXYZ.api.schemas import UserSchema, EmailSchema
from corporationXYZ.models import Email
from corporationXYZ.extensions import db
from corporationXYZ.commons.pagination import paginate


parser = reqparse.RequestParser()
parser.add_argument('names')
parser.add_argument('email', required=True, help='Email cannot be blank')
parser.add_argument('to', required=True, help='Recipients cannot be blank')
parser.add_argument('subject')
parser.add_argument('bodyContent', required=True, help='Body content cannot be blank')
parser.add_argument('attachment')

parser.add_argument('Authorization', location='headers')


class EmailResource(Resource):
    method_decorators = [jwt_required]

    def post(self):
        args = parser.parse_args()
        # Get user identity
        encoded_token = args['Authorization'].replace("Bearer", "").replace(" ", "")
        decoded_token = decode_token(encoded_token)
        user_identity = decoded_token[app.config["JWT_IDENTITY_CLAIM"]]

        schema = EmailSchema()

        email = Email(
            user_id=user_identity,
            names = args['names'],
            email = args['email'],
            to = args['to'],
            subject = args['subject'],
            bodyContent = args['bodyContent'],
            attachment = args['attachment'],
        )

        db.session.add(email)
        db.session.commit()

        return {"msg": "Email sent!!", "email": schema.dump(email)}, 201
