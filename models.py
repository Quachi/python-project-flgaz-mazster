from app import db


class Message(db.Model):
    __tablename__ = 'Message'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                     index=False,
                     unique=True,
                     nullable=False)
    message = db.Column(db.String(80),
                        index=True,
                        unique=True,
                        nullable=False)
    created = db.Column(db.DateTime,
                        index=False,
                        unique=False,
                        nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.username)
