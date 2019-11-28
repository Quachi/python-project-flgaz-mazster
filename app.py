from flask import Flask, request, render_template, redirect, url_for
import csv
from flask import json
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)


@app.route('/')
def home():
    return 'Bienvenue !'


@app.route('/gaz', methods=['GET', 'POST'])
def save_gazouille():
    if request.method == 'POST':
        print(request.form)
        dump_to_csv(request.form)
        return redirect(url_for('timeline'))
        # return "OK"
    if request.method == 'GET':
        return render_template('formulaire.html')


@app.route('/timeline', methods=['GET'])
def timeline():
    gaz = parse_from_csv()
    return render_template("timeline.html", gaz=gaz)


@app.route('/twitt', methods=['GET'])
def get_twitt():
    if request.method == 'POST':
        print(request.form)
        dump_to_csv(request.form)
        return redirect(url_for('timeline'))
        # return "OK"
    if request.method == 'GET':
        return render_template('formulaire.html')


@app.route('/message')
def someName():
    messages = Message.query.all()
    for message in messages:
        print(message)
    return render_template('formulaire.html')


def parse_from_csv():
    gaz = []
    with open('./gazouilles.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            gaz.append({"user": row[0], "text": row[1]})
    return gaz


def dump_to_csv(d):
    donnees = [d["user-name"], d["user-text"]]
    with open('./gazouilles.csv', 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(donnees)


class Message(db.Model):
    __tablename__ = 'message'
    id = db.Column(db.Integer,
                   primary_key=True)
    name = db.Column(db.String(64),
                     index=False,
                     unique=True,
                     nullable=False)
    text = db.Column(db.String(80),
                     index=True,
                     unique=True,
                     nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)


class Comments(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))


db.create_all()
