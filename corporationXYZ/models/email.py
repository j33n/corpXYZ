from corporationXYZ.extensions import db, pwd_context


class Email(db.Model):
    """Basic email model
    """

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    to = db.Column(db.String(1000), nullable=True)
    subject = db.Column(db.String(1000), nullable=True)
    bodyContent = db.Column(db.String(255), nullable=True)
    attachment = db.Column(db.String(255), nullable=True)

    user = db.relationship("User", lazy="joined")

    def __repr__(self):
        return "<Email %s>" % self.email
