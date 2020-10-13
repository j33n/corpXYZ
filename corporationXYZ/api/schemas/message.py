from corporationXYZ.models import Message
from corporationXYZ.extensions import ma, db


class MessageSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)

    class Meta:
        model = Message
        sqla_session = db.session
        load_instance = True
