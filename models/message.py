"""
      file message: DAO message
"""
from run import db
from sqlalchemy import Column, String, Integer


class Message(db.Model):
    """
      class Message: DTO of message
    """
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True)
    name = Column(String(64),
                  index=False,
                  nullable=False)
    text = Column(String(280),
                  index=True,
                  nullable=False)

    def __repr__(self):
        return '<Message {}>'.format(self.name)
