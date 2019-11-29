"""
      file app: entry point for project gaz
"""

import csv
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql

pymysql.install_as_MySQLdb()

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 300
app.config['CORS_HEADERS'] = 'Content-Type'

DB = SQLAlchemy(app)


@app.route('/')
def home():
    """
   function home: show route index
   """
    return 'Bienvenue !'


@app.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    """
      function save_gazouille: save gazouille or show form to add a gaz
    """
    if request.method == 'POST':
        print(request.form)
        add_message(request.form)
        return redirect(url_for('timeline'))
        # return "OK"
    if request.method == 'GET':
        return render_template('formulaire.html')


@app.route('/timeline', methods=['GET'])
def timeline():
    """
      function timeline: show all gazouille from oldest to latest
      Return
      -------
      template
      render html template
    """
    messages = get_message()
    return render_template("timeline.html", messages=messages)


@app.route('/timeline/<username>', methods=['GET'])
def timeline_user(username):
    """
      function timeline: show all gazouille to one user
      Return
      -------
      template
      render html template timeline
    """
    from models import Message
    messages = Message.query.filter_by(name=username)
    return render_template("timeline.html", messages=messages)


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


def add_message(data):
    """
          function timeline: add message in database
        """
    message = Message(
        name=data["user-name"],
        text=data["user-text"]
    )
    from models import Message
    DB.session.add(message)
    DB.session.commit()


def get_message():
    """
      function timeline: get all message in database
      Return
      -------
      messages
    """
    from models import Message
    messages = Message.query.all()
    return messages


DB.create_all()
