from corporationXYZ.extensions import db, pwd_context


class Message(db.Model):
    """Basic message model
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    recipient = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255), nullable=False)

    user = db.relationship("User", lazy="joined")

    def __repr__(self):
        return "<Recipient %s>" % self.recipient
