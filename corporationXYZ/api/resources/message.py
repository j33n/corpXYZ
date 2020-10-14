import os

from flask import request, current_app as app
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, decode_token
from twilio.rest import Client

from corporationXYZ.api.schemas import MessageSchema
from corporationXYZ.models import Message
from corporationXYZ.extensions import db


# Basic validations(emptyness)
parser = reqparse.RequestParser()
parser.add_argument('recipient', required=True, help='Recipient phone number is required')
parser.add_argument('body', required=True, help='Cannot send a blank message')

parser.add_argument('Authorization', location='headers')


class MessageResource(Resource):
    """Single object resource

    ---
    post:
      tags:
        - Messages
      requestBody:
        content:
          application/json:
            schema:
              type: object
              properties:
                recipient:
                  type: string
                  example: "+250788222222"
                  required: true
                body:
                  type: string
                  example: Hello from the Corp api
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
                    example: Message sent!!
                  message: MessageSchema
        400:
          description: a DB or twilio exception error
    """

    method_decorators = [jwt_required]

    def post(self):
        args = parser.parse_args()
        # Get user identity
        encoded_token = args['Authorization'].replace("Bearer", "").replace(" ", "")
        decoded_token = decode_token(encoded_token)
        user_identity = decoded_token[app.config["JWT_IDENTITY_CLAIM"]]

        schema = MessageSchema()

        # Initialize Twilio
        account_sid = app.config["TWILIO_ACCOUNT_SID"]
        auth_token = app.config["TWILIO_AUTH_TOKEN"]
        twilioClient = Client(account_sid, auth_token)

        # Send message
        try:
            sentMessage = twilioClient.messages \
                    .create(
                        body=args['body'],
                        from_=os.getenv("TWILIO_PHONE_NBR"),
                        to=args['recipient']
                    )

            message = Message(
                user_id = user_identity,
                recipient = args['recipient'],
                body = args['body']
            )

            db.session.add(message)
            db.session.commit()

            return {"msg": "Message sent!!", "message": schema.dump(message)}, 201

        except Exception as e:
            return({"error": str(e)})
