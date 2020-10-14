from flask import request, current_app as app
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, decode_token
from flask_mail import Message

from corporationXYZ.api.schemas import UserSchema, EmailSchema
from corporationXYZ.models import Email, User
from corporationXYZ.extensions import db, mail
from corporationXYZ.commons.pagination import paginate


parser = reqparse.RequestParser()
parser.add_argument('to', required=True, help='Recipients cannot be blank')
parser.add_argument('subject')
parser.add_argument('bodyContent', required=True, help='Body content cannot be blank')
parser.add_argument('attachment')

parser.add_argument('Authorization', location='headers')


class EmailResource(Resource):
    """Single object resource

    ---
    post:
      tags:
        - Emails
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                to:
                  type: string
                  example: "test@gmail.com"
                  required: true
                subject:
                  type: string
                  example: Hello from the Corp api
                  required: false
                bodyContent:
                  type: string
                  example: Hello, we just wanted to welcome you onboard
                  required: true
      responses:
        201:
          content:
            application/json:
              schema:
                type: object
                properties:
                  msg:
                    type: string
                    example: Email sent!!
                  email: EmailSchema
        400:
          description: a DB or mailtrap exception error
    """
    method_decorators = [jwt_required]

    def post(self):
        args = parser.parse_args()
        # Get user identity
        encoded_token = args['Authorization'].replace("Bearer", "").replace(" ", "")
        decoded_token = decode_token(encoded_token)
        user_identity = decoded_token[app.config["JWT_IDENTITY_CLAIM"]]

        schema = EmailSchema()

        # Fetch user info by ID
        user = User.query.get_or_404(user_identity)

        # Send the email
        try:
            msg = Message(
                args['subject'],
                sender=user.companyEmail,
                recipients=args['to'].split(",")
            )
            msg.body = args['bodyContent']
            mail.send(msg)
            
            email = Email(
                user_id = user_identity,
                to = args['to'],
                subject = args['subject'],
                bodyContent = args['bodyContent'],
                attachment = args['attachment'],
            )
            
            db.session.add(email)
            db.session.commit()
            return {"msg": "Email sent!!", "email": schema.dump(email)}, 201
        except Exception as e:
            return({"error": str(e)}) 

        
