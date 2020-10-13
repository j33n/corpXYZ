from corporationXYZ.models import Email
from corporationXYZ.extensions import ma, db


class EmailSchema(ma.SQLAlchemyAutoSchema):

    id = ma.Int(dump_only=True)

    class Meta:
        model = Email
        sqla_session = db.session
        load_instance = True
