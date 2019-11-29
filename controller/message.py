"""
      file message: service message
"""
import csv

from models.message import Message
from run import db


def add_message(data):
    """
      function timeline: add message in database
    """
    message = Message(
        name=data["user-name"],
        text=data["user-text"]
    )
    db.session.add(message)
    db.session.commit()


def get_message():
    """
      function timeline: get all message in database
      Return
      -------
      messages
    """
    messages = Message.query.all()
    return messages


def parse_from_csv():
    """
      function timeline: read and return all data in gazouille
      Return
      -------
      array gaz
    """
    gaz = []
    with open('./gazouilles.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            gaz.append({"user": row[0], "text": row[1]})
    return gaz


def dump_to_csv(data):
    """
      function timeline: add data in gazouille csv
    """
    donnees = [data["user-name"], data["user-text"]]
    with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(donnees)
